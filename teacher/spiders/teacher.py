# -*- coding: utf-8 -*-
import scrapy
import time
import numpy
import re
import sys
import json
from lxml import html

from teacher.items import TeacherItem


class teacherSpider(scrapy.Spider):
    name = "teacher"
    domain = "http://www.job910.com"
    # 目标地址
    start_urls = []
    def __init__(self):
        self.start_urls.append(self.domain+"/search.aspx")

    def parse(self, response):
        classList = self.getClass(response)
        for item in classList:
            for child in item['children']:
                    request = scrapy.Request(self.domain+'/search.aspx?funtype='+child['id'],callback=self.getPages)
                    request.meta['typeName'] = item['name']+','+child['name']
                    yield request                

    def getClass(self,response):
        data = []
        childrenArr = []
        
        i = 0
        for classList in response.xpath("//div[@class='type-content']/div[@class='filter-con-l2']"):
            for item in classList.xpath(".//div[@class='filter-l2-list']"): 
                arr = []
                index = 0
                for id in item.xpath("a/@data-code").extract():
                    arr.append({
                        'id':id
                    })
                for name in item.xpath("a/text()").extract():
                    arr[index]['name'] = name
                    index+=1
                childrenArr.append(arr)
        for classList in response.xpath("//div[@id='search-filter-wrapper']/div[@class='filters-by-type pb4']/div[@class='type-content']/div[@class='filter-con-l1']"):
                for id in classList.xpath("a/@data-code").extract():
                    data.append({
                        'id':id
                    })
                for name in classList.xpath("a/text()").extract():
                    data[i]['name'] = name
                    data[i]['children'] = childrenArr[i]
                    i+=1
        return data
    def getPages(self,response):
        typeName = response.meta['typeName']
        pageNum = response.xpath('//span[@class="pager-mini"]/span/text()').extract()
        if len(pageNum)==0:
            request = scrapy.Request(response.url,callback=self.getTeacherList)
            request.meta['typeNames'] = typeName
            yield request
        else:
            i = 1 
            while i<=int(pageNum[2]):
                request = scrapy.Request(response.url+'&'+'pageIndex='+str(i),callback=self.getTeacherList)
                request.meta['typeNames'] = typeName
                i+=1
                yield request
    def getTeacherList(self,response):
        typeNames = response.meta['typeNames']
        for url in response.xpath('//ul[@id="search-result"]/li/div[@class="info-col-1st"]/div[@class="position title"]/a[@class="extend"]/@href').extract():
            print(self.domain+url)
            request = scrapy.Request(self.domain+url,callback=self.getTeacherInfo)
            request.meta['jobClass'] = typeNames
            yield request
    def getTeacherInfo(self,response):
        item = TeacherItem()
        item['savetype'] = 4
        item['job_class'] = response.meta['jobClass']
        res = response.xpath("//div[@id='jobs-page']")
        item['name'] = res.xpath('//span[@class="name"]/text()').extract()[0]
        item['company_name'] = res.xpath('//div[@class="job-name"]/div[@class="company"]/a/text()').extract()[0]
        msg = res.xpath('//div[@class="job_request"]/p/span/text()').extract()
        arr = msg[0].split('/')
        salary = re.findall(r"(\d+)[WK]",msg[0])
        try:
            if arr[1].strip()=='年':
                item['minsalary'] = int(salary[0])*10/12
                item['maxsalary'] = int(salary[1])*10/12
            else:
                item['minsalary'] = salary[0]
                item['maxsalary'] = salary[1]
        except Exception as e:
            item['minsalary'] = 0
            item['maxsalary'] = 0
            print('面议问题...')
        item['area'] = msg[1]
        timer = re.findall(r'(.+)?年以上',msg[2])
        if not timer:
           timer = re.findall(r'经验(不限)',msg[2]) 
        item['timer'] = timer[0] if timer else ''
        education = re.findall(r'(.+)?及以上',msg[3])
        item['education'] = education[0] if education else ''
        item['job'] = msg[4]
        item['description'] =  res.xpath('//div[@class="desc-wrap"]').extract()[0]
        contents = res.xpath('//div[@class="desc-wrap contact"]/div/text()').extract()
        item['contact'] = contents[0]
        item['address'] = contents[1]
        
        phoneId = res.xpath('//a[@class="green-tip showphone"]/@rel').extract()[0]
        request = scrapy.Request('http://www.job910.com/api/job/index.ashx?jobid='+phoneId+'&d_type=phone',callback=self.getContact)
        request.meta['item'] = item
        url = res.xpath('//div[@class="job-name"]/div[@class="company"]/a/@href').extract()[0]
        request.meta['url'] = url
        
        yield request
    
    def getContact(self,response):
        item = response.meta['item']
        res = json.loads(response.body)
        item['phone'] = res['Data']['Phone']
        for key in item:
            if isinstance(item[key],str):
                item[key] = item[key].strip()
        url = response.meta['url']
        request = scrapy.Request('http://www.job910.com'+url,callback=self.getCompanyIfo)
        request.meta['item'] = item
        yield request

    
    def getCompanyIfo(self,response):
        item = response.meta['item']
        item['company_name'] = response.xpath("//div[@class='school-primary']/h1/text()").extract()[0].strip()
        arr = response.xpath("//div[@class='school-primary']/p[@class='school-summary']/span/text()").extract()
        if len(arr):
            item['pr'] = arr[1]
            item['mun'] = arr[2]
        res = response.xpath("//div[@class='school-link']/a/@href").extract()
        if res:
            item['website'] = res[0]
        else:
            item['website'] = ''
        info = response.xpath("//div[@class='school-desc overflow']").extract()
        if info:
            item['school_desc'] = info[0]
        else:
            item['school_desc'] = ''
        yield item



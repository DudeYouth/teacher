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
    # 目标地址
    start_urls = []
    def __init__(self):
        n = 1
        while n <= 1457:
            self.start_urls.append("http://www.job910.com/search.aspx?pageIndex="+str(n))
            n+=1

    def parse(self, response):
        # for url in response.xpath("//ul[@class='famous-hot-info clearfix']/li/a/@href").extract():
        #     request = scrapy.Request(url,callback=self.getTeacherMsg)
        #     yield request
        for url in response.xpath("//ul[@class='search-result-list']/li/div[@class='info-col-1st']/div/a/@href").extract():
            request = scrapy.Request('http://www.job910.com'+url,callback=self.getTeacherInfo)
            yield request
    #def getTeacherMsg(self,response):  
        # for url in response.xpath("//div[@class='joblist']/ul/li/a/@href").extract():
        #     url = 'http:'+url
        #     request = scrapy.Request(url,callback=self.getTeacherInfo)
        #     yield request
    def getClass(self,response):
        data = []
        childrenArr = []
        index = 0
        i = 0
        for classList in response.xpath("//div[@class='type-content']/div[@class='filter-con-l2']").extract():
            item in classList.xpath("//a[@class='filter-con-l2']/div[class='filter-l2-list']").extract(): 
                arr = []
                id in item.xpath("//a/@data-code)").extract():
                    arr.append({
                        id:id
                    })
                name in item.xpath("//a/text()").extract():
                    arr[index].name = name
                    index+=1
                childrenArr.append(arr)  
        for classList in response.xpath("//div[@class='type-content']/div[@class='filter-con-l1']").extract():
            item in classList.xpath("//a[@class='filter-l1 filter-position']").extract():
                id in item.xpath("//a/@data-code)").extract():
                    data.append({
                        id:id
                    })
                name in item.xpath("//a/text()").extract():
                    data[i].name = name
                    arr[i].children = childrenArr[i]
                    i+=1

    def getTeacherInfo(self,response):
        item = TeacherItem()
        item['savetype'] = 4
        res = response.xpath("//div[@id='jobs-page']")
        item['name'] = res.xpath('//span[@class="name"]/text()').extract()[0]
        item['job_class'] = item['name']
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



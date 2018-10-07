# -*- coding: utf-8 -*-
import scrapy
import time
import numpy
import re
import sys

from teacher.items import TeacherItem


class teacherSpider(scrapy.Spider):
    name = "teacher"
    # 目标地址
    start_urls = [
        "http://www.job910.com"
    ]

    def parse(self, response):
        for url in response.xpath("//ul[@class='famous-hot-info clearfix']/li/a/@href").extract():
            request = scrapy.Request(url,callback=self.getTeacherMsg)
            yield request

    def getTeacherMsg(self,response):
        
        for url in response.xpath("//div[@class='joblist']/ul/li/a/@href").extract():
            url = 'http:'+url
            request = scrapy.Request(url,callback=self.getTeacherInfo)
            yield request

    def getTeacherInfo(self,response):
        item = TeacherItem()
        item['savetype'] = 4
        res = response.xpath("//div[@id='jobs-page']")
        item['name'] = res.xpath('//div[@class="company"]/text()').extract()[0]
        item['job_class'] = res.xpath('//span[@class="name"]/text()').extract()[0]
        msg = res.xpath('//div[@class="job_request"]/p/span/text()').extract()
        print([msg,31321321312])
        sys.exit()
        salary = re.findall(r"(\d+)W",msg[0])
        item['minsalary'] = salary[0]
        item['maxsalary'] = salary[1]
        item['area'] = msg[1]
        timer = re.findall(r'(.+)?年以上',msg[2])
        item['timer'] = timer[0] if timer else '';
        education = re.findall(r'(.+)?及以上',msg[3])
        item['education'] = education[0] if education else ''
        item['job'] = msg[4]
        item['description'] = res.xpath('//div[@class="desc-wrap"]/text()').extract()[0];
        contents = res.xpath('//div[@class="ddesc-wrap contact"]/div/text()').extract();
        item['contact'] = contents[0]
        item['address'] = contents[1]
        phoneId = res.xpath('//a[@class="green-tip showphone"]/@rel').extract()[0];
        request = scrapy.Request('http://www.job910.com/api/job/index.ashx?jobid='+phoneId+'&d_type=phone',callback=self.getContact)
        item['phone'] = request.meta['phone']
    
    def getContact(self,response):
        response.meta['phone'] = response['Data']['Phone']





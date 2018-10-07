# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TeacherItem(scrapy.Item):
    # define the fields for your item here like:
    savetype = scrapy.Field()
    name = scrapy.Field()
    job_class = scrapy.Field()
    level = scrapy.Field()
    minsalary = scrapy.Field()
    maxsalary = scrapy.Field()
    area = scrapy.Field()
    timer = scrapy.Field()
    education = scrapy.Field()
    job = scrapy.Field()
    description = scrapy.Field()
    contact = scrapy.Field()
    address = scrapy.Field()
    phone = scrapy.Field()
    pass

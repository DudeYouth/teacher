# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
import md5

class TeacherPipeline(object):
    timers = {
        '一':'1年以上',
        '二':'2年以上',
        '三':'3年以上',
        '五':'5年以上',
        '八':'8年以上',
        '十':'10年以上'
    }

    def __init__(self):  
        # 建立数据库连接  
        self.connect = pymysql.connect('localhost','root','','phpyun_test',use_unicode=True,charset='utf8')  
        # 获取游标 
        self.cursor = self.connect.cursor()  
        print("connecting mysql success!")  

    def process_item(self, item, spider):
        # 工作经验
        timerSql = "select id from zpcomclass where name='%s'"%(timers[item['timer']]);
        self.cursor.execute(timerSql)
        timerData = self.cursor.fetchone()
        if not timerData:
            item['timer'] = timerData['id']

        # 学历
        educationSql = "select id from zpcomclass where name='%s'"%(item['education']);
        self.cursor.execute(educationSql)
        educationData = self.cursor.fetchone()
        if educationData:
            item['education'] = educationData['id']
        else
            educationSql = "select max(sort) from zpcomclass where keyid=38;
            self.cursor.execute(educationSql)
            educationData = self.cursor.fetchone()
            educationSql = "insert into zpcomclass(keyid,name,variable,sort) value(7,'%s','',%d)"%(item['education'],int(educationData['sort'])+1);
            self.cursor.execute(educationSql)
            item['education'] = self.cursor.lastrowid

        # 职业类型
        jobClassSql = "select id from zpjob_class where name='%s'"%(item['job_class'])
        self.cursor.execute(jobClassSql)
        jobClassData = self.cursor.fetchone()
        if jobClassData:
            item['job_class'] = jobClassData['id']
        else:
            jobClassSql = "insert into zpjob_class(keyid,name,sort,content) value(87,'%s',0,'')"%(item['job_class'])
            self.cursor.execute(jobClassSql)
            item['job_class'] = self.cursor.lastrowid
        
        self.connect.commit() 
        return item
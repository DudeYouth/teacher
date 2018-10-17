# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
import phpserialize

class TeacherPipeline(object):
    timers = {
        '一':'1年以上',
        '两':'2年以上',
        '三':'3年以上',
        '四':'4年以上',
        '五':'5年以上',
        '六':'6年以上',
        '七':'7年以上',
        '八':'8年以上',
        '十':'10年以上',
        '不限':'不限',
    }

    def __init__(self):  
        # 建立数据库连接  
        self.connect = pymysql.connect('localhost','root','','phpyun_test',use_unicode=True,charset='utf8',cursorclass = pymysql.cursors.DictCursor)  
        # 获取游标 
        self.cursor = self.connect.cursor()  
        print("connecting mysql success!")  

    def process_item(self, item, spider):
        jsons = {}
        # 工作经验
        timer = self.timers[item['timer']] if item['timer'] else '应届毕业生'
        timerSql = "select id from zpcomclass where name='%s'"%(timer)
        self.cursor.execute(timerSql)
        timerData = self.cursor.fetchone()
        if timerData:
            jsons['exp'] = timerData['id']
        else:
            timerSql = "select * from zpcomclass where keyid=10"
            self.cursor.execute(timerSql)
            timerData = self.cursor.fetchone()
            sort = 0
            if timerData:
                sort = timerData['sort']
            timerSql = "insert into zpcomclass(keyid,name,variable,sort) value(10,'%s','',%d)"%(item['education'],sort+1)
            self.cursor.execute(timerSql)
            jsons['exp'] = self.cursor.lastrowid
        # 学历
        educationSql = "select id from zpcomclass where name='%s'"%(item['education']);
        self.cursor.execute(educationSql)
        educationData = self.cursor.fetchone()
        if educationData:
            jsons['edu'] = educationData['id']
        else:
            educationSql = "select max(sort) sort from zpcomclass where keyid=38"
            self.cursor.execute(educationSql)
            educationData = self.cursor.fetchone()
            sort = 0
            if timerData:
                sort = educationData['sort']
            educationSql = "insert into zpcomclass(keyid,name,variable,sort) value(38,'%s','',%d)"%(item['education'],sort+1)
            self.cursor.execute(educationSql)
            jsons['edu'] = self.cursor.lastrowid

        # 职业类型
        jobClassSql = "select id from zpjob_class where name='%s'"%(item['job_class'])
        self.cursor.execute(jobClassSql)
        jobClassData = self.cursor.fetchone()
        if jobClassData:
            jsons['job_post'] = jobClassData['id']
        else:
            jobClassSql = "insert into zpjob_class(keyid,name,sort,content) value(87,'%s',0,'')"%(item['job_class'])
            self.cursor.execute(jobClassSql)
            jsons['job_post'] = self.cursor.lastrowid

        # 城市地址
        areas = item['area'].split('-');
        areaSql = "select id from zpcity_class where keyid=0 and name like '%%%s%%'"%(areas[0])
        self.cursor.execute(areaSql)
        areaData = self.cursor.fetchone()
        jsons['provinceid'] = areaData['id']
        areaSql = "select id from zpcity_class where keyid=%d and name like '%%%s%%'"%(areaData['id'],areas[1])
        self.cursor.execute(areaSql)
        areaData = self.cursor.fetchone()
        print([jsons['provinceid'],areaData,areas,454654654564654645646456])
        jsons['cityid'] = areaData['id']
        if len(areas)>2:
            areaSql = "select id from zpcity_class where keyid=%d and name like '%%%s%%'"%(areaData['id'],areas[2])
            self.cursor.execute(areaSql)
            areaData = self.cursor.fetchone()
            jsons['three_cityid'] = areaData['id']
        jsons['minsalary'] = item['minsalary']
        jsons['maxsalary'] = item['maxsalary']
        jsons['hy'] = 35
        jsons['number'] = 40
        jsons['report'] = 54
        jsons['age'] = 88     
        jsons['sex'] = 3 
        jsons['marriage'] = 72 
        jsons['lang[]'] = 100 
        jsons['islink'] = 1 
        jsons['link_man'] = ''
        jsons['link_moblie'] = '' 
        jsons['tblink'] = jsons['report'] 
        jsons['isemail'] = 1
        jsons['email'] = ''
        jsons['submitBtn'] = "提 交 操 作" 
        jsons['jobcopy'] = ''
        jsons['state'] = '' 
        jsons['save'] = '' 
        jsons['name'] = item['name'] 
        jsons['description'] = item['description']
        # save = phpserialize.dumps(jsons)
        # sqlstr = "insert into zplssave(uid,save,savetype) values(%d,'%s',4)"%(uid,save)
        # self.cursor.execute(sqlstr)
        sqlstr = "select max(uid) uid from zpcompany"
        self.cursor.execute(sqlstr)
        userData = self.cursor.fetchone()
        uid = int(userData['uid'])+1 if userData else 1;
        sqlstr = "insert into zpcompany set name='%s',shortname='%s',hy=35,pr=23,provinceid=%d,cityid=%d,three_cityid=%d,mun=3,address='%s',linktel='%s'"%(item['company_name'],item['company_name'],jsons['provinceid'],jsons['cityid'],jsons['three_cityid'],item['address'],item['phone'])
        self.cursor.execute(sqlstr)
        uid = self.cursor.lastrowid
        sqlstr = "insert into zpcompany_job set uid=%d,name='%s',com_name='%s',hy=35,job1=23,job1_son=87,number=40,exp=%d,edu=%d,report=54,sex=3,marriage=72,provinceid=%d,cityid=%d,three_cityid=%d,mun=3,description='%s',minsalary=%d,maxsalary=%d,age=%d,lang=%d"%(uid,item['company_name'],item['company_name'],jsons['exp'],jsons['edu'],jsons['provinceid'],jsons['cityid'],jsons['three_cityid'],jsons['description'],jsons['minsalary'],jsons['maxsalary'],88,101)
        print("insert into zpcompany_job set uid=%d,name='%s',com_name='%s',hy=35,job1=23,job1_son=87,number=40,exp=%d,edu=%d,report=54,sex=3,marriage=72,provinceid=%d,cityid=%d,three_cityid=%d,mun=3,description='%s',minsalary=%d,maxsalary=%d,age=%d,lang=%d"%(uid,item['company_name'],item['company_name'],jsons['exp'],jsons['edu'],jsons['provinceid'],jsons['cityid'],jsons['three_cityid'],jsons['description'],jsons['minsalary'],jsons['maxsalary'],88,101))
        self.cursor.execute(sqlstr)
        jobid = self.cursor.lastrowid
        sqlstr = "insert into uid,jobid"%(uid,jobid)
        self.cursor.execute(sqlstr)
        self.connect.commit() 
        return item
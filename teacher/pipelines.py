# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
import phpserialize
import hashlib
import json

class TeacherPipeline(object):
    types = {
    }
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
    citys = [
        '上海',
        '重庆',
        '天津',
        '北京'
    ]
    def read_json(self):
        file_obj = open('./data.json')
        content = file_obj.read()
        self.json = json.loads(content)
    def __init__(self): 
        self.read_json()
        # 建立数据库连接  
        self.connect = pymysql.connect(host='',port=,user='root',passwd='',db='phpyun',use_unicode=True,charset='utf8',cursorclass = pymysql.cursors.DictCursor)  
        #self.connect = pymysql.connect(host='localhost',port=3306,user='root',passwd='',db='phpyun_test',use_unicode=True,charset='utf8',cursorclass = pymysql.cursors.DictCursor)  
        # 获取游标 
        self.cursor = self.connect.cursor()  
        print("connecting mysql success!")  

    def process_item(self, item, spider):
        job_class = item['job_class']
        try:
            job_class = self.json[item['job_class']]
        except Exception as e:
            job_class = item['job_class']
        job_class = job_class.split(',')
        job_class1 = job_class[0]
        job_class2 = job_class[1]
        sqlstr = "select id from zpcomclass where name='%s'"%(item['pr'])
        self.cursor.execute(sqlstr)
        prData = self.cursor.fetchone()
        prId = 0
        if prData:
            prId = prData['id']
        else:
            sqlstr = "insert into zpcomclass(keyid,name,variable,sort) value(0,'%s','',%d)"%(item['pr'],1)
            self.cursor.execute(sqlstr)
            prId = self.cursor.lastrowid

        sqlstr = "select id from zpcomclass where name='%s'"%(item['mun'])
        self.cursor.execute(sqlstr)
        munData = self.cursor.fetchone()
        munId = 0
        if munData:
            munId = munData['id']
        else:
            sqlstr = "insert into zpcomclass(keyid,name,variable,sort) value(0,'%s','',%d)"%(item['mun'],1)
            self.cursor.execute(sqlstr)
            munId = self.cursor.lastrowid
        # sqlstr = "update zpcompany set pr=%d,mun=%d where name='%s'"%(prId,munId,item['company_name'])
        # self.cursor.execute(sqlstr)
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
            timerSql = "insert into zpcomclass(keyid,name,variable,sort) value(10,'%s','',%d)"%(timer,sort+1)
            self.cursor.execute(timerSql)
            jsons['exp'] = self.cursor.lastrowid
        # 学历
        educationSql = "select id from zpcomclass where name='%s'"%(item['education'])
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
        jobClassSql = "select id from zpjob_class where name='%s'"%(job_class1)
        self.cursor.execute(jobClassSql)
        jobClassData = self.cursor.fetchone()
        if jobClassData:
            job_post = jobClassData['id']
        else:
            jobClassSql = "insert into zpjob_class(keyid,name,sort,content) value(0,'%s',0,'')"%(job_class1)
            self.cursor.execute(jobClassSql)
            job_post = self.cursor.lastrowid

        jobClassSql = "select id from zpjob_class where keyid=%d and name='%s'"%(job_post,job_class2)
        self.cursor.execute(jobClassSql)
        jobClassData = self.cursor.fetchone()
        if jobClassData:
            jsons['job_post'] = jobClassData['id']
        else:
            jobClassSql = "insert into zpjob_class(keyid,name,sort,content) value(%d,'%s',0,'')"%(job_post,job_class2)
            self.cursor.execute(jobClassSql)
            jsons['job_post'] = self.cursor.lastrowid
        # 城市地址
        areas = item['area'].split('-')
        areaSql = "select id from zpcity_class where keyid=0 and name like '%%%s%%'"%(areas[0])
        self.cursor.execute(areaSql)
        areaData = self.cursor.fetchone()
        jsons['provinceid'] = areaData['id']
        jsons['cityid'] = 0
        if len(areas)<3 and areas[0] in self.citys:
            try:
                temp = areas[1]
                areas[1] = areas[0]
                areas.append(temp)
            except Exception as e:
                areas[1] = 0
        try:
            areaSql = "select id from zpcity_class where keyid=%d and name like '%%%s%%'"%(jsons['provinceid'],areas[1])
            self.cursor.execute(areaSql)
            areaData = self.cursor.fetchone()
            jsons['cityid'] = areaData['id']
        except Exception as e:
            jsons['cityid'] = 0

        try:
            if len(areas)>2:
                areaSql = "select id from zpcity_class where keyid=%d and name like '%%%s%%'"%(jsons['cityid'],areas[2])
                self.cursor.execute(areaSql)
                areaData = self.cursor.fetchone()
                jsons['three_cityid'] = areaData['id']
            else:
                jsons['three_cityid'] = 0
        except Exception as e:
                jsons['three_cityid'] = 0
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

        sqlstr = "select uid from zpcompany where name='%s'"%(item['company_name'])
        self.cursor.execute(sqlstr)
        userData = self.cursor.fetchone()
        if not userData:
            sqlstr = "select max(moblie) moblie from zpmember"
            self.cursor.execute(sqlstr)
            moblieData = self.cursor.fetchone()
            if moblieData['moblie']:
                moblie = int(moblieData['moblie'])+1
            else:
                moblie = '13800000000'
            salt = '86a069'
            password = '136139..'
            password = hashlib.md5(password.encode(encoding='UTF-8')).hexdigest()+salt
            password = hashlib.md5(password.encode(encoding='UTF-8')).hexdigest()
            sqlstr = "insert into zpmember set username='%s',password='%s',moblie='%s',status=1,login_ip='119.130.207.169',usertype=2,salt='%s'"%(item['company_name'],password,str(moblie),salt)
            self.cursor.execute(sqlstr)
            uid = self.cursor.lastrowid
            sqlstr = "insert into zpcompany set uid=%d,hy=35,name='%s',shortname='%s',provinceid=%d,cityid=%d,three_cityid=%d,busstops='',welfare='',content='%s',website='%s',pr=%d,mun=%d"%(uid,item['company_name'],item['company_name'],jsons['provinceid'],jsons['cityid'],jsons['three_cityid'],pymysql.escape_string(item['school_desc']),item['website'],munId,prId)
            self.cursor.execute(sqlstr)
            sqlstr = "insert into zpcompany_statis set uid=%d,sq_job=0,all_pay=0,consum_pay=0,fav_job=0,rating=3,rating_name='免费会员',job_num=20,editjob_num=20,breakjob_num=20,part_num=10,editpart_num=10,breakpart_num=10"%(uid)
            self.cursor.execute(sqlstr)
        else:
            uid = userData['uid']
        sqlstr = "select id,uid from zpcompany_job where uid=%d and name='%s' and com_name='%s'"%(uid,item['name'],item['company_name'])
        self.cursor.execute(sqlstr)
        jobData = self.cursor.fetchone()
        if not jobData:
            try:
                sqlstr = "select keyid from zpjob_class where id=%d"%(jsons['job_post'])
                self.cursor.execute(sqlstr)
                jobData = self.cursor.fetchone()
                job1 = jobData['keyid']
                sqlstr = "insert into zpcompany_job set uid=%d,name='%s',com_name='%s',state=1,job1=%d,job1_son=%d,job_post=0,type=0,cert='',welfare='',sdate=unix_timestamp(now()),lastupdate=unix_timestamp(now()),statusbody='',edate=unix_timestamp(now()),hy=35,number=40,exp=%d,edu=%d,report=54,sex=3,marriage=72,provinceid=%d,cityid=%d,three_cityid=%d,mun=3,description='%s',minsalary=%d,maxsalary=%d,age=%d,lang=%d"%(uid,item['name'],item['company_name'],job1,jsons['job_post'],jsons['exp'],jsons['edu'],jsons['provinceid'],jsons['cityid'],jsons['three_cityid'],jsons['description'],int(jsons['minsalary'])*1000,int(jsons['maxsalary'])*1000,88,101)
                self.cursor.execute(sqlstr)
                jobid = self.cursor.lastrowid
                sqlstr = "insert into zpcompany_job_link set uid=%d,jobid=%d"%(uid,jobid)
                self.cursor.execute(sqlstr)
            except Exception as e:
                print(e)
        else:
            sqlstr = "update zpcompany_job set provinceid=%d,cityid=%d,three_cityid=%d where id=%d"%(jsons['provinceid'],jsons['cityid'],jsons['three_cityid'],jobData['id'])
            self.cursor.execute(sqlstr)
        self.connect.commit() 
        return item

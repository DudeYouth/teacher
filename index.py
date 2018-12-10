import pymysql

# 建立数据库连接  
connect = pymysql.connect(host='123.56.177.147',port=3308,user='root',passwd='&UJM8ik,',db='phpyun',use_unicode=True,charset='utf8',cursorclass = pymysql.cursors.DictCursor)   
# 获取游标 
cursor = connect.cursor()  
print("connecting mysql success!")
sqlstr = "select id,job_post from zpcompany_job"
cursor.execute(sqlstr)
data = cursor.fetchall()
for item in data:
    sqlstr = "select keyid from zpjob_class where id=%d"%(item['job_post'])
    cursor.execute(sqlstr)
    jobData = cursor.fetchone()
    sqlstr = "update zpcompany_job set job1=%d,job1_son=%d where id=%d"%(jobData['keyid'],item['job_post'],item['id'])
    cursor.execute(sqlstr)
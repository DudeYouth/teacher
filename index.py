import pymysql

# 建立数据库连接  
connect = pymysql.connect('localhost','root','','phpyun_test',use_unicode=True,charset='utf8',cursorclass = pymysql.cursors.DictCursor)  
# 获取游标 
cursor = connect.cursor()  
print("connecting mysql success!") 
timerSql = "select * from zpcomclass where name='测试'"
cursor.execute(timerSql)
timerData = cursor.fetchone()
print(timerData['id'])
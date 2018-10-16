import pymysql

# 建立数据库连接  
connect = pymysql.connect('localhost','root','','phpyun_test',use_unicode=True,charset='utf8',cursorclass = pymysql.cursors.DictCursor)  
# 获取游标 
cursor = connect.cursor()  
print("connecting mysql success!")
try:
    sqlstr = "select max(uid) uid from zpcompany"
    cursor.execute(sqlstr)
    userData = cursor.fetchone()
    uid = int(userData['uid'])+1 if userData else 1;
    print(uid)
    connect.commit()
except Exception:
    print("发生异常",Exception)
    connect.rollback()
print(cursor)
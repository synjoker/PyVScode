import pymysql
# 打开数据库
db = pymysql.connect("localhost", "syn", "asdfgh123456syn", "homework")
# 建立cursor对象
cursor = db.cursor()

cursor.execute("SELECT VERSION()")
data = cursor.fetchall()
print("database version: %s "% data)

# 方式一 转义方式具有可读性
name = 'syn'
lastname = 'ben'
age = '23'
sex = 'm'
income = 12200
sql = 'INSERT INTO EMPLOYEE(FIRST_NAME, \
        LAST_NAME, AGE, SEX, INCOME) \
        VALUES (%s, %s, %s, %s, %s) '
val =  (name, lastname, age, sex, income) 

try:
    cursor.execute(sql, val)
    db.commit()
except:
    db.rollback()

# # 方式二 直接插入 适合sql操作
# sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
#         LAST_NAME, AGE, SEX, INCOME)
#         VALUES('SYN', 'BEN', '22', 'M', 10000)
#         """

# try:
#     cursor.execute(sql, val)
#     db.commit()
# except:
#     db.rollback()

db.close()

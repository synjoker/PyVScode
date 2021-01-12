import pymysql
# 打开数据库
db = pymysql.connect("localhost", "syn", "asdfgh123456syn", "homework")
# 建立cursor对象
cursor = db.cursor()

# 使用 execute() 方法执行 SQL，如果表存在则删除
cursor.execute("DROP TABLE IF EXISTS test")

sql = """CREATE TABLE test(
   id INT PRIMARY KEY AUTO_INCREMENT,
   content LONGTEXT,
   image LONGBLOB )
    """

cursor.execute(sql)

f = open('camera0.jpg','rb')
data = f.read()
id = 1
content = "$GPGGA,061346.80,3208.0138462,N,11841.7793013,E,2,15,2.22,54.09,M,2.10,M,2,0806*66"
sql = 'INSERT INTO TEST(ID, CONTENT, IMAGE) \
        VALUES (%s, %s, %s)'
val =  (id, content, data) 

try:
    cursor.execute(sql, val)
    db.commit()
except:
    db.rollback()
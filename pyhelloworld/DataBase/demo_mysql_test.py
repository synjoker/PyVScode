import mysql.connector
 
mydb = mysql.connector.connect(
  host="localhost",       # 数据库主机地址
  user="syn",    # 数据库用户名
  passwd="asdfgh123456syn",   # 数据库密码
  database="homework" # 直接连接的数据库
)
 
print(mydb)

mycursor = mydb.cursor()

# sql = "INSERT INTO newtable (id, name, classname, newtablecol) VALUES (%s, %s, %s, %s)"
# val = (6, "s", "y", "n")
# mycursor.execute(sql, val)
  
# mydb.commit()    # 数据表内容有更新，必须使用到该语句
  
# print(mycursor.rowcount, "记录插入成功。")

# mycursor.execute("SHOW DATABASES")
# for x in mycursor:
#   print(x)

# mycursor.execute("SHOW TABLES")
# for x in mycursor:
#   print(x)

# mycursor.execute("CREATE TABLE sites (name VARCHAR(255), url VARCHAR(255))")

# sql = "INSERT INTO sites (name, url) VALUES (%s, %s)"
# val = ("RUNOOB", "https://www.runoob.com")
# mycursor.execute(sql, val)
 
# mydb.commit()    # 数据表内容有更新，必须使用到该语句
 
# print(mycursor.rowcount, "记录插入成功。")

# sql = "INSERT INTO sites (name, url) VALUES (%s, %s)"
# val = [
#   ('Google', 'https://www.google.com'),
#   ('Github', 'https://www.github.com'),
#   ('Taobao', 'https://www.taobao.com'),
#   ('stackoverflow', 'https://www.stackoverflow.com/')
# ]
 
# mycursor.executemany(sql, val) # 插入许多记录
 
# mydb.commit()    # 数据表内容有更新，必须使用到该语句
 
# print(mycursor.rowcount, "记录插入成功。")
# id INT AUTO_INCREMENT PRIMARY KEY 将id设置为主键
mycursor.execute("ALTER TABLE sites ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

sql = "INSERT INTO sites (name, url) VALUES (%s, %s)"
val = ("Zhihu", "https://www.zhihu.com")
mycursor.execute(sql, val)
 
mydb.commit()
 
print("1 条记录已插入, ID:", mycursor.lastrowid)
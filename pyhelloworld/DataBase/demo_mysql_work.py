import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="syn",
    passwd="asdfgh123456syn",
    database="homework"
)
mycursor = mydb.cursor()
# mycursor.execute("SELECT * FROM sites WHERE name LIKE '%zhi%'")
# # fetchall() 获取所有记录
# myresult = mycursor.fetchall()     
# for x in myresult:
#     print(x)

sql = "SELECT * FROM sites WHERE name = %s"
na = ("RUNOOB", )
 
mycursor.execute(sql, na)
 
myresult = mycursor.fetchall()
 
for x in myresult:
  print(x)


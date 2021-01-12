import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="syn",
    passwd="asdfgh123456syn",
    database="homework"
)
mycursor = mydb.cursor()
    
sql = "SELECT * FROM sites ORDER BY name"
    
mycursor.execute(sql)
    
myresult = mycursor.fetchall()
    
for x in myresult:
    print(x)
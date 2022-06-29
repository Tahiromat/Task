# -- Q5: Calculate converted ratio for each marketing channel for each year month
import pymysql
pymysql.install_as_MySQLdb()

mydb = pymysql.connect(
    host='localhost', 
    user='tahir', 
    password='Password123#@!', 
    database='taputestdb'
)

query = ""

mycursor = mydb.cursor()
mycursor.execute(query)

result = mycursor.fetchall()
mydb.commit()
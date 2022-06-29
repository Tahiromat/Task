# -- Q2: Plot number of unique users for date_served
import pymysql
pymysql.install_as_MySQLdb()

mydb = pymysql.connect(
    host='localhost', 
    user='tahir', 
    password='Password123#@!', 
    database='taputestdb'
)

query = "SELECT user_id FROM test_table WHERE user_id IS NOT NULL GROUP BY user_id having count(*) >= 1;"

mycursor = mydb.cursor()
mycursor.execute(query)

result = mycursor.fetchall()
mydb.commit()

print(len(result))


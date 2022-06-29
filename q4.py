# -- Q4: Plot number user for each marketing_channel for each month (convert date_served to year_month  - example: 2018-01)
import pandas as pd
import pymysql
pymysql.install_as_MySQLdb()

mydb = pymysql.connect(
    host='localhost', 
    user='tahir', 
    password='Password123#@!', 
    database='taputestdb'
)

# GROUP BY date_served marketing_channel types
queryy = '''
    SELECT 
    marketing_channel, COUNT(user_id)
    FROM
        test_table
    GROUP BY marketing_channel
    HAVING COUNT(marketing_channel) > 1;

'''

# GROUP BY date_served dates
query = '''
    SELECT 
    date_served, COUNT(user_id)
    FROM
        test_table
    GROUP BY date_served
    HAVING COUNT(date_served) > 1;
'''

mycursor = mydb.cursor()
mycursor.execute(query)

result = mycursor.fetchall()
mydb.commit()

print(f"GROUP BY date_served: \n\n{result}\n\n")



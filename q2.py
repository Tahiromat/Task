# -- Q2: Plot number of unique users for date_served
import pymysql
pymysql.install_as_MySQLdb()

mydb = pymysql.connect(
    host='localhost', 
    user='tahir', 
    password='Password123#@!', 
    database='taputestdb'
)

query = '''
    SELECT 
    COUNT(uniq_users.user_id)
    FROM
        (SELECT 
            user_id, date_served, COUNT(user_id) AS cnt_records
        FROM
            test_table
        GROUP BY user_id , date_served
        HAVING COUNT(user_id) = 1
        ORDER BY user_id DESC) AS uniq_users;
'''

mycursor = mydb.cursor()
mycursor.execute(query)

result = mycursor.fetchall()
mydb.commit()

uniq_users_count_for_date_served = result[0][0]
print(uniq_users_count_for_date_served)


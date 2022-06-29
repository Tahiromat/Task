# -- Q3: How many unique user are in this dataset and can a user have multiple data?
import pymysql
pymysql.install_as_MySQLdb()

mydb = pymysql.connect(
    host='localhost', 
    user='tahir', 
    password='Password123#@!', 
    database='taputestdb'
)


# UNIQ USERS
queryfor_non_uniq = "SELECT user_id FROM test_table WHERE user_id IS NOT NULL GROUP BY user_id having count(*) > 1;"

# NON-UNIQ USERS
queryfor_uniq = "SELECT user_id FROM test_table WHERE user_id IS NOT NULL GROUP BY user_id having count(*) = 1;"

# TOTAL USERS
queryfor_total_user = "SELECT COUNT(asdf.user_id) FROM (SELECT user_id FROM test_table WHERE user_id IS NOT NULL GROUP BY user_id HAVING COUNT(*) >= 1 ) AS asdf;"


mycursor = mydb.cursor()
mycursor.executemany(queryfor_non_uniq)

result = mycursor.fetchall()
mydb.commit()

print(result)

# 5029
# 2281

# print(len(result))
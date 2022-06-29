# -- Q1: print unique user for each for following categories: ['marketing_channel', 'variant', 'language_displayed', 'language_preferred', 'age_group', 'subscribing_channel']

import pymysql
pymysql.install_as_MySQLdb()


mydb = pymysql.connect(
    host='localhost', 
    user='tahir', 
    password='Password123#@!', 
    database='taputestdb'
)

columns = ['marketing_channel', 'variant', 'language_displayed', 'language_preferred', 'age_group', 'subscribing_channel']

# UNIQ USERS FOR 'marketing_channel'
query_marketing_channel = '''
    SELECT 
    user_id, marketing_channel, COUNT(*) AS cnt_records
    FROM
        test_table
    GROUP BY user_id , marketing_channel
    HAVING COUNT(*) = 1
    ORDER BY user_id DESC;
''' 

# UNIQ USERS FOR 'variant'
query_variant = '''
    SELECT 
    user_id, variant, COUNT(*) AS cnt_records
    FROM
        test_table
    GROUP BY user_id , variant
    HAVING COUNT(*) = 1
    ORDER BY user_id DESC;
'''


mycursor = mydb.cursor()
mycursor.execute(query_variant)

result = mycursor.fetchall()
mydb.commit()

for row in result:
    print(f"{row[0]}\n")

print(f"[INFO]----- LEN OF UNIQ USERS FOR 'variant':  {len(result)}")


# -- Q1: print unique user for each for following categories: ['marketing_channel', 'variant', 'language_displayed', 'language_preferred', 'age_group', 'subscribing_channel']
import time
import pymysql
pymysql.install_as_MySQLdb()

mydb = pymysql.connect(
    host='localhost', 
    user='tahir', 
    password='', 
    database='taputestdb'
)

columns = ['marketing_channel', 'variant', 'language_displayed', 'language_preferred', 'age_group', 'subscribing_channel']

for col in columns:
    # UNIQ USERS FOR SPECİFİED COLUMNS
    query = f'''
        SELECT 
        user_id, {col}, COUNT(*) AS cnt_records
        FROM
            test_table
        GROUP BY user_id , {col}
        HAVING COUNT(*) = 1
        ORDER BY user_id DESC;
    ''' 

    mycursor = mydb.cursor()
    mycursor.execute(query)

    result = mycursor.fetchall()
    mydb.commit()
    
    print(f"\n\n\n\[INFO]---------- PRINTING OF UNIQ USERS FOR {col}")
    time.sleep(3)

    for row in result:
        print(f"{row}\n")

    


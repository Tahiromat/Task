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
queryfor_uniq = '''
    SELECT 
    COUNT(uniq_users.user_id)
    FROM
        (SELECT 
            user_id
        FROM
            test_table
        WHERE
            user_id IS NOT NULL
        GROUP BY user_id
        HAVING COUNT(user_id) = 1) AS uniq_users;
'''

# NON-UNIQ USERS
queryfor_non_uniq = '''
    SELECT 
    COUNT(non_uniq_users.user_id)
    FROM
        (SELECT 
            user_id
        FROM
            test_table
        WHERE
            user_id IS NOT NULL
        GROUP BY user_id
        HAVING COUNT(user_id) > 1) AS non_uniq_users;
'''

queries = [queryfor_uniq, queryfor_non_uniq]

for query in queries:
    mycursor = mydb.cursor()
    mycursor.execute(query)
    result = mycursor.fetchall()
    mydb.commit()

    if query.index == 0:
        print(f"\n\n\n\[INFO]---------- PRINTING NUMBER OF UNIQUE USERS FOR DATASET : {result[0][0]}")
    else:
        print(f"\n[INFO]---------- PRINTING NUMBER OF NON-UNIQUE (HAVE MUTIPLE DATA) USERS FOR DATASET : {result[0][0]} \n\n\n")

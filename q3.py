# -- Q3: How many unique user are in this dataset and can a user have multiple data?
import pymysql
pymysql.install_as_MySQLdb()

mydb = pymysql.connect(
    host='localhost', 
    user='tahir', 
    password='', 
    database='taputestdb'
)

operators = ['=', '>']

for opt in operators:
    query = f'''
        SELECT 
        COUNT(users.user_id)
        FROM
            (SELECT 
                user_id
            FROM
                test_table
            WHERE
                user_id IS NOT NULL
            GROUP BY user_id
            HAVING COUNT(user_id) {opt} 1) AS users;
    '''
    mycursor = mydb.cursor()
    mycursor.execute(query)

    result = mycursor.fetchall()
    mydb.commit()

    if opt =='=':
        print(f"\n\n\n\[INFO]---------- NUMBER OF UNIQUE USERS FOR DATASET : {result[0][0]}")
    elif opt == '>':
        print(f"\n[INFO]---------- NUMBER OF NON-UNIQUE (HAVE MUTIPLE DATA) USERS FOR DATASET : {result[0][0]} \n\n\n")
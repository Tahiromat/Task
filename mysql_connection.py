import pymysql
pymysql.install_as_MySQLdb()
import csv

# DATABASE CONNECTION 
mydb = pymysql.connect(
    host='localhost', 
    user='tahir', 
    password='', 
    database='taputestdb'
)


# READ CSV FILE ROW BY ROW
with open('data.csv') as csv_file:
    csvfile = csv.reader(csv_file, delimiter=',')
    all_values = []
    for row in csvfile:
        value = (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11])
        all_values.append(value)


# CREATE TABLE IN MYSQL
create_table_in_mysql = '''
    CREATE TABLE `test_table` (
        user_id VARCHAR(25),
        date_served VARCHAR(25),
        marketing_channel VARCHAR(25),
        variant VARCHAR(25),
        converted VARCHAR(25),
        language_displayed VARCHAR(25),
        language_preferred VARCHAR(25),
        age_group VARCHAR(25),
        date_subscribed VARCHAR(25),
        date_canceled VARCHAR(25),
        subscribing_channel VARCHAR(25),
        is_retained VARCHAR(25)
    );
'''

# INSERT CSV FILE TO MYSQL TABLE
query = '''
    INSERT INTO `test_table`(
        `user_id`, 
        `date_served`, 
        `marketing_channel`, 
        `variant`, 
        `converted`, 
        `language_displayed`, 
        `language_preferred`, 
        `age_group`, 
        `date_subscribed`, 
        `date_canceled`, 
        `subscribing_channel`, 
        `is_retained`
    ) 
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
'''



# EXECUTE THE QUERY
mycursor = mydb.cursor()
mycursor.execute(create_table_in_mysql)
mycursor.executemany(query, all_values)
mydb.commit()

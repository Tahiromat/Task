# -- Q2: Plot number of unique users for date_served


# #################### WITH SQL #####################################################################################
import pymysql
pymysql.install_as_MySQLdb()
import matplotlib.pyplot as plt
import pandas as pd

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

print(f"\n\n\\[INFO]---------- NUMBER OF UNIQUE USERS FOR 'date_served' : {result[0][0]}\n\n")


# #################### WITH Pandas #####################################################################################
# Read data
data = pd.read_csv('data.csv')

df = data[['user_id','date_served']]
df.date_served = pd.to_datetime(df.date_served)
total_users = len(data)
df = df.drop_duplicates(subset=['user_id'])
unique_users = len(df)

non_unique_users = total_users - unique_users


data_for_plot = {'Total':total_users, 'Unique':unique_users, 'Non-Unique':non_unique_users}

x_labels = list(data_for_plot.keys())
y_values = list(data_for_plot.values())

plt.bar(x_labels, y_values)
 
plt.xlabel("USERS")
plt.ylabel("USERS COUNTS")
plt.title("EVALUATION OF UNIQUE OR NON-UNIQUE USER")
plt.show()
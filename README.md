### To Tapu.com

### Description
* mysql_connection.py file features:
  - SQL queries are included.
  - Connection working environment to MySQL Workbench.
  - Create new table into Database.
  - Read data.csv file row by row  from work-environment.
  - Insert data into table created in Database.

* q1.py file features:
  - SQL queries are included.
  - Prints unique 'user_id's for specified columns.
  

* q2.py file features:
  - SQL queries are included.
  - Print number of unique users for date_served.
  - Finds total, unique, non-unique user counts for specified data.
  - Visualizes the results.

* q3.py file features:
  - SQL queries are included.
  - Print number of unique and non-unique users for dataset.

* q4.py file features:
  - Print the number of user for each marketing_channel type, based on the month.
  - Visualizes the results.

* q5.py file features:
  - Print the number of user for each marketing_channel type, based on the month and print them grouped by 'converted' column.

* q6.py file features:
  - Change categorical data to numeric data
  - Change age-range with randomly between given range.
  - Visualize the 0, 1 distribution.
  - Print the model accuracy, predictions and preedictions probabilities.
  - Visualize ROC-CURVE for model prediction.



#### For Using
- Download the code
- Create venv : $ virtualenv venv
- Activate venv : $ source venv/bin/activate
- Download libraries needed from requirements.txt file :  $ pip3 install -r requirements.txt
  NOT: To use mysql_connection.py, q1.py, q2.py and q3.py files you need to make your own database connection.
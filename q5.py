# -- Q5: Calculate converted ratio for each marketing channel for each year month
from sklearn.preprocessing import LabelEncoder
import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")

# Read data
data = pd.read_csv('data.csv')

# Rename the columns
data.rename(columns={"date_served":"Date", "converted":'Converted', "marketing_channel":"Marketing_Channels"}, inplace=True)

# Fill nan cells
data.Date = data.Date.fillna('1/26/18')
data.Converted = data.Converted.fillna('True')
data.Marketing_Channels = data.Marketing_Channels.fillna('unspecified')


df = data[['user_id', 'Date', 'Marketing_Channels', 'Converted']]

df['Date'] = pd.to_datetime(df.Date)

# Change time frequency from daily to monthly
df['Monthly_Date'] = df['Date'].dt.to_period('M')

grouped_df = df.groupby(['Converted', 'Marketing_Channels', 'Monthly_Date']).count()
grouped_df.rename(columns={"user_id":"User_Count"}, inplace=True)
grouped_df.drop("Date", axis=1, inplace=True)


print(f"\n\n[INFO] ------- 'convert' numbers of each 'marketing_channel' channels in month-based evaluation \n\n{grouped_df} \n\n")






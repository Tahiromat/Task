# -- Q4: Plot number user for each marketing_channel for each month (convert date_served to year_month  - example: 2018-01)
import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")

# Read data
data = pd.read_csv('data.csv')

# Change column name
data.rename(columns={"date_served":"Date"}, inplace=True)

# Fill nan marketing channel cells with unspecified
data.marketing_channel = data.marketing_channel.fillna('unspecified')

# Fill nan Date cells with given date -- This is randomly choosed 
data.Date = data.Date.fillna('1/26/18')

# Create new df
df = data[['user_id', 'Date', 'marketing_channel']]

# Rename the Columns
df.rename(columns={"marketing_channel":"Marketing_Channels"}, inplace=True)

# Change dtype from strinf to datetime
df['Date'] = pd.to_datetime(df.Date)

# Change time frequency from daily to monthly
df['Monthly_Date'] = df['Date'].dt.to_period('M')

# Groupby monthly data
grouped_df = df.groupby(['Marketing_Channels', 'Monthly_Date']).count()

# Rename the Columns
grouped_df.rename(columns={"user_id":"User_Count"}, inplace=True)
grouped_df.drop("Date", axis=1, inplace=True)

print(grouped_df)

# Plot the result
grouped_df.plot()
plt.show()

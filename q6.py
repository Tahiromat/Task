# -- Q6: Build a basic binary classification model for classify converted column. you can drop some feature

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

import warnings
warnings.filterwarnings("ignore")

data = pd.read_csv('data.csv')

le = LabelEncoder()
encoded = le.fit_transform(data['converted'])
data['encoded'] = encoded

df = data[['age_group', 'encoded']]
df['age_group'] = df['age_group'].astype(str).str.replace('0-18 years','18', regex=True)
df['age_group'] = df['age_group'].astype(str).str.replace('19-24 years','24', regex=True)
df['age_group'] = df['age_group'].astype(str).str.replace('24-30 years','30', regex=True)
df['age_group'] = df['age_group'].astype(str).str.replace('30-36 years','36', regex=True)
df['age_group'] = df['age_group'].astype(str).str.replace('36-45 years','45', regex=True)
df['age_group'] = df['age_group'].astype(str).str.replace('45-55 years','55', regex=True)
df['age_group'] = df['age_group'].astype(str).str.replace('+','-60', regex=True)
df['age_group'] = df['age_group'].astype(str).str.replace('55-60 years','60', regex=True)

print(df)

plt.scatter(df.age_group, df.encoded, marker='+', color='red')
plt.show()


X_train, X_test, y_train, y_test = train_test_split(df[['age_group']], df.encoded, test_size=0.8)

model = LogisticRegression()

model.fit(X_train, y_train)
predictions = model.predict(X_test[20:50])
print(predictions)

score = model.score(X_test, y_test)
print(score)

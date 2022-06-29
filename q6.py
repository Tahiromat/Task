# -- Q6: Build a basic binary classification model for classify converted column. you can drop some feature
import random
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib as mpl
from pathlib import Path
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score, roc_curve, confusion_matrix


filepath = Path('/home/tahir/Documents/DataScience/TEST/dataforclassifyconvertedfeature.csv')  
filepath.parent.mkdir(parents=True, exist_ok=True)  

mpl.style.use(['https://gist.githubusercontent.com/BrendanMartin/01e71bb9550774e2ccff3af7574c0020/raw/6fa9681c7d0232d34c9271de9be150e584e606fe/lds_default.mplstyle'])
mpl.rcParams.update({"figure.figsize": (8,6), "axes.titlepad": 22.0})
import warnings
warnings.filterwarnings("ignore")


# DATA PREPROCESSING AND CREATE NEW DF FOR BINARY CLASSIFICATION

data = pd.read_csv('data.csv')

lab_encoder = LabelEncoder()
encoded = lab_encoder.fit_transform(data['converted'])
data['encoded_cenverted'] = encoded

df = data[['age_group', 'encoded_cenverted']]
df['age_group'] = df['age_group'].astype(str).str.replace('0-18 years', str(random.randint(0, 18)), regex=True)
df['age_group'] = df['age_group'].astype(str).str.replace('19-24 years', str(random.randint(19, 24)), regex=True)
df['age_group'] = df['age_group'].astype(str).str.replace('24-30 years', str(random.randint(24, 30)), regex=True)
df['age_group'] = df['age_group'].astype(str).str.replace('30-36 years', str(random.randint(30, 36)), regex=True)
df['age_group'] = df['age_group'].astype(str).str.replace('36-45 years', str(random.randint(36, 45)), regex=True)
df['age_group'] = df['age_group'].astype(str).str.replace('45-55 years', str(random.randint(45, 55)), regex=True)
df['age_group'] = df['age_group'].astype(str).str.replace('+','-90', regex=True)
df['age_group'] = df['age_group'].astype(str).str.replace('55-90 years', str(random.randint(55, 90)), regex=True)
df['encoded_cenverted'] = df['encoded_cenverted'].astype(str).str.replace('2', '1', regex=True)

''' OLD MODEL

# prepared_df = pd.read_csv(filepath)

plt.scatter(prepared_df.age_group, prepared_df.encoded_cenverted, marker='+', color='red')
plt.show()


# X_train, X_test, y_train, y_test = train_test_split(df[['age_group']], df.encoded, test_size=0.8)

# # print(X_train)


# model = LogisticRegression()

# model.fit(X_train, y_train)
# predictions = model.predict(X_test)
# print(predictions)

# score = model.score(X_test, y_test)
# print(score)
'''

# #########################  NEW MODEL #####################################


(unique, counts) = np.unique(df['encoded_cenverted'], return_counts=True)

print('Unique values of the target variable', unique)
print('Counts of the target variable :', counts)

df['encoded_cenverted'] = df['encoded_cenverted'].map({'1': 1, '0': 0}).astype(int)

sns.barplot(x=unique, y=counts)
plt.title('encoded_cenverted variable counts in dataset')
plt.legend()
plt.show()

X_train, X_test, y_train, y_test = train_test_split(df[['age_group']], df.encoded_cenverted, test_size=0.8)


model = LogisticRegression()
model.fit(X_train, y_train)

'''print(model)

predictions = model.predict(X_test)

print(predictions)

cm = confusion_matrix(y_test, predictions)

TN, FP, FN, TP = confusion_matrix(y_test, predictions).ravel()

print('True Positive(TP)  = ', TP)
print('False Positive(FP) = ', FP)
print('True Negative(TN)  = ', TN)
print('False Negative(FN) = ', FN)

accuracy =  (TP+TN) /(TP+FP+TN+FN)*100

print('Accuracy of the binary classification = {:0.3f}'.format(accuracy))'''

y_pred = model.predict(X_test)


print(f'Accuracy of the binary classification = {(model.score(X_test, y_test))*100}')



model_roc_auc = roc_auc_score(y_test, model.predict(X_test))
fpr, tpr, thresholds = roc_curve(y_test, model.predict_proba(X_test)[:,1])

plt.figure()
plt.plot(fpr, tpr, label='Logistic Regression (area = %0.2f)' % model_roc_auc)
plt.plot([0, 1], [0, 1], 'r--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.xlabel('Operating Characteristic')
plt.legend(loc='lower right')
plt.savefig('Log_ROC')
plt.show()
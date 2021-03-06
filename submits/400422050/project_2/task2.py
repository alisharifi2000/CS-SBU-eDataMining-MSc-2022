# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Yn56uj9R1rLeUTTImSZ58LWE14PLq6W6
"""

import pandas as pd
from sqlite3 import OperationalError
import seaborn as sns
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.compose import ColumnTransformer
from sklearn.tree import DecisionTreeClassifier
import numpy as np
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.feature_selection import SelectFromModel
#Scratch*
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
import math
from sklearn.metrics import mean_absolute_error

from google.colab import drive
drive.mount('/gdrive', force_remount=True)

! ls /gdrive/MyDrive/csv

root = '/gdrive/MyDrive/csv/'
Data=pd.read_csv('immo_data.csv')
print(Data)

Data.columns[(data.isna().sum())/len(data)>0.50]

for cols in Data.columns :
  if Data[cols].dtype == 'bool' or Data[cols].dtype == 'object':
   Data[cols].fillna(Data[cols].value_counts().head(1).index[0],inplace=True)

Data.fillna(Data._get_numeric_Data().mean(),inplace = True)

Data.isna().sum()

New=Data.iloc[:, :11]
x=New.drop(columns=["regio1", "telekomTvOffer", "telekomHybridUploadSpeed", "newlyConst", "balcony", "picturecount", "pricetrend"])
print(x)
y=Data.iloc[:, 10]
print(y)

x2= pd.get_dummies(x,columns=['heatingType'] ,prefix='type')
print(df)

x_train, x_test, y_train, y_test=train_test_split(x2, y, test_size=0.2, random_state=1)

model = LinearRegression()
model.fit(X_train, y_train)

y_train.mean()

model.score(X_train, y_train)

model.score(X_test, y_test)

print(model.intercept_)
print(model.coef_)

y_pred = model.predict(X_test)

pred_df = X_test.copy()
pred_df["y_true"] = y_test
pred_df["y_pred"] = y_pred
pred_df.head()

mean_absolute_error(y_test, y_pred)
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 19:08:24 2024

@author: Engineer José López
"""


import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import train_test_split
# %matplotlib inline

data_filename= 'Advertising.csv'
df=pd.read_csv(data_filename)

# df_new=df.iloc[0:7,[0,3]] ##excelente, Felicidades
# print(df_new)

traindata=df.iloc[5:13]
# print(traindata.iloc[:,0])

x_true=df.TV.iloc[5:13]
y_true=df.Sales.iloc[5:13]
idx=np.argsort(traindata.iloc[:,0]).values
print(idx)
# print(x)
# print(x.iloc[[3,2,1,4,5]])


x_true=x_true.iloc[idx].values
# print(x)
y_true=y_true.iloc[idx].values
# print(y)

def find_nearest(array,value):
    
    idx=pd.Series(np.abs(array-value)).idxmin()
    return idx, array[idx]

x=np.linspace(np.min(x_true),np.max(x_true))
# print(x)
y=np.zeros(len(x))

for i, xi in enumerate(x):
    
    y[i]=y_true[find_nearest(x_true,xi)[0]]
    
plt.plot(x,y, '-.')
plt.plot(x,y,'kx')
plt.xlabel("Gasto en Publicidad por TV [$]")
plt.ylabel("Retorno en Ventas [$]")
plt.title("Gasto en Publicidad por TV vs Retorno en Ventas")

# =============================================================================
# 
# =============================================================================



x=df['TV']
y=df['Sales']

x_train, x_test, y_train, y_test = train_test_split()

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
%matplotlib inline

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
x=df[['TV']]
y=df['Sales']

x_train, x_test, y_train, y_test=train_test_split(x,y,test_size=0.4,train_size=0.6,random_state=42)
##why random.state=42
k_value_min=1
k_value_max=70
k_list=np.linspace(k_value_min,k_value_max,70)
fig, ax=plt.subplots(figsize=(10,6))

j=0

for k_value in k_list:
    
    model=KNeighborsRegressor(n_neighbors=int(k_value))
    model.fit(x_train,y_train)
    y_pred=model.predict(x_test)
    colors=['grey','r','b']
    
    if k_value in [1,10,70]:
        xvals=np.linspace(x.min(),x.max(),100)
        ypreds=model.predict(xvals)
        ax.plot(xvals,ypreds,'-',label=f'k={int(k_value)}',linewidth=j+2,color=colors[j])
        j+=1
        
ax.legend(loc='lower right',fontsize=20)
ax.plot(x_train, y_train, 'x',label='train',color='k')
ax.set_xlabel('TV budget in $1000',fontsize=20)
ax.set_ylabel('Sales in $1000',fontsize=20)
plt.tight_layout()

model=KNeighborsRegressor(n_neighbors=int(1))
print(model)
test=model.predict([[200]])
print(test)

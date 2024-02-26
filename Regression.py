# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 20:45:46 2024

@author: engineer José López
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from helper import fit_and_plot_linear
from helper import fit_and_plot_multi

df=pd.read_csv('Advertising.csv')

x_true=df[['TV']]
z_true=df[['Radio']]
u_true=df[['Newspaper']]
y_true=df['Sales']
predictor=df[['TV','Radio','Newspaper']]

r2_train_x, r2_test_x=fit_and_plot_linear(x_true)
r2_train_z, r2_test_z=fit_and_plot_linear(z_true)
r2_train_u, r2_test_u=fit_and_plot_linear(u_true)
r2_train_m, r2_test_m=fit_and_plot_multi()

r2_results=pd.DataFrame([r2_train_x, r2_train_z,r2_train_u,r2_train_m],[r2_test_x, r2_test_z,r2_test_u,r2_test_m])


Predictors=['TV', 'Radio', 'Newspaper', 'Multi']

r2_results=[[r2_train_x, r2_train_z, r2_train_u, r2_train_m], [r2_test_x, r2_test_z, r2_test_u, r2_test_m]]
df_results = pd.DataFrame(columns=['Predictor', 'R2 Train', 'R2 Test'])
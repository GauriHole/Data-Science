# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 08:24:13 2024

@author: Lenovo
"""

# sales = pd.read_excel("sales.xlsx")
# sales.head()
# sales.columns

import seaborn as sns
import pandas as pd
import matplotlib as plt
cars = pd.read_csv("Cars.csv")
cars.head()
cars.columns
sns.relplot(x='HP',y='MPG',data=cars)
sns.relplot(x='HP',y='MPG',data=cars,kind='line')
sns.catplot(x='HP',y='MPG',data=cars,kind='box')
sns.distplot(cars.HP)

cars.describe()
#------------------------------------------
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
plt.bar(height=cars.HP,x=np.arange(1,82,1))
sns.distplot(cars.HP)
plt.boxplot(cars.HP)
sns.distplot(cars.MPG)
plt.boxplot(cars.MPG)
sns.distplot(cars.VOL)
plt.boxplot(cars.VOL)
sns.distplot(cars.SP)
plt.boxplot(cars.SP)
sns.distplot(cars.WT)
plt.boxplot(cars.WT)

import seaborn as sns
sns.jointplot(x=cars['HP'],y=cars["MPG"])
plt.figure(1,figsize=(16,10))
sns.countplot(cars['HP'])

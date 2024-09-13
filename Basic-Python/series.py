# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 08:50:13 2024

@author: Lenovo
"""
import pandas as pd
songs = pd.Series([145,142,38,13],name='counts') 
songs.index
songs3 = pd.Series([145,142,38,13],name='counts',
index=['Paul','John','George','Ringo'])
songs3.index
songs3
#---------------------------------------------

import pandas as pd
f1=pd.read_csv('C:/1-maths/age.csv')
f1
#----------Check Your Pandas Working Directory-----

df = pd.read_excel('C:/1-maths/Bahaman.xlsx')
#---------Reading CSV File----------------------

import numpy as np
numpy_ser = np.array([145,142,38,13])
songs3[1]
numpy_ser[1]
songs3.mean()
numpy_ser.mean()
#---------Finding Mean of Series----------------
#Note: Lists , Series and Numpy Arrays are Nearby Same.

#CRUD Operations on Series - (Create,Read,Update,Delete)
george=pd.Series([10,7,1,22],
     # Here,index are same which cause confusion but ('1970')
     # helpful when you want the duplicate record for some operation. 
index=['1968','1969','1970','1970'],name='George_Songs')
#Column name should not have the space instead of you can use '_'
print(george)
george

#Reading Series
george['1968']
george['1970']

for item in george:
    print(item)

#Updating Series
george['1969'] = 68
george['1969']
george

#Deleting Series
import pandas as pd
george=pd.Series([10,7,1,22],
     # Here,index are same which cause confusion but ('1970')
     # helpful when you want the duplicate record for some operation. 
index=['1968','1969','1970','1970'],name='George_Songs')
#Column name should not have the space instead of you can use '_'
print(george)
george
del george['1968']
george
                            #03-04-2024
#Convert Types
# dtype is a property because it won't consists ()
'''1. string use.astype(str)
   2. numeric use pd.to_numeric 
   3. integer use.astype(int)'''
import pandas as pd   
songs_66 = pd.Series([3.0,None,11.0,9.0],
    index=['George','Ringo','John','Paul'],
    name='Counts')
#songs_66=songs_66.astype(int)
songs_66.dtypes
# this below is showing error : ValueError: Unable to parse string "nan" at position 1
pd.to_numeric(songs_66.apply(str))
#this statement will not showing the error
pd.to_numeric(songs_66.astype(str),errors='coerce')
songs_66.dtypes

#.fillna will replace that value with the assign value

#-------------------- FillNA --------------------------
songs_66 = songs_66.fillna(-1)
songs_66 = songs_66.astype(int)
print(songs_66)
songs_66.dtypes

#-------------------- DropNA ----------------------

import pandas as pd   
songs_66 = pd.Series([3.0,None,11.0,9.0],
    index=['George','Ringo','John','Paul'],
    name='Counts')
songs_66 = songs_66.dropna()
print(songs_66)

#Append, Combining and Joining two Series
#--------------- ConCat/Append --------------------
songs_69 = pd.Series([7,12,16,21],
                     index=['Ram','Shyam','Ghanshyam','Radhasham'],
                     name='Counts')
pd.concat([songs_66,songs_69])
songs = songs_66.append(songs_69)
print(songs)

#--------------- MatPlotLib ---------------------
import matplotlib.pyplot as plt
fig = plt.figure()
songs_66.plot()
plt.legend()
#------------------------------------
fig =plt.figure()
songs_69.plot(kind='bar')
songs_66.plot(kind='bar',color='r')
plt.legend()

#---------------- NumPY ----------------------
import numpy as np
data = pd.Series(np.random.random(500),
                 name='500_random')
fig = plt.figure()
ax = fig.add_subplot(111)
data.hist()
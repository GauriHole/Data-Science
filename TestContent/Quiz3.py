# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 09:12:33 2024

@author: Lenovo
"""
#1
def ListCom():
    n=5
    l1=[1,2,3,4,5]
    l2=[3,10,9,6,12]
    for i in range(0,n):
        for j in range(i,n):
            if(l1[i]==l2[j]):
                return "True"
            else:
                return "False"
            j=j+1
        i=i+1
            
ListCom()

#2 
list1 = [1,2,3,4,5,6]
list2 =[]
for i in range(0,7):
    list2 = list1[i]+6
    print(list2)
list2

#3
str = "Sanjivani"
#strRev = 
strRev = str.slice[-1::]

#4
dict1 = {1:"Gauri",2:"Ishwari",3:"Aditi",4:"Vidya"}
for i in dict1.keys():
    print(dict1[i])
'''
Gauri
Ishwari
Aditi
Vidya '''
    
#5
dict1 = {1:2000,2:3000,3:1000,4:1500}
dict2 = {}
for i in dict1.keys():
    if(dict1[i] > 2000):
        dict2[i] = dict1[i]
print(dict2)
'''
print(dict2)
{2: 3000} '''

#6
open('data.txt',mode='r')
''' 
Out[64]: <_io.TextIOWrapper name='data.txt' 
mode='r' encoding='cp1252'>
'''
#7
import numpy as np
import array
data = np.array([11,22,33,44,55])
zeroTh = data[0]
fourTh = data[4]
print("Zero th Index Data : ",zeroTh)
print("Four th Index Data: ",fourTh)
'''
print("Zero th Index Data : ",zeroTh)
Zero th Index Data :  11

print("Four th Index Data: ",fourTh)
Four th Index Data:  55 '''

#8
'''Not able to solve pandas code'''

#9
import pandas as pd
df = pd.DataFrame('name':['Anna','Dinu','Ramu','Ganu','Emily','Mahesh','Jayesh','venkat','Ajay','Dhanesh'],
                 'score': [12.5,9,16.5,np.nan,9,20,14.5,np.nan,8,19],
                 'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
                 'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes'])
print(df)
#labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])
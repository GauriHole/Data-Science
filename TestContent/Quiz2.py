# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 08:20:39 2024

@author: Lenovo
"""
#Example 1)
def list(list1,list2):
    for i in range(0,5):
        for j in range(0,5):
            if(list1[i]==list2[j]):
                print("True")
list1 = [1,2,3,4,5]
list2 = [2,7,8,6,9]
list(list1,list2)

#Example2)
list1 = [1,2,3,4,5]
list_new = list1
list_new.append(6)
print(list_new)

#Example3)
string_O = "Hellow Sanjivani"
string_Rev = reversed(string_O)
print(string_Rev)

#Example4)
dict ={'Roll':68,'Name':"Gauri",'Class':"TYCM"}
for i in dict:
    print(i," : ",dict[i])

#Example5)
dict1 = {'EID':1200,'Salary':2000}
for i in dict1:
    temp=dict1[i]
    if (temp >= 2000):
        dict2 = temp
print("New Dict: ",dict2)

#Example6)
file = open("data.txt",mode='r')
print(file)

#Example7)
import numpy 
data = numpy.array([11, 22, 33, 44, 55])
print("0th index : ",data[0])
print("4th index : ",data[4])    

#Example8)
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Original list of integers:")
print(nums)

print("\nEven numbers :")
print("\nOdd numbers :")

#Example9)
import pandas as pd 
import numpy as np
dict_new ={
    'name': ['Anna','Dinu','Ramu','Ganu','Emily','Mahesh','Jayesh','venkat','Ajay','Dhanesh'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8,9],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes'],
    }
row_labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
data = pd.DataFrame(dict_new)
print(data)

#Example10)
import numpy
data = numpy.array([11, 22, 33, 44, 55])
print("Data From 1 to 4",data[1:4])
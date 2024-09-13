# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 09:05:12 2024

@author: Lenovo
"""

#1
'''Check if email address valid or not in Python
e.g. Input: my.ownsite@ourearth.org
Output: Valid Email'''
import re
def match(text):
    pattern = '[a-z]+[.][a-z]+[@][a-z]+[.][a-z]+$'
    if re.search(pattern, text):
        return 'Valid Mail'
    else:
        return 'InValid Mail'
print(match("my.ownsite@ourearth.org"))
print(match("ankitrai326.com"))

#2
'''Write a Python program to find the median of below three values.
Values: (25,55,65)'''

arr = [25,55,65]
print("The original list : " + str(arr)) 
 
mid = len(arr) // 2
result = (arr[mid] + arr[~mid]) / 2
print("Median : " + str(result))

#3
'''Write a program to create a decorator function to measure the 
execution time of a function.'''
def my_deco(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper
@my_deco
def hi():
    print("Welcome...")
#-----------------INCOMPLETE--------------------

#4
'''Write a python program that opens a file and handles a 
FileNotFoundError exception if the file does not exist.'''
try:
    file1 = open("sample.txt",'r')
except:
    print("file not found")

#5
'''Write a python program to find the intersection of two given arrays 
using Lambda.
Original arrays:
[1, 2, 3, 5, 7, 8, 9, 10]
[1, 2, 4, 8, 9] Intersection of the said arrays: [1, 2, 8, 9]'''

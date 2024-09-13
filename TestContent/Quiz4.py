# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 10:05:47 2024

@author: Lenovo
"""
#1 ----
''' . Write a python program to print all even numbers from a given list of
numbers in the same order and stop printing any after 237 in the sequence.
Sample numbers list:
numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 
           978, 328, 615, 953, 345, 399, 162, 758, 219, 918, 237, 
           412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 
           67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 
           843, 831, 445, 742, 717, 958,743, 527] '''
numbers = [ 386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 
328, 615, 953, 345,399, 162, 758, 219, 918, 237, 412,566,826,248,866, 
950, 626, 949, 687, 217,815, 67, 104, 58, 512, 24, 892, 894, 767,
553, 81, 379, 843, 831, 445, 742, 717, 958,743, 527]

list2 =[x for x in list]
        
#2 ----
''' Write a python program to find a list of integers with exactly two 
occurrences of nineteen and at least three occurrences of five. Return True 
otherwise False.
e.g. Input: [19, 19, 15, 5, 3, 5, 5, 2]
Output: True
'''
list = [19, 19, 15, 5, 3, 5, 5, 2]
list[0]
list2 =[x for x in list]
list2
for i in range(0,list):
    print(list[i])
    
#3 ----
''' Write a python program to find numbers that are greater than 10 and have 
odd first and last digits.
e.g: Input: [1, 3, 79, 10, 4, 1, 39, 62]
Output: [79, 39]
'''
import numpy as np
list = [1,3,79,10,4,1,39,62]
new_arr = np.array(list)
for i in range(0,10):
    if new_arr[i]%2 ==0:
        print(new_arr[i])
#if list[i]:

#4 ----
''' Write a python program to find the largest negative and smallest positive 
numbers (or 0 if none).
e.g. Input:[-12,-6,300,-40,2,2,3,57,-50,-22,12,40,9,11,18]
Output: [-6, 2] '''
list1 = [-12,-6,300,-40,2,2,3,57,-50,-22,12,40,9,11,18]
list2=[x for x in list]
if list2 % 2 == 0:
    print(list2.x)
    
#5 ----
''' Write a Python program that matches a string that has an a followed by 
zero or more b's '''
import re
def match(text):
    pattern = '^a(b*)$'
    if re.search(pattern, text):
        return 'Matched'
    else:
        return 'Not match'
print(match("abb"))

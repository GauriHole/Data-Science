# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 08:43:04 2024

@author: Lenovo
"""

def foo(a, b=4, c=6):
    print(a, b, c)
foo(20, c=12)
#---------------------------------------

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
print(fruits[2])
#----------------------------------------

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
fruits[-1] = "Melons"
fruits.append("Lemons")
print(fruits)
#---------------------------------------

starting_dictionary = {
"a": 9,
"b": 8,
	}
final_dictionary = {
"a": 9,
"b": 8,
"c": 7,
	}
final_dictionary = starting_dictionary
print(final_dictionary)

#---------------------------------------
order = {
	    "starter": {1: "Salad", 2: "Soup"},
	    "main": {1: ["Burger", "Fries"], 2: ["Steak"]},
	    "dessert": {1: ["Ice Cream"], 2: []},
	}
print(order)
#---------------------------------------

def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2
print(add(2, multiply(5, divide(8, 4))))
#---------------------------------------

def outer_function(a, b):
    def inner_function(c, d):
        return c + d
    return inner_function(a, b)
result = outer_function(5, 10)
print(result)
#--------------------------------------

student = {
  "name": "Emma",
  "class": 9,
  "marks": 75
}
print(student[marks])
#-------------False-----------------
student = {
  "name": "Emma",
  "class": 9,
  "marks": 75
}
mark= student["marks"]
print(mark)
#----------Corrected---------------

student = { 
  "name": "Emma", 
  "class": 9, 
  "marks": 75 
}
#remove.student["marks"]
#----------False------------------
student.pop("marks")
print(student)
#----------Corrected--------------

dict1={
      "roll" : 68,
      "name" : "Gauri"
       }
dict2={}
dict2=dict1
print(dict2)
#----------------------------------

lst = [int(x*x) for x in range(3,12,4)]
print(lst[-2])
#------------Not Solve --------------

lst= [ int(x/3) for x in range(5,35) if x % 2 == 0 and x%5 == 0]
print(lst[-1]+5)
#------------Not Solve --------------

Func1=lambda x: ((x + 3) * 5 / 2)
Func1(3)
#------------------------------------




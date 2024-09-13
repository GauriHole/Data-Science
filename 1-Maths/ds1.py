# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 08:16:56 2024

@author: Lenovo
"""
''' Exception Handling '''
try:
    numerator =50
    denom = int(input("enter the denominator : "))
    print(numerator/denom)
    print("Division is successful ")
except ZeroDivisionError:
    print("Denominator should not be 0 ")
except ValueError:
    print("denominator should be integer")
print("---------------------------------")

try:
    numerator =50
    denom = int(input("enter the denominator:"))
    print(numerator/denom)
    print("Division is successful")
except ZeroDivisionError:
    print("Denominator should not be 0")
except:
    print("Some Error occured")
print("---------------------------------")

#try...catch....else
try:
    num=50
    deno=int(input("Enter denominator:"))
    quotient =(num/deno)
    print("Division perform successfully...")
except ZeroDivisionError:
    print("Number not divisible by 0")
except ValueError:
    print("Denominator Number should be Interger")
except:
    print("Some Error is occured")
else:
    print("Result of Division : ",quotient)
print("--------------------------------")

#try...catch....else....finally
try:
    num=10
    deno=int(input("Enter Denominator:"))
    quotient = (num/deno)
    print("Division is perform Successfully",quotient)
except ZeroDivisionError:
    print("Denominator should not be 0")
except ValueError:
    print("Number Should be integer")
except:
    print("Some Error Occured")
finally:
    print("Code Perform Successfully With 0:Errors")
print("-------------------------------------")

                            #29-03-2024
#Classes and Object
class Human:
    def __init__(self,n,o):
        self.name=n
        self.occupation=o
    def do_work(self):
        if self.occupation == "tennis player":
            print(self.name,"playes tennis")
        elif self.occupation=="actor":
            print(self.name,"shoots films")
    def speaks(self):
        print(self.name,"says hello , How are you?")

tom = Human("tom_cruise","actor")
tom.do_work()
tom.speaks()

maria = Human("maria_sharapuva","tennis player")
maria.do_work()
maria.speaks()
print("------------------------------------")

# Inheritance
class Vehicle:
    def general_usage(self):
        print("General Use: Transportation")
class Car(Vehicle):
    def __init__(self):
        print("I am Car")
        self.wheels = 4
        self.has_roof =True
    def specific_usage(self):
        self.general_usage()
        print("Specific Use: Commute to work, vacation with family")
class MotorCycle(Vehicle):
    def __init__(self):
        print("I am Motor Cycle")
        self.wheels = 2
        self.has_roof = False
    def specific_usage(self):
        self.general_usage()
        print("Specific Use : Racing And Bike Riding")
car = Car()
motor = MotorCycle()
car.specific_usage()
motor.specific_usage()
print(issubclass(Car, MotorCycle)) #issubclass(derived,base) False
print(issubclass(Car, Vehicle)) # True
print("-----------------------------------")

# Multiple Inheritance
class Father():
    def skills(self):
        print("I like Programming , and Gardening ")
class Mother():
    def skills(self):
        print("I like Cooking and Cleaning")
class Gauri(Father,Mother):
    def skills(self):
        Father.skills(self)
        Mother.skills(self)
        print("I like Web Designing and Watching Movies ")
        
gauri = Gauri()
gauri.skills()
print("----------------------------------")




'''
try:
    set1 = [1, 2, 3]
    result = 20 + set1
    print(result)
except TypeError:
    print("Error : You cann't Perform Interger and Set Addition ")

str = "vidya"
dict = {1:'Jagtap'}
try:
    print(str+dict)
except TypeError as t:
    print("Error : Check the Format ")
    print(t)
'''

'''
def divide_numbers(a,b):
    if b == 0:
        raise ZeroDivisionError("Error: Cannot Divide by Zero")
    elif b == None:
        raise NameError("Error: Names Not Allowed")
    elif s == True:
        raise SyntaxError("Error : Syntax is not Correct")
    elif t == True:
        raise TypeError("Error: Type is Not Proper")
    else:
        return a/b

try:
    result = divide_numbers(10,0)
    print(result)
except IndentationError as i:
    print(i)
except SyntaxError as s:
    print(s)
except NameError as e:
    print(e)
except ZeroDivisionError as z:
    print(z)
except TypeError as t:
    print(t)
'''

try:
    user_input = input("Enter a integer : ")
    print(user_input)
    user_input = "Gaytri"

    result = input(user_input)
    print(result)
except ValueError:
    print("Error: Invalid value. You did not enter a valid integer. ")

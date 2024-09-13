print("-------------   Lambda Function   ------------")
'''
addition = lambda a, b: a * b
result = addition(2, 3)
print("Addition Result : ",result)

multiply = lambda a, b: a * b
result = multiply(2, 3)
print("Multiply Result : ",result)

division = lambda a, b : a / b
result = division(5 , 10)
print("Division Result : ",result)

def perform_operation(operation,x,y):
    return operation(x,y)
result = perform_operation(division,2,10)
print("Passing Value to Another Function : ",result)

def square(x):
    return x*x

def compose(f,g):
    return lambda x,y: f(g(x,y))
result = compose(square,addition)(2,3)
print("Compose Result : ",result)
'''

def add(a,b):
    return a+b;

def sub(a,b):
    return  a-b;

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

operations = {
    '+' : add,
    '-' : sub,
    '*' : mul,
    '/' : div
}

operat = input("Enter What would you like to Perform (+,-,*,/) : ")
num1 = float(input("Enter First Number : "))
num2 = float(input("Enter Second Number : "))

if operat in operations:
    result = operations[operat](num1, num2)
    print("Result : ",result)
else:
    print("Invalid Operator ")
'''
def my_deco(func):
    def wrapper():
        print("Something happen Before function called ")
        func()
        print("Something happen after function called ")
    return wrapper
print("Something happend in main Function ")

@my_deco
def say_Hi():
    print("How are You ? ")

say_Hi()
'''
def log_function_call(func):
    def wrapper(*args,**kwargs):
        print(f"Calling function :{func.__name__}")
        print(f"Argument (4,5) : {args}")
        print(f"Arguments : {args},{kwargs}")
        result = func(*args, **kwargs)
        print(f"Function Result : {result} ")
        return result
    return wrapper
@log_function_call
def add_numbers(a,b):
    print("I am in add numbers ")
    return (a+b)

result = add_numbers(5,10)
print(f"Result : {result}")
print("------------ Type 1 ------------")
def greet():
    def say_hello():
        print("Hello Gauri , What Happen ? ")
    return say_hello
my_func = greet()
my_func()

print("------------ Type 2 ------------")
def greet():
    print("Hello Gauri ")
def execute_fun(func):
    func()
execute_fun(greet)

print("------------ Type 3 ------------")
def greet():
    print("Hello Gauri ")
func = greet()

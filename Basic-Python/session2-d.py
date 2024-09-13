'''
for j in range(4,0, -1):
    print('*' * j)
'''

''' next Part '''
global_var = 10

def my_func():
    global global_var
    print("Before Increment : ",global_var)
    global_var += 5
my_func()
print("After Increment : ",global_var)
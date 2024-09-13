""" This Numpy Library is Used for Print the array and also used shape(used for dimenssions) function"""
from numpy import array
l = [1.0,2.0,3.0]
a = array(l)
print(a)
print(a.shape)

""" This Numpy Library is Used to Get the Garbege Value """
from numpy import empty
a = empty([3,3])
print(a)

""" This Numpy Library is used for printing 0's With Row=3 and Columns= 6 """
from numpy import zeros
a = zeros([3,6])
print(a)

""" This Numpy library is used to print 1's array """
from numpy import ones
a = ones([5])
print(a)

""" This Numpy Library is used for representation of vertical array alignment"""
from numpy import array
from numpy import vstack

a1= array([1,2,3])
print(a1)

a2= array([4,5,6])
print(a2)

a3= vstack((a1,a2)) 
print(a3)
print(a3.shape) # Shape Display the alignment of array with dimenssions

""" This Numpy library is used to print array in Horizontal Alignment """
from numpy import array
from numpy import hstack

a1= array([1,2,3])
print(a1)

a2= array([4,5,6])
print(a2)

a3= hstack((a1,a2)) 
print(a3)
print(a3.shape)

""" This Numpy library is used to find Type of variable"""
from numpy import array
data = [11,22,33,44,55]
print(type(data))
print(data)
data = array(data)
print(type(data))

""" This Numpy library is used to compile block of input using select-> scroll arrow toward bottom-> and [I]"""
from numpy import array
data =[[11,22],
       [33,44],
       [55,66]]
data = array(data)
print(data)
print(type(data))

""" This Numpy library is used to print the data by using it's index """
from numpy import array
data = array([11,22,33,44,55])
print(data[0])
print(data[3])

""" This Code generated an error message that array is out of bound """
from numpy import array
data = array([11,22,33])
print(data[4])

""" This code is for Reverse indexing """
from numpy import array
data = array([11,22,33,44,55])
print(data[-4])
print(data[-2])

""" This code is for display the two dimenssional array """
from numpy import array
data = array([[11,22],
             [23,24],
            [32,44]])# 0  1 
print(data[2,0]) # 0 (11,22)
                 # 1 (23,24)
                 # 2 (32,44)

""" This code is for display all columns in first row """
from numpy import array
data = array([[11,22],
             [23,24],
             [32,44]])
print(data[0,]) 

""" This code is for sliceing of an array """
from numpy import array
data = array([11,22,33,44,55])
print(data[2:3])

""" This is code for negative/reverse sliceing of array """
from numpy import array
data = array([11,22,33,44,55])
print(data[-1:])
print(data[-2:])
print(data[-3:])
print(data[-4:])

""" This is used for dividing array into two parts """
from numpy import array
data = array([
    [11,22,33],
    [44,55,66],
    [77,88,99]
    ])
x,y = data[ : , : -1], data[ : , -1]
    # here,0:2,0:-1         0:0,-1 only 
x
y

""" This perform the addition of number b with all array elements """
from numpy import array
a = array([1,2,3])
b = 2
print(a,b)
c = a+b
print(c)

""" This perform the addition of two dimenssional array """
from numpy import array
a = array([1 , 2 , 3 ])
b = array([2, 3, 4 ])
print(a,b)
c = a + b
print(c)

""" This code perform addition and substraction of an two different data types of array element """
from numpy import array
a = array([11,2,3])
b = array([1.0,2.3,3.1])
print(a,b)
print(a+b)
print(a-b)

""" This is used for optimization our model is underbit or overbit that we will know by this norm """
from numpy import array
from numpy.linalg import norm

a = array([1,2,3])
print(a)
l1 = norm(a,1)
print(l1)

a = array([1,2,3])
print(a)
l2 = norm(a)
print(l2)

""" This is used while we only select either upper side element or lower side elements """
# triangular matrices
from numpy import array
from numpy import tril
from numpy import triu
M = array([
    [1, 2, 3],
    [1, 2, 3],
    [1, 2, 3]
    ])
print(M)
lower = tril(M)
upper = triu(M)
print(lower)
print(upper)

""" This is for Diagonal elements"""
from numpy import array
from numpy import diag
M = array([
    [1, 2, 3],
    [1, 2, 3],
    [1, 2, 3]
    ])
print(M)

d = diag(M)
print(d)

D = diag(d)
print(D)

""" This is for """
from numpy import identity
I = identity(3)
print(I)

"""  """
from numpy import array
from numpy.linalg import inv

Q = array([
    [1,0],
    [0,-1]])
print(Q)

V=  inv(Q)
print(Q.T)
print(V)

I = Q.dot(Q.T)
print(I) 

""" This is for finding transport of matrix  """
from numpy import array

a = array([
    [1,2],
    [3,4],
    [5,6]])

b = array([
    [1,2,3],
    [4,5,6]])

print(a)
print(b)

c = a.T
print(c)
c = b.T
print(c)

""" This code is for  """
from numpy import array
from numpy.linalg import inv

A = array([
    [1.0,2.0],
    [3.0,4.0]
    ])

B = inv(A)
print(B)

I = A.dot(B)
print(I) # identity matrics

""" This code is for Sparse Matrix """
from numpy import array
from scipy.sparse import csr_matrix

A = array([
    [1,0,0,1,0,0],
    [0,0,2,0,0,1],
    [0,0,0,2,0,0]])
print(A)

S = csr_matrix(A);
print(S)

B = S.todense()
print(B)

""" This code iis for version details & configuration """
import numpy as np
print(np.__version__)
print(np.show_config())

""" This is for """
import numpy as np
print(np.info(np.add))

""" This is code for """
import  numpy as np
x = np.array([1,2,3,4])

print("Original Array :",x)

print("Check Your Image doesn't contain any zeros ")
print(np.all(x))
x = np.array([0,1,2,3])
print("Original array :",x)
print("Test if none of the elements of the said array is zeroo : ")
print(np.all(x))

""" This is code for checking whether your array contain non-zero or not  """
import numpy as np

x = np.array([1,0,0,0])
print("Orginal Array : ",x)
print("Test whether any of the elemts of a given array is non-zero ")
print(np.any(x))
x=np.array([0,0,0,0])
print("Original array :")
print(x)
print("Test whether any of yhe elements of a given array is ")
print(np.any(x))

""" This is code for checking whether the array contain infinite numbers if yes the true another false """
import numpy as np
a = np.array([1,0,np.nan,np.inf])
print("Original array : ",a)
print("Test a given array elements-wise for finiteness : ")
print(np.isfinite(a))

""" This is code for checking whether the array contain NAN values """
import numpy as np
a = np.array([1,0,np.nan,np.inf])
print("Original Array : ",a)
print("Test element-wise for NaN : ",np.isnan(a))

""" This code is for Check Complex Number & Scalar Type of Number """
import numpy as np

a = np.array([1+1j, 1+0j, 4.5, 3, 2, 2j])
print("Original Number : ",a)
print("Complex Number : ",np.iscomplex(a))
print("Check Number is Real Number : ",np.isreal(a))
print("Check Number is Scalar Type : ",np.isscalar(3.1))
print(np.isscalar([3.1]))

""" This is code for Dot , Outer and cross Product of two given matrices """
import numpy as np
p = [[1,0],[0,1]]
q = [[1,2],[3,4]]
print("Original Matrix : ")
print(p,q)
result=np.dot(p,q)
print("Dot product : ",result)
result = np.outer(p,q)
print("Outer product of the said two vectors : ")
print(result)
result = np.cross(p,q)
print("Cross product of the said two vectors : ")
print(result)
result = np.cross(q,p)
print("Cross product of the said two vectors : ")
print(result)
# write defination of cross and dot product ...

""" This is code for draw a line with suitable label """
import matplotlib.pyplot as plt
X = range(1,50)
Y = [value * 3 for value in X]
print("Values of X : ")
print(*range(1,50))
 
''' 
This is quivqlent to -
i in range(1,50 ):
    print(i,end='')
    
 '''
print("Values of Y (thrice of X ) : ")
print(Y)
# Plot lines and markers to the above
plt.plot(X,Y)
# set the x-axis label of the current axis.
plt.xlabel('x-axis')
# set the y-axis label of current axis.
plt.ylabel('y-axis')
#set a title
plt.title('Draw a line . ')
# Display the figure.
plt.show()

# Date : 29-09-2023
''' Code is implementated Using the library of mathploatlib  '''
import matplotlib.pyplot as plt
x = [1,2,3]
y = [2,4,1]

plt.plot(x,y)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Sample graph !')
plt.show()

''' Code for plot more than two or more lines using legends '''
import matplotlib.pyplot as plt
x1 =[10,20,30]
y1 =[20,40,10]


x2= [10,20,30]
y2= [40,10,30]

plt.plot(x1,y1,label='line1')
plt.plot(x2,y2,label='line2')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Two or More Lines on same plot with suitable legends')
plt.legend()
plt.show()

''' Code for give color to the legends and also change the style of the legends with dashed & dotted '''
import matplotlib.pyplot as plt
x1 =[10,20,30]
y1 =[20,40,10]

x2= [10,20,30]
y2= [40,10,30]
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Two or More Lines on same plot with suitable legends')
plt.plot(x1,y1, color='pink', linewidth=3, label='line1-width-3', linestyle='dotted')
plt.plot(x2,y2, color='blue', linewidth=5, label='line2-width-5', linestyle='dashed')
plt.legend()
plt.show()

''' Code Set x & y axis limits'''
import matplotlib.pyplot as plt
x = [1,4,5,6,7]
y =[2,6,3,6,3]

plt.plot(x,y,marker='o', markerfacecolor='blue',markersize=12, color='red', linestyle='dashdot', linewidth=3 )
plt.ylim(1,8)
plt.xlim(1,8)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Graph')
plt.legend()
plt.show()

''' Code For the Printing Vertical Bar Chart for Popular Language in the World '''
import matplotlib.pyplot as plt
x = ['Java','Python','PHP','JavaScript','C#','C++']
popularity =  [22.2,17.6,8.8,8,7.7,6.7]
x_pos = [i for i, _ in enumerate(x)]
plt.bar(x_pos,popularity,color='Green')
plt.xlabel("Language")
plt.ylabel("Popularity")
plt.title("Popularity of Programming Language \n"+"Worldwide, Over the Popularity")
plt.xticks(x_pos,x)
plt.minorticks_on()
plt.grid(which='major',linestyle='-',linewidth='0.5',color='red')
plt.show()

''' This code is used for Printing Horizontal Bar Chart'''
import matplotlib.pyplot as plt
x = ['Java','Python','PHP','JavaScript','C#','C++']
popularity =  [22.2,17.6,8.8,8,7.7,6.7]
x_pos = [i for i, _ in enumerate(x)]
plt.barh(x_pos,popularity,color='Blue')
plt.xlabel("Language")
plt.ylabel("Popularity")
plt.title("Popularity of Programming Language \n"+"Worldwide, Over the Popularity")
plt.xticks(x_pos,x)
plt.minorticks_on()
plt.grid(which='major',linestyle='-',linewidth='0.5',color='red')
plt.show()

''' This is code for give default color to our bar chart  '''
import matplotlib.pyplot as plt
x = ['Java','Python','PHP','JavaScript','C#','C++']
popularity =  [22.2,17.6,8.8,8,7.7,6.7]
x_pos = [i for i, _ in enumerate(x)]
plt.bar(x_pos,popularity,color=(0.4,0.6,0.8,1.0))
plt.xlabel("Language")
plt.ylabel("Popularity")
plt.title("Popularity of Programming Language \n"+"Worldwide, Over the Popularity")
plt.xticks(x_pos,x)
plt.minorticks_on()
plt.grid(which='major',linestyle='-',linewidth='0.5',color='red')
plt.show()

''' This code is used for given different color to all individual bars'''
import matplotlib.pyplot as plt
x = ['Java','Python','PHP','JavaScript','C#','C++']
popularity =  [22.2,17.6,8.8,8,7.7,6.7]
x_pos = [i for i, _ in enumerate(x)]
plt.bar(x_pos,popularity,color=['orange','blue','green','red','pink','black'])
plt.xlabel("Language")
plt.ylabel("Popularity")
plt.title("Popularity of Programming Language \n"+"Worldwide, Over the Popularity")
plt.xticks(x_pos,x)
plt.minorticks_on()
plt.grid(which='major',linestyle='-',linewidth='0.5',color='red')
plt.show()

#Date : 30-09-23

''' This code is for used of fourier transformation '''
# finding integration
from numpy import exp
f=lambda x:exp(-x**2)

'''
    def add(a,b,c)
    sum=a+b+c
    return sum
print(add(4,5,6))
add=lambda a,b,c:a+b+c
add(4,5,6)
'''
# Date : 06-10-2023
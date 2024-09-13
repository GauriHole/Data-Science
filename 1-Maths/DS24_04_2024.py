# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 08:40:43 2024

@author: Lenovo
"""
#Transpose Matrix
from numpy import array
A = array([
    [1,2],
    [3,4],
    [5,6]])
print(A)
C = A.T
print(C)

#Inverse Matrix
from numpy import array
from numpy.linalg import inv
A = array([
    [1.0,2.0],
    [3.0,4.0]])
print(A)
B = inv(A)
print(B)

#multipy A and B
I = A.dot(B)
print(I)

#Sparse Matrix
from numpy import array
from scipy.sparse import csr_matrix
A = array([
    [1,0,0,1,0,0],
    [0,0,2,0,0,1],
    [0,0,0,2,0,0]])
print(A)
#convert to sparse matrix (CSR method)
S = csr_matrix(A)
print(S)
#reconstruct dense matrix in (previous form)
B = S.todense()
print(B)

#---------------------MatPlotLib------------------------
#write a code to draw line with labels
import matplotlib.pyplot as plt
X = range(1,50)
Y = [value *3 for value in X]
print("Values of X : ")
print(*range(1,50))
'''
This is equivalent to i in range (1,50):
    print(i,end='')
'''
print("Values of Y (thrice of X: ",Y) 
#Plot lines and markers to the Axes
plt.plot(X,Y)
#Set the X axis label of the current axis
plt.xlabel('x-axis')
plt.ylabel('y-axis')
#set a title
plt.title("Sample Line")
plt.show()

#Sample graph
import matplotlib.pyplot as plt
x = [1,2,3]
y = [2,4,1]
#Plot lines and markers to the Axes
plt.plot(x,y)
#Set the x-axis label of the current axis
plt.xlabel('X-axis : ')
plt.ylabel('Y-axis : ')
plt.title('Sample Graph')
plt.show()

#Write a program to plot two or more lines 
#Two or more lines on same plot with suitable legends
import matplotlib.pyplot as plt
#line 1 points
x1 = [10,20,30]
y1 = [20,40,10]

#line 2 points
x2 = [10,20,30]
y2 = [40,10,30]

#ploting the line 1 points
plt.plot(x1,y1,label='line 1')
#ploting the line 2 points
plt.plot(x2,y2,label="line2")
#Select X and Y axis labels 
plt.xlabel('x-axis')
plt.ylabel('Y-axis')
plt.title("Two line Graph")
plt.legend()
plt.show()

#Write program to plot two or more lines
#with different widts and colors
import matplotlib.pyplot as plt
#line 1 points
x1 = [10,20,30]
y1 = [20,40,10]

#line 2 points
x2 = [10,20,30]
y2 = [40,10,30]
#Select X and Y axis labels 
plt.xlabel('x-axis')
plt.ylabel('Y-axis')
plt.title("Different Width and Color Graph ")
plt.plot(x1,y1,color='blue',linewidth=3,label="line1")
plt.plot(x2,y2,color='red',linewidth=5,label="line2")
plt.legend()
plt.show()

#Write program to plot two or more lines with different style
import matplotlib.pyplot as plt
#line 1 points
x1 = [10,20,30]
y1 = [20,40,10]

#line 2 points
x2 = [10,20,30]
y2 = [40,10,30]
#Select X and Y axis labels 
plt.xlabel('x-axis')
plt.ylabel('Y-axis')
plt.title("Different Width and Color Graph ")
plt.plot(x1,y1,color='blue',linewidth=3,label="dash_line1",linestyle='dotted')
plt.plot(x2,y2,color='red',linewidth=5,label="dash_line2")
plt.legend()
plt.show()

#-------------------------------------------------------------------------
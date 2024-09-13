# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 08:45:17 2024

@author: Lenovo
"""
#NumPy - Numerical Python
#Used in image processing and AI
import numpy as np
np.__version__
#Arrays In Numpy Create ndArray
arr = np.array([10,20,30])
print(arr)

#Create Multi Dimenssional 2-D Array
arr = np.array([[10,20,30],[11,22,33]])
print(arr)

#Create 3-D Array
arr = np.array([10,20,30,40],ndmin=3)
print(arr)

#Change the datatype to Complex
arr = np.array([10,20,30],dtype=complex)
print(arr)

#Get Dimenssion of Array
arr = np.array([[10,20,30],[7,8,9],[1,2,3]])
print(arr.ndim)
print(arr)

#Finding the size of each item in the array
arr = np.array([10,20,30,40])
print("Each  item contains in bytes : ",arr.itemsize)

#Get shape and size of array
arr =  np.array([[10,20,30,40],[60,70,20,40]])
print("Size : ",arr.size)
print("Shape : ",arr.shape)

#Creating array from list
arr = np.array([10,20,30])
print("array : ",arr)

#Creating array from list with type float
arr = np.array([[10,20,30],[20,30,40]],dtype='float')
print("Array from list : ",arr)

#Creating Sequence of integer
#From 0 to 20 with step 3
arr = np.arange(0,20,3)
print("A Sequencial array with steps of 3 :\n",arr)

arr = np.arange(11)
print(arr)
#If you want  the 2nd location item from array
print(arr[2])
print(arr[-2]) #Negative Indexing

#Indexing for multi dimenssional array
arr = np.array([[10,20,30,40,50],[20,30,40,50,10]])
print(arr)
print(arr.shape) #(2, 5)
print(arr[1,1]) #30
print(arr[0,4]) #50
print(arr[1,-1])#10

#Access array elements using slicing
arr =np.array([0,1,2,3,4,5,6,7,8,9])
x = arr[1:8:2]
print(x)

#start last but one(-2) upto 3 not
x = arr[-2:3:-1]
print(x)

#--------- Slicing in Multi-D --------------------
multi_arr = np.array([[10,20,10,40],
                      [40,50,70,90],
                      [60,10,70,80],
                      [30,90,40,30]])
multi_arr

#Slicing 
multi_arr[1,2] # To access the value of 1 row and 2 column
multi_arr[1,:] # To get the values at row 1 and all columns 
multi_arr[:,1] # Access the value at all rows and 1 column
#---------------------------------------------------------
                                        # 19 -04 -2024
#----------------- MOST IMPORTANT --------------------
#x=3 Scalar
#x=[10,20,30] Vector
#x=[[10,20],[20,30]] Metrics
#x=[[[]]] Tensor

x = multi_arr[:3,::2]
print(x)

#Integer array indexing
arr = np.arange(35).reshape(5,7)
print(arr)

#Boolean Array Indexing
arr = np.arange(12).reshape(3,4)
print(arr)

rows =np.array([False,True,True])#omiteed 0th index
rows
wanted_rows = arr[rows, : ] #selective rows all columns
print(wanted_rows)


#numpy.asarray()
list = [20,40,60,80]
array = np.asarray(list)
print("Array : ",array)
print(type(array))

#Shape of ndarray
array =  np.array([[1,2,3],[4,5,6]])
array
print(array.shape)

#Resize the array
array = np.array([[10,20,30],[40,50,60]])
array.shape=(3,2)
print(array)

#Reshape array
array = np.array([[1,2,3],[4,5,6]])
new_array = array.reshape(3,2)
print(new_array)

#Apply arithmetic operations on numpy array
arr1 = np.arange(16).reshape(4,4)
arr2 = np.array([1,3,2,4])

#Addition
add_arr = np.add(arr1,arr2)
print(f"Adding two arrays : \n{add_arr}")

#Substract
sub_arr = np.subtract(arr1,arr2)
print(f"Adding two arrays : \n{sub_arr}")

#Multiplication
mul_arr = np.multiply(arr1,arr2)
print(f"Multipy two arrays : \n{mul_arr}")

#Division
div_arr = np.divide(arr1,arr2)
print(f"Dividing two arrays :  \n {div_arr}")

#Reciprocal
arr1 = np.array([50,10.3,5,1,200])
rep_arr1 = np.reciprocal(arr1)
print(f"After applying reciprocal function to array: \n {rep_arr1}")

#numpy.power()
arr1 = np.array([3,10,5])
pow_arr1 = np.power(arr1,3)
print(f"After applying power functionto array : \n{pow_arr1}")

#power() using 2 arrays
arr1 = np.array([3,10,5])
arr2 = np.array([3,2,1])
print("My second array:\n",arr2)
pow_arr2 = np.power(arr1,arr2)
print(f"After applying power functionto array : \n{pow_arr2}")

#MOD operation
arr1 = np.array([7,20,13])
arr2 = np.array([3,5,2])
arr1
arr1.dtype
#mod()
mod_arr = np.mod(arr1,arr2)
print(f"After applying mod function to array :\n {mod_arr}")

#Create Empty array
from numpy import empty
a = empty([3,3])
print(a)

#Create Zero Array
from numpy import zeros
a = zeros([3,5])
print(a)

#Create one array
from numpy import ones
a = ones([5])
print(a)

#Create first Vstack (vertical array) 
from numpy import array
from numpy import vstack
a1 = array([1,2,3])
a1
a2 = array([4,5,6])
a2

#Vertical Stack
a3 = vstack((a1,a2))
print(a3)
print(a3.shape)

#Create first Hstack(horizontal array)
from numpy import array
from numpy import hstack
a1 = array([1,2,3])
a1
a2 = array([4,5,6])
a2
a3 = hstack((a1,a2))
print(a3)
print(a3.shape)
#-------------------------------------------------------
                                        
                                       # 23 -04 -2024
from numpy import array
data = array([10,20,30,40])
print(data[5])
#Array index out of bound

#index row of 2-D Array
from numpy import array
data = array([
    [11,22],
    [33,44],
    [55,66]])
print(data[0,])#Select 0th row and all columns

#slice a one-dimensional array
from numpy import array
data= array([11,22,33,44,55])
print(data[-2:])#last second row and all columns
data

#split input and output data
from numpy import array
data = array([
    [11,22,33],
    [44,55,66],
    [77,88,99]])
X,y = data[:,:-1],data[:,-1] #all row only last column
X        #[all:row ,column0:-1]
y

#Broadcat scalar to 1-D array
from numpy import array
#dedine array
a = array([1,2,3])
print(a)
#define scalar
b =2 
print(b) 
#Broadcast
c = a+b
print(c)

#----------------L1 Norm----------------
from numpy import array
from numpy.linalg import norm
a = array([1,2,3])
print(a)
#calculate norm 1
l1 = norm(a,1)
print(l1)

#----------------L2 Norm----------------
from numpy import array
from numpy.linalg import norm
a = array([1,2,3])
print(a)
#calculate norm 2
l2 = norm(a)
print(l2)

#----------------Triangular Matrix--------
from numpy import array,tril,triu
#defines square matrix
M = array([
 [1,2,3],
 [1,2,3],
 [1,2,3]
    ]) 
print(M)

#Lower triangular matrix
lower = tril(M)
print("-------Lower triangular------   ",lower)
#Upper triangular matrix
upper = triu(M)
print("-------Upper triangular------   ",upper)

#------------------Diagonal Matrix----------
from numpy import array,diag
#define square matrix
M = array([
    [1,2,3],
    [1,2,3],
    [1,2,3]])
print(M)

#extract diagonal vector
d = diag(M)
print(d)

#create diagonal matrix from vector
D = diag(d)
print(D)

#----------------Identity Matrix-------------
from numpy import identity
I = identity(3)
print(I)

#----------------Orthogonal Matrix-----------
'''
The matrix is said to be an orthogonal matrix it 
the product of a matrix and it's tranpose fives an 
identity value
'''
from numpy import array
from numpy.linalg import inv
#define orthogonal matrix

Q = array([
    [1,0],
    [0,-1]])
print(Q)

#inverse equivalence
V = inv(Q)
print(Q.T)
print(V)
#identity equivalence
I = Q.dot(Q.T)
print(I)

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
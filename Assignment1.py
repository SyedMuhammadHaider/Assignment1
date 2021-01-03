####### Assignment#1 #######
############################
###########################################################
# 1. Import the numpy package under the name np
import numpy as np
# 1. Create a null vector of size 10
a = np.zeros(10)
# 1. Create a vector with values ranging from 10 to 49
b = np.arange(10,49)
# 1. Find the shape of previous array in question 3
print(b.shape)
# 1. Print the type of the previous array in question 3
print(b.dtype)
# 1. Print the numpy version and the configuration
print(np.__version__)
print(np.show_config())
# 1. Print the dimension of the array in question 3
print(b.ndim)
# 1. Create a boolean array with all the True values
arr_bool = np.ones(10, dtype=bool)
# 1. Create a two dimensional array
c = np.array([[1,2,3],[4,5,6]])
# 1. Create a three dimensional array
a_3d=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
##########################################################
# 1. Reverse a vector (first element becomes last)
arr=np.arange(10,55)
rev_arr=arr[::-1]
# 1. Create a null vector of size 10 but the fifth value which is 1
e=np.zeros(10)
e[4]=1
# 1. Create a 3x3 identity matrix
identity_matrix=np.identity(3)
# 1. arr = np.array([1, 2, 3, 4, 5])
##Convert the data type of the given array from int to float
arr = np.array([1, 2, 3, 4, 5])
converted=arr.astype(np.float)
# 1. arr1 = np.array([[1., 2., 3.],
##
##            [4., 5., 6.]])  
##
##arr2 = np.array([[0., 4., 1.],
##
##           [7., 2., 12.]])
##Multiply arr1 with arr2
arr1 = np.array([[1., 2., 3.],[4., 5., 6.]])
arr2 = np.array([[0., 4., 1.],[7., 2., 12.]])
print(np.multiply(arr1,arr2))
# 1. arr1 = np.array([[1., 2., 3.],[4., 5., 6.]]) 
##arr2 = np.array([[0., 4., 1.],[7., 2., 12.]])
##Make an array by comparing both the arrays provided above
arr1 = np.array([[1., 2., 3.],[4., 5., 6.]])
arr2 = np.array([[0., 4., 1.],[7., 2., 12.]])
# 1. Extract all odd numbers from arr with values(0-9)
arr = np.arange(10)
print(arr[arr%2==1])
# 1. Replace all odd numbers to -1 from previous array
arr[arr%2==1]=-1
print(arr)
# 1. arr = np.arange(10)
##Replace the values of indexes 5,6,7 and 8 to 11
arr = np.arange(10)
a[5:8]=np.arange(8,11)
# 1. Create a 2d array with 1 on the border and 0 inside
x=np.ones((5,5))
x[1:-1,1:-1]=0
print(x)
#############################################################
# 1. arr2d = np.array([[1, 2, 3],
##            [4, 5, 6], 
##            [7, 8, 9]])
##Replace the value 5 to 12
arr2d = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
arr2d[1,1]=12
# 1. arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
##Convert all the values of 1st array to 64
arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
arr3d[0,0,:]=64
# 1. Make a 2-Dimensional array with values 0-9 and slice out the first 1st 1-D array from it
arrr2d=np.arange(10).reshape(2,5)
print(arrr2d[0,:])
# 1. Make a 2-Dimensional array with values 0-9 and slice out the 2nd value from 2nd 1-D array from it
print(arrr2d[1,1])
# 1. Make a 2-Dimensional array with values 0-9 and slice out the third column but only the first two rows
arrr2d[0:2,2]
# 1. Create a 10x10 array with random values and find the minimum and maximum values
y = np.random.random((10,10))
ymin=y.min()
ymax=y.max()
print(ymax, ymin)
# 1. a = np.array([1,2,3,2,3,4,3,4,5,6]) b = np.array([7,2,10,2,7,4,9,4,9,8])
##Find the common items between a and b
a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])
print(np.intersect1d(a,b))
##############################################################
# 1. Create a 2D array of shape 5x3 to contain decimal numbers between 1 and 15.
ar2=np.arange(1,16).reshape(5,3)
# 1.Create an array of shape (2, 2, 4) with decimal numbers between 1 to 16.
ar4=np.arange(1,17).reshape(2,2,4)
# 1. Swap axes of the array you created in Question 32
print(np.swapaxes(ar2,1,0))
# 1. Create an array of size 10, and find the square root of every element in the array, if the values less than 0.5, replace them with 0
R=np.arange(10)
R=np.sqrt(R)
np.where(R<0.5,0,R)
# 1. x = np.array([[1., 2., 3.], [4., 5., 6.]]) y = np.array([[6., 23.], [-1, 7], [8, 9]])
##Find the dot product of the above two matrix
x = np.array([[1., 2., 3.],[4., 5., 6.]])
y = np.array([[6., 23.],[-1, 7],[8, 9]])
print(np.dot(x,y))
# 1. Generate a matrix of 20 random values and find its cumulative sum
c1=np.random.random(20)
print(np.sum(c1))
##############################################################

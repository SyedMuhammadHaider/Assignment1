##########################
#######Assignment 2#######
##########################
##########################
import numpy as np
# QUESTION #1
arr=np.arange(10)
arr_2d=np.reshape(arr,(2,5))
print(arr_2d)
# QUESTION #2
x = np.array([3,5,7])
y = np.array([5,7,9])
print(np.vstack((x,y)))
# QUESTION #3
a = np.array([[1,2,3],[4,5,6]])
b = np.array([[9,8,0],[5,4,1]])
print(np.hstack((a,b)))
# QUESTION #4
ar = np.arange(15).reshape(5,3)
onedar = ar.flatten()
# QUESTION #5
ar3d = np.arange(8).reshape(2,2,2)
print(ar3d.flatten())
# QUESTION #6
one_d_ar = np.arange(24)
three_d_ar = one_d_ar.reshape(4,3,2)
print(three_d_ar)
# QUESTION #7
AR = np.arange(25).reshape(5,5)
print(AR)
print(np.square(AR))
# QUESTION #8
np.random.seed(123)
arr1 = np.random.randint(30, size = (5,6))
print(arr1)
print("MEAN:",arr.mean())
# QUESTION #9
print(np.std(arr1))
# QUESTION #10
print(np.median(arr1))
# QUESTION #11
print("Transpose:",arr1.T)
# QUESTION #12
ARR1 = np.arange(16).reshape(4,4)
diag_sum = np.sum(np.diagonal(ARR1))
print(diag_sum)
# QUESTION #13
print("Determinant:",np.linalg.det(ARR1))
# QUESTION #14
arr5 = np.arange(10)
print("5th Percentile:",np.percentile(arr5,5))
print("95th Percentile:",np.percentile(arr5,95))
# QUESTION #15




import numpy as np

#create np array from simple list
my_list = [1,2,3,4]
my_np_array = np.array(my_list)
print(my_np_array)

#create multidimensional array

my_2nd_list = ["a", "b", "c", "c"]

lists = [my_2nd_list, my_list]
matrix_array = np.array(lists)
print(matrix_array)

#shape of the matrix - 2 rows, 4 columns
print(matrix_array.shape)
#type of the array
print(matrix_array.dtype)
#create array of zeros  -with a shape of  2 rows 5 columns passed as tuple

zeroed = np.zeros((2, 5))
print(zeroed)

#create array of ones - shape passed as list

print(np.ones([5,5]))

#an eye matrix

print(np.eye(3))

#another way to create a matrix array
#reshape tells how many rows and columns the matrix should have
np.arange(100).reshape(10, 10)

#create array with a start, stop and step
# for an evenly spaced values within a given interval

print(np.arange(1, 100, 5))
print(np.arange(5))

#multipling array just like in linear algebra

arr1 = np.array([[1, 2, 3, 4], [4, 3, 2, 1]])
print(arr1)
print(arr1*arr1)
print(arr1*2)
print(1 / arr1)
print(arr1**2)
print(arr1**0.5)

#array indexin
new_arr = np.arange(21)
#get a value from the aray
new_arr[8]
#get a range of values from the array
new_arr[1:5]

#set the values in a range
new_arr[1:5] = 100
#slice of a array is a new array
slice_new_arr = new_arr[10:16]
#select all elements in array and assingn the same value
slice_new_arr[:] = 99
#when the slice is modified the original array is modified as well
new_arr
#to make a copy of an array in order not to affect the original
#an explicit copy must be made
slice_copy = slice_new_arr.copy()
slice_copy
slice_copy[:] = 96
slice_new_arr
new_arr
slice_copy

#indexing 2d arrays


arr2d = np.array([[1, 2, 3],
                      [4, 5, 6],
                      [7, 8, 0],
                      [32, 33, 0],
                      [99, 2, 5]])
print(arr2d[2:, :2])
    #fancy indexing means selecting random rows
arr2d[[2,4, 0, 1]]

#transposing an array, fliping rows into columns
arr2d.T

#dot product
np.dot([1, 2, 3], [3, 2, 1])
np.dot(arr2d, arr2d.T)

#3d array
arr3d = np.arange(50).reshape((5, 5, 2))
print(arr3d)

#3d arrays can be transposed as well

print(arr3d.transpose((1, 0, 2)))

#arrays can swap axes

print(arr3d.swapaxes(0, 1))

#NUMPY UNIVERSAL FUNCTIONS
#universal functions are functions that can be applied
#to any value in an array

arr = np.arange(5)
# 1. square root
np.sqrt(arr)

# 2. exponential function
#ridicare numarului lui Euler la o putere indicata
#in acest caz, fiecare valoare din sir

np.exp(arr)

#binary functions

# 1. adding arrays

A = np.array([1, 2, 3])
B = np.array([6, 7, 8])
print(np.add(A, B))

# 2. multiplication
print(np.multiply(A, B))

# 3. division

print(np.divide(B, A))

# 4. maximum
#compares the maximum at each index

print(np.maximum(A, B))

# 5. Minimum

print(np.minimum(A, B))

all_universal_functions_documentation = 'https://numpy.org/doc/stable/reference/ufuncs.html#available-ufuncs'
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

print(np.eye(5))

#create array with a start, stop and step
# for an evenly spaced values within a given interval

print(np.arange(0, 100, 25))
print(np.arange(5))

#multipling array just like in linear algebra

arr1 = np.array([[1, 2, 3, 4], [4, 3, 2, 1]])
print(arr1)
print(arr1*arr1)
print(arr1*2)
#array division
print(1 / arr1)
#array exponentiation
print(arr1**2)
print(arr1**0.5)

# INDEXING ARRAYS

arr = np.arange(0, 11)
print(arr)
print(arr[8])
#get a range of values
print(arr[1:5])

#set a value for an index

arr[9] = 11
print(arr[9])

#set one value for a range in an array

arr[0:3] = 100

print(arr)

#slices of arrays
slice_of_arr = arr[0:6]
print(slice_of_arr)

#put the same value in all the elements of an array
slice_of_arr[:] = 99
print(slice_of_arr)

#!!!changes to slice_of_arr affects arr
print(arr)

#to make a copy of an array use the copy method

arr_copy = arr.copy()
print(arr_copy)
arr_copy[:] = 0
print(arr_copy)
print(arr)

#indexing 2d arrays

arr_2d = np.array(([5, 10, 15], [20,25, 30], [35, 40, 45]))
print(arr_2d)
#to see a row
print(arr_2d[1])
#to see a value, row number first column number second
print(arr_2d[2][2])
#to see a column
print(arr_2d[:3,1])

# to take a slice of a 2d array

print(arr_2d[:2, 1:])
#arrays have a shape property
arr2d = np.zeros((10, 10))
print(arr2d.shape)

for i in range(arr2d.shape[0]):
    arr2d[i] = i

print(arr2d)

#get some of the rows in the array
#fancy indexing

print(arr2d[[2,4,6,8]])
print(arr2d[[3,1,5,2]])




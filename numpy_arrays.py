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
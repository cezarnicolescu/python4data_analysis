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
print(1 / arr1)
print(arr1**2)
print(arr1**0.5)
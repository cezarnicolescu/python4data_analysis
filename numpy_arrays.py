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
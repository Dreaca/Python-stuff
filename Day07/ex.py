#create the 2D numpy array which has dimension 4*5 which contain numbers 1 to 20
# add 10 to every element
# multiply every element by 2
# calculate the square of each
# import numpy as np

# array  = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16],[17,18,19,20]])

# print("Add 10", array+10)

# print("\n================================")

# print("Multiply by 2 ", array *2)

# print("\n================================")

# print("Square root",np.sqrt(array))

#================================================================================================#

#1.create 1D a numpy array with values from 1 to 20. Use boolean values to extract all even numbers
#2. Create 1D a numpy array with elements 10,20,30,40,50 . Use boolean indexing to extract all elements greater than the mean 
#of the array.

import numpy as np

array = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])

even_numbers = array[array%2 == 0]

print("Even numbers:", even_numbers)

array_2 = np.array([10,20,30,40,50])

mean_value = np.mean(array_2)

print("Mean value:", mean_value)

filtered = array_2[array_2 > mean_value]

print(filtered)


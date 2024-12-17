#create the 2D numpy array which has dimension 4*5 which contain numbers 1 to 20
# add 10 to every element
# multiply every element by 2
# calculate the square of each
import numpy as np

array  = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16],[17,18,19,20]])

print("Add 10", array+10)

print("\n================================")

print("Multiply by 2 ", array *2)

print("\n================================")

print("Square root",np.sqrt(array))
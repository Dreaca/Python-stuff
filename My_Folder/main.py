# import my_calculator.addition;
# import my_calculator.subtraction;

# result_1 = my_calculator.addition.add(5,3)
# result_2 = my_calculator.subtraction.subtraction(10,4)

# print("Addition Result : ", result_1)

# print("Subtraction Result : ", result_2) ~~~~First way

################################################################################################################################

# from my_calculator import addition;
# from my_calculator import subtraction;

# result_1 = addition.add(5,3)

# result_2 = subtraction.subtraction(10,4)

# print("Addition Result : ", result_1)
# print("Subtraction Result : ", result_2) #~~~~Second way

#############################################################################################################################

from my_calculator.addition import add
from my_calculator.subtraction import subtraction

result_1 = add(5,3)

result_2 = subtraction(10,4)

print("Addition Result : ", result_1)

print("Subtraction Result : ", result_2) #~~~~Third way



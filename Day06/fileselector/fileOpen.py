# file_1 = open("Day06\mytext.txt", "r")
# # file_content = file_1.read()

# # file_content = file_1.readline()

# file_content = file_1.readlines()

# print(file_content, type(file_content))

# file_1.close()

with open("Day06/my_file_1.txt", "w") as file:
    file.write("Hello World !")
    file.write("\nThis is another line.")

with open("Day06/my_file_2.txt", "w+") as file:
    file.writelines(["Hello World", "\nThis is my kingdom come","\nThis is another line"])
    
with open("Day06/my_file_2.txt", "a") as file:
    file.write("\n We are global citizens")
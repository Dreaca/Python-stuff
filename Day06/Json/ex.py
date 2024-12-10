#you are given a file name students.json which contains information about students and their grades.
#Your task is to,
            #Read the json file
            #Display the names of all students who scored above 75
            #Add a new student record to the file
            #Save the updated data back to the JSon file
import json
with open("Day06/Json/student.json","r") as student:
    students = json.load(student)

for student in students:
    if student["score"] > 75:
        print(student["name"])

name = input("Enter the name :")
score = input("Enter the score :")

new_student = {
    "name": name,
    "score": int(score),
}
students.append(new_student)

print(students)

with open("Day06/Json/student.json","a") as student:

    json_data = json.dumps(students, indent=4);
    student.write(json_data)



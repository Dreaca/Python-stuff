#You are tasked to create a python program to manage a company's employee records stored in csv files.
#The program should read the employee details from a csv file, filter the records based on a condition and write the filters 
#record to a new csv file
#Input file = employee.csv contains the following fields : EmployeeID,Name,Department,Salary
#Output file = high_salary_employee.csv : you will create this file. It should contain records of employees whose salaries are
#above 57000. The fields should remain the same
#Tasks :
        #Read the input file. Use csv.reader to read employees.csv and display all the records on the console
        #Filter the records identified by Salary > 57000
        #Write the filtered records to high_salary_employee.csv using csv.DictWriter to write the filtered records

import csv

csv_path = "Day06/csv/employee.csv"
with open(csv_path, 'r') as csv_file:
    reader = csv.reader(csv_file)

    for row in reader:
        print(row)

emp_csv = open(csv_path, 'r')

dict_reader = csv.DictReader(emp_csv)

file_path = 'Day06/csv/high_salary_employee.csv'

with open(file_path, 'w', newline='') as csvfile:
    fieldnames = ['EmployeeID', 'Name', 'Department', 'Salary']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    for row in dict_reader:
        if float(row['Salary']) > 57000:
            writer.writerow(row)

emp_csv.close()


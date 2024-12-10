import csv

csv_path = "Day06/csv/customers-100.csv"

with open(csv_path, 'r',newline='') as customers:
    csv_reader = csv.reader(customers)

    for row in csv_reader:
        print(row,type(row))
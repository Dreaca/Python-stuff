import csv

csv_path = "Day06/csv/my_csv_file.csv"

data =[{"Name": "John Doe", "Age":39, "City": "New York"},
       {"Name":"Jane Smith", "Age":29, "City": "Los Angeles"},
       {"Name":"Bobby John", "Age":"38", "City": "Chicago"}]

field_names =["Name","Age","City"]

with open(csv_path, 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=field_names)
    writer.writeheader()

    for row in data:
        writer.writerow(row)
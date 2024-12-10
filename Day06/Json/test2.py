import json

data ={
    "name": "Kasun",
    "age": 23,
    "department": "Animation",
    "salary": 50000
}

json_file_path = "Day06/Json/test.json"

with open(json_file_path, 'w') as json_file:
    json_data = json.dumps(data, indent=4)
    json_file.write(json_data)
import json


path = "Day06/Json/example_1.json"

with open(path, 'r') as f:
    data = json.load(f)

print(data,type(data))
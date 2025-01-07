import requests

response = requests.get("http://api.github.com/events")

print(response.status_code)

if response.status_code == 200:
    print("OK")
import requests


json_data = {
    "name": "Allen",
    "interest": ["A", "B"]
}

res = requests.post(
    "http://localhost:5001/hello_json",
    json=json_data
)

json_data = requests.get(
    "http://localhost:5001/poker?player=5"
).json()

print(json_data)
print(type(json_data))

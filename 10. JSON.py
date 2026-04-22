import json

import requests

# Write JSON data in text file

book = {}

book['tom'] = {
    'name': 'Tom',
    'age': 20,
    'phone': 12345678
}

book['john'] = {
    'name': 'John',
    'age': 25,
    'phone': 987654321
}

s = json.dumps(book)
print(s)
print(type(s))

with open(r"D:\Ashish Doc\Ashish\AI-engineer\1. Python\Output\book.txt", "w") as f:
    f.write(s)

print("*" * 50)

# Read Text file

data = open(r"D:\Ashish Doc\Ashish\AI-engineer\1. Python\Output\book.txt", "r")
s_data = data.read()
print(s_data)
print(type(s_data))

j_data = json.loads(s_data)
print(j_data)
print(type(j_data))

print("*" * 50)

# url = 'https://jsonplaceholder.typicode.com/todos/1'
url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    print(data)
    for item in data:
        print(item['name'])
else:
    print(f"Response code",response.status_code)

print("*" * 50)
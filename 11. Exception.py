
try:
    num = int(input("Enter a number: "))

    cal = 10 / num
except Exception as exp:
    print(f"Exception: {exp}")
    print(f"Exception Type: {type(exp).__name__}")
else:
    print(f"Calculation: {cal}")
finally:
    print(f"Code run complete.")

print("*"*50)

import json
import requests

url = "https://jsonplaceholder.typicode.com/users"

try:
    response = requests.get(url)
except Exception as exp:
    print(f"Exception: {exp}")
else:
    data = response.json()
    print(data)
finally:
    print(f"Code run complete.")


print("*"*50)

# User Define Exception

class User_Exp(Exception):
    def __init__(self, msg):
        self.msg = msg

    def display(self):
        print(f"User define Exp: {self.msg}")

try:
    # raise User_Exp(input("Enter a Exp: "))
    raise User_Exp("Exception form Ashish")
except User_Exp as exp:
    exp.display()



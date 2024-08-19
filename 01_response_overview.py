import requests

# Getting desired web address
address = ""
address = input("Input web address:\n")

if address == "":
    address = "https://api.github.com"

response = requests.get(address)

## Checking Response  Status Code

if response.status_code == 200:
    print("Success!")
elif response.status_code == 404:
    print("Not Found")

## Using  build in response  logic

if response:
    print("Success!!")
else:
    raise Exception(f"Non-success status code: {response.status_code}")

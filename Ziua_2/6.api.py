# API - Application Programming Interface 
# UI - User Interface

import requests

URL = "https://api.chucknorris.io/jokes/random"

response = requests.get(URL)
print(response.status_code)
print(response.json())

response_json =  response.json()
print(type(response_json))

print("Gluma:", response_json["value"])

with open("Ziua_2/6.glume.txt", "a") as fwriter:
    fwriter.write(response_json["value"])
    fwriter.write("\n")


response = requests.get("https://api.chucknorris.io/img/avatar/chuck-norris.png")
with open("Ziua_2/6.chuck-norris.png", "wb") as fwriter:
    fwriter.write(response.content)

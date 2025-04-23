import json
# JavaScript Object Notation


dictionar = {
    "salut" : "hello",
    "varsta" : "age",
    "bun venit": "welcome" 
}

with open("Ziua_2/5.traduceri.json", "w") as fwriter:
    json.dump(dictionar, fwriter)
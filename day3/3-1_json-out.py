import json
price = {
"date": "2020-04-05",
"price": {
"Apple": 80,
"Orange": 55,
"Banana": 40
}}
s = json.dumps(price)  
print(s)

import requests
import json

response = requests.get("https://api.punkapi.com/v2/beers")

jsonResp = json.loads(response.text)

print(response.text)
print(jsonResp)

#print(jsonResp[0]["name"])
for beer in jsonResp:
    print(beer["name"])

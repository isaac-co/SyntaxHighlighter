import requests
import json

data = {
      "key":"7a92f55097104ec88155244b8f084016",
      "q":"Sams Zacatecas, Mexico",
      "pretty":1
      }


response= requests.get("https://api.opencagedata.com/geocode/v1/json", params=data)

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

#jprint(response.json())

lol= response.json()
datos= []
try:
    datos.append(lol['results'][0]['components']['city'])
except KeyError: 
    datos.append("NA")
try:
    datos.append(lol['results'][0]['components']['county']) 
except KeyError: 
    datos.append("NA")
try:
    datos.append(lol['results'][0]['components']['postcode']) 
except KeyError: 
    datos.append("NA")
try:
    datos.append(lol['results'][0]['geometry']['lat'])
except KeyError: 
    datos.append("NA")
try:
    datos.append(lol['results'][0]['geometry']['lng']); 
except KeyError: 
    datos.append("NA")
try:
    datos.append(lol['results'][0]['confidence']); 
except KeyError: 
    datos.append("NA")
    


print(datos)
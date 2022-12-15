import json
import requests

city = input('Введите город - ')

with open('API_key/myKey.txt', mode='r+') as file:
   password = file.read()

value = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={password}"

myAPI = requests.get(value)

desearicationIntuObject = json.loads(myAPI.text)

print(f"Температура = {round(desearicationIntuObject['main']['temp'] - 273.15)}\u00B0C")

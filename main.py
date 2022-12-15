import json
import requests

city = input('Введите город - ')

with open('API_key/myKey.txt', mode='r+') as file:
   password = file.read()

value = r"https://api.openweathermap.org/data/2.5/weather?q={}&appid={}"

myAPI = requests.get(value.format(city,password))

desearicationIntuObject = json.loads(myAPI.text)

print(f"Температура = {round(desearicationIntuObject['main']['temp'] - 273.15)}\u00B0C")

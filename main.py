import requests
from pprint import pprint

API_key = "13c73780b9790afad64455355c82068b"

city = input("Enter your city: ")

base_url = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+API_key

weather_data = requests.get(base_url).json()

pprint(weather_data)







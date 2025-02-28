import requests
from config import API_KEY

LAT = -32.8894155
LON = -68.8446177
URL = f"https://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LON}&appid={API_KEY}&units=metric"

response = requests.get(URL)
print(response.json())

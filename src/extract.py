import requests
import pandas as pd
from config import API_KEY

LAT = -32.8894155
LON = -68.8446177
URL = f"https://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LON}&appid={API_KEY}&units=metric&lang=es"


def extract_data():
    response = requests.get(URL)
    data = response.json()
    data_dict = {
        "fecha_hora": pd.to_datetime(data["dt"], unit="s"),
        "pais": data["sys"]["country"],
        "ciudad": data["name"],
        "temp_actual": data["main"]["temp"],
        "sensacion_termica": data["main"]["feels_like"],
        "clima": data["weather"][0]["main"],
        "descripcion_clima": data["weather"][0]["description"],
        "temp_min": data["main"]["temp_min"],
        "temp_max": data["main"]["temp_max"],
        "velocidad_viento[m/s]": data["wind"]["speed"],
    }
    df = pd.DataFrame(data_dict, index=[0])
    return df

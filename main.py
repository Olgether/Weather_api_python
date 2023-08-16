import requests
from pprint import pprint
from datetime import datetime

API = "b6c6070f01146d48dc0c247e08f7018f"
city = "Almaty"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric"

res = requests.get(url)
data = res.json()

# pprint(data)

sunrise = datetime.fromtimestamp(data["sys"]["sunrise"])
sunset = datetime.fromtimestamp(data["sys"]["sunset"])

info = f"""
city: {data["name"]}
temp: {data["main"]["temp"]}
pres: {data["main"]["pressure"]}
humid: {data["main"]["humidity"]}

windspd: {data["wind"]["speed"]}
Weather: {data["weather"][0]["description"]}

voskhod : {sunrise.time()}
day length : {sunset - sunrise}
zakat : {sunset.time()}

"""

print(info)
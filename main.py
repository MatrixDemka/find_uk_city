import requests
import time
from pprint import pp

# https://geocode.maps.co/reverse?lat=latitude&lon=longitude&api_key=api_key

url = "https://geocode.maps.co/reverse"
token = "67113daabed4b697756967ztb90aa98"

_coordinates = [
    ('55.7514952', '37.618153095505875'),
    ('52.3727598', '4.8936041'),
    ('53.4071991', '-2.99168')
]

uk_city = ["Leeds", "London", "Liverpool", "Manchester", "Oxford", "Edinburgh", "Norwich", "York"]

for latitude, longitude in _coordinates:
    # latitude = i[0]
    # longitude = i[1]

    params = {
        "lat": latitude,
        "lon": longitude,
        "api_key": token
    }

    response = requests.get(url=url, params=params)
    data = response.json()
    city = data["address"]["city"]
    #city = data.get("address", {}).get("city")

    if city in uk_city:
        time.sleep(2)
        print(city)
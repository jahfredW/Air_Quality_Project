import geopy
import requests

town = input('ville svp ? ')
loc = geopy.geocoders.Nominatim(user_agent="GetLoc")
getLoc = loc.geocode(town)


r = requests.get(f'http://api.openweathermap.org/data/2.5/air_pollution?lat={getLoc.latitude}&lon={getLoc.longitude}'
                     f'&appid=a1f0eace01a7421a3046c32bf90392a5')


texte = r.json()
print(texte)

"""
r2 = requests.get('http://127.0.0.1:8001/pollution/Paris/all')
print(r2.json()["datas"])
"""
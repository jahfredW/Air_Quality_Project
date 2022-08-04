import geopy
import requests

loc = geopy.geocoders.Nominatim(user_agent="GetLoc")
getLoc = loc.geocode('Dunkerque')



r = requests.get(f'http://api.openweathermap.org/data/2.5/air_pollution?lat={getLoc.latitude}&lon={getLoc.longitude}'
                     f'&appid=a1f0eace01a7421a3046c32bf90392a5')

texte = r.json()
print(texte['list'])
import requests
import pyowm
from pyowm.utils.config import get_default_config

apikey = 'de344c900509e22467e79e19be02d6bb'

config_dict = get_default_config()
config_dict['language'] = 'fr'
test_api = pyowm.OWM(apikey, config_dict)

meteo_api_data = test_api.city_id_registry()
location = meteo_api_data.geopoints_for('Dunkerque')
location = location[0]
"""
print(location.lon)
print(test_api.weather_manager().one_call(location.lat, location.lon))
print(test_api.airpollution_manager().air_quality_forecast_at_coords(location.lat, location.lon))
"""



"""
response = requests.get('http://api.openweathermap.org/data/2.5/forecast?lat=50&lon=50&appid=de344c900509e22467e79e19be02d6bb')
print(response.status_code)
"""
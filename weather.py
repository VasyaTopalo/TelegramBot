import pyowm
from pyowm.utils.config import get_default_config

owm = pyowm.OWM('b1bfa5ad5e3bbe621f0153bc78503113')

def get_weather(place):
    try:
        pl = ""
        if place[:5] == 'місті':
            pl = "місті"
            place = place[6:]
        elif place[:4] == "селі":
            pl = "селі"
            place = place[5:]
        elif place[:4] == "смт.":
            pl = "смт."
            place = place[5:]

        config_dict = get_default_config()
        config_dict['language'] = 'ua'

        observation = owm.weather_manager().weather_at_place(place)

        w = observation.weather
        detailed_status = observation.weather.detailed_status
        wind = observation.weather.get_wind
        if detailed_status == "чисте небо":
            detailed_status += ' ☀'
        elif detailed_status == "уривчасті хмари" or detailed_status == "рвані хмари":
            detailed_status += ' 🌤'

        temp = observation.weather.temperature('celsius')['temp']


        result = "В {0} {1} зараз {2} \nТемпература {3}".format(pl, place.title(), detailed_status, int(temp))
        return result
    except:
        return "Ви ввели некоректне місце 😢"



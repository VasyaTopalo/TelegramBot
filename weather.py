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
        detailed_status = w.detailed_status

        if detailed_status == "чисте небо":
            detailed_status += ' ☀'
        elif detailed_status == "уривчасті хмари" or detailed_status == "рвані хмари" or detailed_status == "кілька хмар":
            detailed_status += ' 🌤'

        temp = int(w.temperature('celsius')['temp'])
        wind = w.wind()
        humidity =  w.humidity
        message = ''

        if temp < -10:
            message = "На вулиці дуже холодно ліпше нікуди не йти"
        elif temp < 0:
            message = "На вулиці мороз, потрібно тепло одягнутись"
        elif temp < 10:
            message = "На вулиці прохолодно, але якщо одягнутись можна погуляти"
        elif temp <= 20:
            message = "На вулиці помірна температура, саме час для прогулянки!"
        elif temp < 30:
            message = "На вулиці дуже тепло, одягніть легку одежу і ідіть погуляйте на свіжому повітрі"
        else:
            message = "На вулиці дуже спекотно, ліпше утриматись від прогулянок під прямим сонцем"

        result = "В {0} {1} зараз {2} \n\n🌡 Температура: {3}℃\n🌬 Швидкість вітру: {4} м/c\n💦 Вологість: {5}%\n\n{6}".format(pl, place.title(), detailed_status, temp, wind['speed'], humidity, message)
        return result
    except:
        return "Ви ввели некоректне місце 😢"



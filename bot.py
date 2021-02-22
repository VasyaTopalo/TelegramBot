import telebot
import configure
import converter
import datetime
import pattern
from weather import get_weather

client = telebot.TeleBot(configure.TOKEN)

def olo(t):

    pass

@client.message_handler(content_types = ['text'])

def get_text(message):
    #Greeting
    hello = message.text.lower()
    if  pattern.pattern(hello) == "привіт":
        client.send_message(message.chat.id, "Привіт людина!!!")

    #Calculator
    calc = message.text.lower()

    if pattern.pattern(calc)  == "скільки буде":
        try:
            result = "{0} буде {1}".format(calc[12:], eval(calc[12:]))
            client.send_message(message.chat.id, result)
        except:
            client.send_message(message.chat.id, "Спробуйте ще раз...")

    #Валюти
    doll_curse = message.text.lower()
    euro_curse = message.text.lower()
    rub_curse = message.text.lower()
    all_curses = message.text.lower()

    if pattern.pattern(euro_curse) == "який курс євро":
        euro_curse = "Курс євро 🇪🇺 {0}".format(converter.euro + ' 🇺🇦')
        client.send_message(message.chat.id, euro_curse)

    if pattern.pattern(doll_curse) == "який курс долара":
        doll_curse = "Курс долара 🇺🇸 {0}".format(converter.doll + ' 🇺🇦')
        client.send_message(message.chat.id, doll_curse)
    if pattern.pattern(rub_curse) == "який курс рубля":
        rub_curse = "Курс рубля 🇷🇺 {0}".format(converter.euro + ' 🇺🇦')
        client.send_message(message.chat.id, rub_curse)

    if pattern.pattern(all_curses) == "скажи мені курси валют":
        euro_curse = "Курс євро EU 🇪🇺 {0}".format(converter.euro + ' UA 🇺🇦')
        doll_curse = "Курс долара US 🇺🇸 {0}".format(converter.doll + ' UA 🇺🇦')
        rub_curse = "Курс рубля RUB 🇷🇺 {0}".format(converter.euro + ' UA 🇺🇦')

        now = datetime.datetime.now()

        all_curses = "Курси валют ст. на {0}:\n\n{1}\n\n{2}\n\n{3}".format(now.strftime("%d-%m-%Y %H:%M"), euro_curse, doll_curse, rub_curse)

        client.send_message(message.chat.id, all_curses)

    #Weather forecast
    forecast = message.text.lower()
    f = forecast[13:]

    if pattern.pattern(forecast[:12]) == "яка погода в":
        client.send_message(message.chat.id, get_weather(f))
    else:
        client.send_message(message.chat.id, "Вибачте я вас не зрозумів 😢\nСпробуйте ще раз...")

client.polling(none_stop = True, interval = 0)

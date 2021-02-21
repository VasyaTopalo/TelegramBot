import telebot
import configure
import converter
import datetime
from weather import get_weather

client = telebot.TeleBot(configure.TOKEN)

def olo(t):

    pass

@client.message_handler(content_types = ['text'])

def get_text(message):
    if message.text.lower() == "привіт":
        client.send_message(message.chat.id, "Привіт людина!!!")
    calc = message.text.lower()

    if calc[:12]  == "скільки буде":
        result = "{0} буде {1}".format(calc[13:], eval(calc[13:]))
        client.send_message(message.chat.id, result)

    #Валюти
    doll_curse = message.text.lower()
    euro_curse = message.text.lower()
    rub_curse = message.text.lower()
    all_curses = message.text.lower()

    if euro_curse == "який курс євро":
        euro_curse = "Курс євро 🇪🇺 {0}".format(converter.euro + ' 🇺🇦')
        client.send_message(message.chat.id, euro_curse)

    if doll_curse == "який курс долара":
        doll_curse = "Курс долара 🇺🇸 {0}".format(converter.doll + ' 🇺🇦')
        client.send_message(message.chat.id, doll_curse)
    if rub_curse == "який курс рубля":
        rub_curse = "Курс рубля 🇷🇺 {0}".format(converter.euro + ' 🇺🇦')
        client.send_message(message.chat.id, rub_curse)

    if all_curses == "скажи мені курси валют":
        euro_curse = "Курс євро 🇪🇺 {0}".format(converter.euro + ' 🇺🇦')
        doll_curse = "Курс долара 🇺🇸 {0}".format(converter.doll + ' 🇺🇦')
        rub_curse = "Курс рубля 🇷🇺 {0}".format(converter.euro + ' 🇺🇦')

        now = datetime.datetime.now()

        all_curses = "Курси валют станом на {0}:\n{1}\n{2}\n{3}".format(now.strftime("%d-%m-%Y %H:%M"), euro_curse, doll_curse, rub_curse)

        client.send_message(message.chat.id, all_curses)

    #Weather forecast
    forecast = message.text.lower()
    f = forecast[13:]

    if forecast[:12] == "яка погода в":
        client.send_message(message.chat.id, get_weather(f))

client.polling(none_stop = True, interval = 0)

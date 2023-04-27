import requests
from telebot import TeleBot
from telebot.types import KeyboardButton, ReplyKeyboardMarkup

import os


WEATHER_TOKEN = os.environ['WEATHER_TOKEN']
TELEGRAM_TOKEN = os.environ['TELEGRAM_TOKEN']
WEATHER_URL = 'https://api.openweathermap.org/data/2.5/weather'
bot = TeleBot(TELEGRAM_TOKEN)


def get_weather(lat, lon):
    params = {'lat': lat, 'lon': lon, 'units': 'metric', 'lang': 'ru', 'appid': WEATHER_TOKEN}
    response = requests.get(WEATHER_URL, params=params).json()
    city = response['name']
    temp = response['main']['temp']
    feels_like = response['main']['feels_like']
    desc = response['weather'][0]['description']
    return f'Погода в городе {city}\n{desc.capitalize()}\nТемпература {temp}\nОщущается как {feels_like}'


@bot.message_handler(commands=['start'])
def start(message):
    markup = ReplyKeyboardMarkup()
    markup.add(KeyboardButton('Погода', request_location=True))
    markup.add(KeyboardButton('О проекте'))
    bot.send_message(
        message.chat.id,
        'Отправь мне местоположение и я отправлю тебе погоду',
        reply_markup=markup
    )


@bot.message_handler(regexp='О проекте')
def about(message):
    bot.send_message(
        message.chat.id,
        'Я бот для получения погоды, я отправляю погоду по местоположению, данные о погоде я беру с сайта openweathermap'
    )


@bot.message_handler(content_types=['location'])
def send_weather(message):
    lat = message.location.latitude
    lon = message.location.longitude
    weather = get_weather(lat=lat, lon=lon)
    bot.send_message(
        message.chat.id,
        weather
    )


if __name__ == '__main__':
    bot.infinity_polling()

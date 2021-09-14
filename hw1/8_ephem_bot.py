"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging
import ephem

from datetime import datetime
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import settings

PLANETS = [
    'Mercury',
    'Venus',
    'Mars',
    'Jupiter',
    'Saturn',
    'Uranus',
    'Neptune',
    'Pluto',
    'Sun',
    'Moon',
 ]

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


PROXY = {
    'proxy_url': settings.PROXY_URL,
    'urllib3_proxy_kwargs': {
        'username': settings.PROXY_USERNAME,
        'password': settings.PROXY_PASSWORD
    }
}


def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def constellation_to_me(update, context):
    user_planet = update.message.text.split()
    user_text_0, user_planet_text = user_planet
    print('Вызван /planet', user_planet_text)
    if user_planet_text not in PLANETS:
        update.message.reply_text('Я не знаю!!!')
        return
    planet_gett = getattr(ephem, user_planet_text)
    date = datetime.now()
    planet = planet_gett(date)
    planet_constellation = ephem.constellation(planet)
    update.message.reply_text(f'Планета {user_planet_text} сегодня находится в созвездии {planet_constellation}')


def main():
    mybot = Updater(settings.API_KEY, request_kwargs=PROXY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", constellation_to_me))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()

"""
Домашнее задание №2

Уровень 2
Реализуйте в боте команду /wordcount которая считает слова в присланной фразе.
Например на запрос /wordcount Привет как дела бот должен ответить: 3 слова. Не забудьте:

Добавить проверки на пустую строку
Как можно обмануть бота, какие еще проверки нужны?
-----------------------------------------------------------------------------------------
Реализуйте в боте команду, которая отвечает на вопрос “Когда ближайшее полнолуние?” 
Например /next_full_moon 2019-01-01. Чтобы узнать, когда ближайшее полнолуние, 
используйте ephem.next_full_moon(ДАТА)
-----------------------------------------------------------------------------------------
Уровень 3
Научите бота играть в города. Правила такие - внутри бота есть список городов, 
пользователь пишет /cities Москва и если в списке такой город есть, 
бот отвечает городом на букву "а" - "Альметьевск, ваш ход". Оба города должны удаляться из списка.

Помните, с ботом могут играть несколько пользователей одновременно
"""
import logging
import ephem

from datetime import datetime
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import settings

PUNC = '?!()-[]{\};:\'"\\,<>./#$%^&*_~'


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


def wordcount(update, context):
    user_wordcount = update.message.text.split()
    user_text_1, *user_wordcount_text = user_wordcount
    print('Вызван /planet', user_wordcount_text)
    if not user_wordcount_text:
        update.message.reply_text('Пустая строка!!!')
        return
    if ' '.join(user_wordcount_text).isdigit() == True:
        update.message.reply_text('В строке одни цифры!!!')
        return
    meter = 0
    for text_words in user_wordcount_text:
            if text_words not in PUNC:
                meter += 1
                print(text_words)
    update.message.reply_text(f'В тексте {meter} слов')

def next_full_moon(update, context):
    user_next_full_moon = update.message.text
    print('Вызван /next_full_moon')
    dt_moon = ephem.next_full_moon(datetime.now())
    dt_moon = ephem.localtime(dt_moon).strftime('%d.%m.%Y %H:%M')
    update.message.reply_text(f'Ближайшее полнолуние произойдет - {dt_moon}')

def city_games(update, context):
    pass
            

def main():
    mybot = Updater(settings.API_KEY, request_kwargs=PROXY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("wordcount", wordcount))
    dp.add_handler(CommandHandler("next_full_moon", next_full_moon))
    dp.add_handler(CommandHandler("city_game", city_games))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()


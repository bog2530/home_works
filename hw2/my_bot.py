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
Научите бота выполнять основные арифметические действия с двумя числами: 
сложение, вычитание, умножение и деление. 
Если боту дать команду /calc 2-3, он должен ответить “-1”.

"""
import logging
import ephem

from datetime import datetime
from telegram.ext import Updater, CommandHandler

import settings

PUNC = '?!()-[]{\};:\'"\\,<>./#$%^&*_~'
CALC_X = ['+', '-', '/', '**', '*']


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
    update.message.reply_text(text)

def wordcount(update, context):
    user_wordcount = update.message.text.split()
    user_text_1, *user_wordcount_text = user_wordcount
    logging.info(f'/wordcount - {user_wordcount_text}')
    if not user_wordcount_text:
        update.message.reply_text('Пустая строка!!!')
        return
    if ' '.join(user_wordcount_text).isdigit():
        update.message.reply_text('В строке одни цифры!!!')
        return
    meter = sum(1 for x in user_wordcount_text if x not in PUNC)
    update.message.reply_text(f'В тексте {meter} слов')

def next_full_moon(update, context):
    user_next_full_moon = update.message.text
    dt_moon = ephem.next_full_moon(datetime.now())
    dt_moon = ephem.localtime(dt_moon).strftime('%d.%m.%Y %H:%M')
    update.message.reply_text(f'Ближайшее полнолуние произойдет - {dt_moon}')


def calc_1(x, y , operation):
    operations = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y,
    }
    op_calc = operations.get(operation)
    return op_calc(x, y)


def calc(update, context):
    calc_user = update.message.text.split()
    try:
        user_text, calc_text = calc_user
    except ValueError: 
        update.message.reply_text('Формат ввода: x+y!') 
    for sign in calc_text:
        if sign in CALC_X:
            user_calc = calc_text.split(sign)
            logging.info(f'/wordcount - {user_calc}')
            try:
                update.message.reply_text(calc_1(float(user_calc[0]), float(user_calc[1]), sign))
            except ValueError:
                update.message.reply_text('Недопустимое значение') 
            except ZeroDivisionError:
                update.message.reply_text('Деление на 0') 
            return
    update.message.reply_text('Поддерживаются только операции +, -, *, /')


def main():
    mybot = Updater(settings.API_KEY, request_kwargs=PROXY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("wordcount", wordcount))
    dp.add_handler(CommandHandler("next_full_moon", next_full_moon))
    dp.add_handler(CommandHandler("calc", calc))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()

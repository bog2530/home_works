"""

Домашнее задание №1

Условный оператор: Возраст

* Попросить пользователя ввести возраст при помощи input и положить 
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь: 
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат 
  работы функции в переменную
* Вывести содержимое переменной на экран

"""

__name__ = int(input('Введите возраст: '))


def main(__name__):
    if __name__ <= 6:
        result = 'Детский сад!'
    elif __name__ <= 18:
        result = 'Школа!'
    elif __name__ <= 24:
        result = 'ВУЗ!'
    else:
        result = "Работа!"
    return(result)

result = main(__name__)
print(result)
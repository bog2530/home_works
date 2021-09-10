"""

Домашнее задание №1

Цикл while: ask_user со словарём

* Создайте словарь типа "вопрос": "ответ", например:
  {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
* Напишите функцию ask_user() которая с помощью функции input()
  просит пользователя ввести вопрос, а затем, если вопрос есть
  в словаре, программа давала ему соотвествующий ответ. Например:

    Пользователь: Что делаешь?
    Программа: Программирую
    
"""

questions_and_answers = {'Что делаешь?': 'Программирую',
'Как дела?': 'Нормально',
'Как погода?': 'Дождь'}


def ask_user(answers_dict):
    while True:
        hello = input('Задайте вопрос: ')
        if hello == 'СТОП':
            break
        answer = questions_and_answers.get(hello)
        print(answer)

if __name__ == "__main__":
    ask_user(questions_and_answers)

"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""
import csv
USERS_LIST = [
    {'name': 'Alex', 'age': '35', 'job': 'Manager'},
    {'name': 'Max', 'age': '27', 'job': 'Engineer Designer'},
    {'name': 'Tatiana', 'age': '25', 'job': 'Technologist'},
    {'name': 'Andrew', 'age': '35', 'job': 'Programmer'}
]
def main():
    with open('users.csv', 'w', encoding='utf-8') as f:
        fieldes = ['name', 'age', 'job']
        writer = csv.DictWriter(f, fieldes, delimiter=';')
        writer.writeheader()
        for user in USERS_LIST:
            writer.writerow(user)

if __name__ == "__main__":
    main()

"""
Домашнее задание №2

Работа с файлами


1. Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
2. Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
3. Подсчитайте количество слов в тексте
4. Замените точки в тексте на восклицательные знаки
5. Сохраните результат в файл referat2.txt
"""

def main():
    with open('referat.txt', 'r', encoding='utf -8') as f:
        text_file = f.read()
        print(len(text_file))
        text_words = len(text_file.split())
        print(text_words)
    with open('referat2.txt', 'w', encoding='utf -8') as f_1:
        for text_stick in text_file:
            if text_stick != '.':
                text_file = f_1.write(text_stick)
            else:
                text_file = f_1.write(text_stick.replace('.', '!'))
                
                
    

if __name__ == "__main__":
    main()

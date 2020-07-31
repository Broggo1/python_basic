# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.
file = open('new_file.txt', 'x')
while True:
    text = input()
    if text == '': break
    file.write(text+'\n')
file.close()

# Задача 2
# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.
with open('new_file.txt') as file:
    all_lines = 0
    lines = 0
    words = 0
    letters = 0
    for line in file:
        all_lines += 1
        lines += 1
        for letter in line:
            if letter == ' ':
                words += 1
        print(f'Строка номер: {lines} Кол-во слов: {words + 1}')
        words = 0
print(f'Всего строк: {all_lines}')
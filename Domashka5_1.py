# Домашка № 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

my_f = open('domashka5_1.txt', 'x', encoding='utf-8')

while True:
    a = input('')
    my_f.writelines(a + '\n')
    if not a:
        break

my_f.close()
# Вам доступен текстовый файл text.txt с одной строкой текста.
# Напишите программу, которая выводит на экран эту строку в обратном порядке.
#
# Формат входных данных
# На вход программе ничего не подается.
#
# Формат выходных данных
# Программа должна вывести строку указанного файла в обратном порядке.

with open('text.txt') as file:
    line = file.read()
    print(line[::-1])

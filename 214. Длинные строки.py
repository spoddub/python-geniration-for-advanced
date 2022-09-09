# Вам доступен текстовый файл lines.txt, в котором записаны строки текста.
# Напишите программу, которая выводит все строки наибольшей длины из файла, не меняя их порядок.
#
# Формат входных данных
# На вход программе ничего не подается.
#
# Формат выходных данных
# Программа должна вывести строки указанного файла, имеющие наибольшую длину, не меняя их порядка.

max_len = 0
max_str = []

with open('lines.txt') as file:
    for line in file.readlines():
        if len(line) > max_len:
            max_len = len(line)
            max_str = [line]
        elif len(line) == max_len:
            max_str.append(line)

for elem in max_str:
    print(elem, end='')

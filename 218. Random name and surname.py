# Вам доступны два текстовых файла first_names.txt и last_names.txt, один с именами, другой с фамилиями.
#
# Напишите программу, которая c помощью модуля random создает
# 3
# 3 случайные пары имя + фамилия, а затем выводит их, каждую на отдельной строке.
#
# Формат входных данных
# На вход программе ничего не подается.
#
# Формат выходных данных
# Программа должна вывести текст в формате, приведенном в примере.

from random import randint

firstNames = []
lastNames = []

with open('first_names.txt') as file:
    for line in file.readlines():
        firstNames.append(line)

with open('last_names.txt') as file:
    for line in file.readlines():
        lastNames.append(line)

for i in range(3):
    print(firstNames[randint(0, len(firstNames))].strip() + ' ' + lastNames[randint(0, len(lastNames))].strip())

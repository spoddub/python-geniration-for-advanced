# Вам доступен текстовый файл file.txt, набранный латиницей.
# Напишите программу, которая выводит количество букв латинского алфавита, слов и строк.
# Выведите три найденных числа в формате, приведенном в примере.
#
# Формат входных данных
# На вход программе ничего не подается.
#
# Формат выходных данных
# Программа должна вывести три найденных числа в формате, приведенном в примере.

linesNum = 0
wordsNum = 0
lettersNum = 0

with open('file.txt') as file:
    for line in file.readlines():
        linesNum += 1
        wordsNum += len(line.split())
        lettersNum += len([elem for elem in line if elem.isalpha()])

print("Input file contains:\n" + str(lettersNum) + " letters\n" + str(wordsNum) + " words\n" + str(linesNum) + " lines")

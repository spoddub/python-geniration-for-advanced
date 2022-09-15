# Вам доступен текстовый файл input.txt, состоящий из нескольких строк.
# Напишите программу для записи содержимого этого файла в файл output.txt в виде нумерованного списка,
# где перед каждой строкой стоит ее номер, символ ) и пробел. Нумерация строк должна начинаться с 1.
#
# Формат входных данных
# На вход программе ничего не подается.
#
# Формат выходных данных
# Программа должна создать файл с именем output.txt и записать в него пронумерованные строки файла input.txt.

arr = []
counter = 1

with open('input.txt') as file:
    for line in file.readlines():
        arr.append(str(counter) + ') ' + line)
        counter += 1

with open('output.txt', 'w') as file:
    file.writelines(arr)

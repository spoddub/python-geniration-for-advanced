# Вам доступен текстовый файл logfile.txt с информацией о времени входа пользователя в систему и выхода из нее.
# Каждая строка файла содержит три значения, разделенные запятыми и символом пробела:
# имя пользователя, время входа, время выхода, где время указано в 24-часовом формате.
#
# Напишите программу, которая создает файл output.txt и выводит в него имена всех пользователей
# (не меняя порядка следования), которые были в сети не менее часа.
#
# Формат входных данных
# На вход программе ничего не подается.
#
# Формат выходных данных
# Программа должна создать файл с именем output.txt в соответствии с условием задачи.

import io

result = []

with io.open('logfile.txt', encoding='utf-8') as file:
    for line in file:
        name = line.strip().split(', ')[0]
        startTime = line.strip().split(', ')[1]
        endTime = line.strip().split(', ')[2]
        if int(endTime.split(':')[0]) - int(startTime.split(':')[0]) > 1:
            result.append(name + '\n')
        if int(endTime.split(':')[0]) - int(startTime.split(':')[0]) == 1 and int(endTime.split(':')[1]) - int(startTime.split(':')[1]) >= 0:
            result.append(name + '\n')

with open('output.txt', 'w') as file:
    file.writelines(result)

# Вам доступен текстовый файл goats.txt в первой строке которого написано слово COLOURS,
# далее идет список всех возможных цветов козлов. Затем идет строка со словом GOATS,
# и далее непосредственно перечисление козлов разных цветов. Перечень козлов включает только строки из первого списка.
#
# Напишите программу создания файла answer.txt и вывода в него списка козлов,
# которые удовлетворяют условию загадки от Жака Фреско.
#
# Формат входных данных
# На вход программе ничего не подается.
#
# Формат выходных данных
# Программа должна создать файл с именем answer.txt и вывести в него в алфавитном порядке названия цветов козлов,
# которые удовлетворяют условию загадки Жака Фреско.

with open('goats.txt', 'r', encoding='utf-8') as file, open('answer.txt', 'w', encoding='utf-8') as answer:
    lst = []
    for string in file.read().split('GOATS'):
        lst.append(string.strip('COLOURS').strip('\n').strip(' goat ').split(' goat\n'))
    for c in lst[0]:
        if lst[1].count(c) > len(lst[1]) * 0.07:
            print(f'{c} goat', file=answer)


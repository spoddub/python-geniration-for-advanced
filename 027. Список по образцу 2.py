# На вход программе подается число n.
# Напишите программу, которая создает и выводит построчно вложенный список,
# состоящий из n списков [[1], [1, 2], [1, 2, 3], ..., [1, 2, ..., n]].
#
# Формат входных данных
# На вход программе подается натуральное число n.
#
# Формат выходных данных
# Программа должна вывести построчно указанный вложенный список.


my_list = []
n = int(input())
for i in range(1, n + 1):
    my_list.append(i)
    print(my_list)

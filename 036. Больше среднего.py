# Напишите программу, которая выводит количество элементов квадратной матрицы в каждой строке,
# больших среднего арифметического элементов данной строки.
#
# Формат входных данных
# На вход программе подаётся натуральное число n — количество строк и столбцов в матрице,
# затем элементы матрицы (целые числа) построчно через пробел.
#
# Формат выходных данных
# Программа должна вывести n чисел — для каждой строки количество элементов матрицы,
# больших среднего арифметического элементов данной строки.


n = int(input())
matrix = []
for i in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)

for i in matrix:
    average = 0
    summa = 0
    for j in i:
        average = sum(i) / len(i)
        if average < int(j):
            summa += 1
    print(summa)
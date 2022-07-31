# Напишите программу для вычисления суммы двух матриц.
#
# Формат входных данных
# На вход программе подаются два натуральных числа n и m — количество строк и столбцов в матрицах,
# затем элементы первой матрицы, затем пустая строка, далее следуют элементы второй матрицы.
#
# Формат выходных данных
# Программа должна вывести результирующую матрицу, разделяя элементы символом пробела.


n, m = [int(i) for i in input().split()]
matrix1 = [[int(i) for i in input().split()] for _ in range(n)]
a = input()
matrix2 = [[int(i) for i in input().split()] for _ in range(n)]
matrix3 = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        matrix3[i][j] += matrix1[i][j] + matrix2[i][j]

for row in matrix3:
    print(*row)

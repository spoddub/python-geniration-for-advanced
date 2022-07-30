# Магическим квадратом порядка n называется квадратная таблица размера n × n,
# составленная из всех чисел 1,2,3,…,n так, что суммы по каждому столбцу,
# каждой строке и каждой из двух диагоналей равны между собой. Напишите программу,
# которая проверяет, является ли заданная квадратная матрица магическим квадратом.
#
# Формат входных данных
# На вход программе подаётся натуральное число n — количество строк и столбцов в матрице,
# затем элементы матрицы: n строк, по n чисел в каждой, разделённые пробелами.
#
# Формат выходных данных
# Программа должна вывести слово YES, если матрица является магическим квадратом,
# и слово NO в противном случае.


n = int(input())
matrix = [[int(i) for i in input().split()] for j in range(n)]

magic = sum(matrix[0])
flag = 'YES'
digits = [i for i in range(1, n ** 2 + 1)]

for i in range(n):
    for j in range(n):
        if matrix[i][j] in digits:
            digits.remove(matrix[i][j])
    if i == n - 1 and j == n - 1 and digits != []:
        flag = 'NO'

for i in range(n):
    if sum(matrix[i]) != magic:
        flag = 'NO'
        break

for j in range(n):
    result = 0
    for i in range(n):
        result += matrix[i][j]
        if i == n - 1 and result != magic:
            flag = 'NO'
            break

print(flag)

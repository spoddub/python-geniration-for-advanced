# Напишите программу, которая считывает натуральное число n
# и выводит первые n чисел последовательности Трибоначчи.
#
# Формат входных данных
# На вход программе подается одно число n – количество членов последовательности.
#
# Формат выходных данных
# Программа должна вывести члены последовательности Трибоначчи, отделенные символом пробела.

n = int(input())
f1, f2, f3 = 1, 1, 1
for i in range(n):
    print(f1, end=' ')
    f1, f2, f3 = f2, f3, f1 + f2 + f3

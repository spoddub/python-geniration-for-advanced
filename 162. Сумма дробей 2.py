# На вход программе подается натуральное число n.
# Напишите программу, которая вычисляет и выводит рациональное число, равное значению выражения

from math import factorial

from fractions import Fraction


n = int(input())
result = 0
for i in range(1, n + 1):
    result += Fraction(1, factorial(i))
print(result)

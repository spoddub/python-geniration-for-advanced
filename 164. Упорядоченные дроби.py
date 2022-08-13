# На вход программе подается натуральное число n.
# Напишите программу, которая выводит в порядке возрастания все несократимые дроби,
# заключённые между 0 и 1, знаменатель которых не превосходит n.

from math import gcd
from fractions import Fraction
n = int(input())
result = []
while n != 1:
    for i in range(1, n):
        if gcd(i, n) == 1:
            result.append(f'{i}/{n}')
    n -= 1
answer = sorted(map(Fraction, result))
print(*answer, sep='\n')

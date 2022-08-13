# Даны две дроби в формате a/b.
# Напишите программу, которая вычисляет и выводит их сумму, разность, произведение и частное.
#
# Формат входных данных
# На вход программе подаются две ненулевые дроби, каждая на отдельной строке.
#
# Формат выходных данных
# Программа должна вывести сумму, разность, произведение и частное двух дробей.

from fractions import Fraction


n, n2 = input(), input()
summa = Fraction(n) + Fraction(n2)
raznost = Fraction(n) - Fraction(n2)
proizv = Fraction(n) * Fraction(n2)
chastnoe = Fraction(n) / Fraction(n2)
print(n, '+', n2, '=', summa)
print(n, '-', n2, '=', raznost)
print(n, '*', n2, '=', proizv)
print(n, '/', n2, '=', chastnoe)

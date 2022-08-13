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
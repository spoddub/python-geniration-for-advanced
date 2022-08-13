# Дано натуральное число n и два комплексных числа.
# Напишите программу, которая вычисляет и выводит значение выражения

n = int(input())
z1 = complex(input())
z2 = complex(input())
print(z1 ** n + z2 ** n + z1.conjugate() ** n + z2.conjugate() ** (n+1))

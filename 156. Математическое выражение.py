# На вход программе подается Decimal число d. Напишите программу, которая вычисляет значение выражения

from decimal import *
num = Decimal(input())
answer = num.exp() + num.ln() + num.log10() + num.sqrt()
print(answer)


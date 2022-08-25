# Напишите программу, которая принимает число и название функции,
# а выводит результат применения функции к данному числу.
#
# Список возможных функций:
#
# квадрат: функция принимает число и возвращает его квадрат;
# куб: функция принимает число и возвращает его куб;
# корень: функция принимает число и возвращает корень квадратный из этого числа;
# модуль: функция принимает число и возвращает его модуль;
# синус: функция принимает число (в радианах) и возвращает синус этого числа.
# Формат входных данных
# На вход программе подается целое число и название функции, записанные на отдельных строках.
#
# Формат выходных данных
# Программа должна выдать результат применения функции к числу.
#
# Примечание. Решите задачу без использования условного оператора.

from math import *


def resulting(number, word):
    functions = {'квадрат': number ** 2,
                 'куб': number ** 3,
                 'корень': number ** 0.5,
                 'модуль': abs(number),
                 'синус': sin(number)}
    return functions[word]


num, wrd = int(input()), input().lower()
print(resulting(num, wrd))

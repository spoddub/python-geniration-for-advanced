from math import *
def resulting(number, word):
    functions = {'квадрат': number ** 2,
                 'куб': number ** 3,
                 'корень': sqrt(number),
                 'модуль': abs(number),
                 'синус': sin(number)}
    return functions[word]


num, wrd = int(input()), input().lower()
print(resulting(num, wrd))

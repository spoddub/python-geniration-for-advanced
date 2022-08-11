# Напишите программу, которая с помощью модуля random генерирует 100 случайных номеров лотерейных билетов
# и выводит их каждый на отдельной строке. Обратите внимание, вы должны придерживаться следующих условий:
#
# номер не может начинаться с нулей;
# номер лотерейного билета должен состоять из 7 цифр;
# все 100 лотерейных билетов должны быть различными.

import random

for i in range(100):
    print(random.randint(1000000, 9999999))

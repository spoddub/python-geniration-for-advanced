# Напишите программу, которая с помощью модуля random генерирует случайный пароль.
# Программа принимает на вход длину пароля и выводит случайный пароль,
# содержащий только символы английского алфавита a..z, A..Z (в нижнем и верхнем регистре).
#
# Примечание 1. Символам A..Z английского языка соответствуют номера с 65 по 90 в таблице символов ASCII.
#
# Примечание 2. Символам a..z английского языка соответствуют номера с 97 по 122 в таблице символов ASCII.
#
# Примечание 3. Используйте функцию chr() для получения символа по его номеру в таблице символов ASCII.

import random

length = int(input())
password = []
for symbol in range(length):
    num = random.randint(1, 2)
    if num == 1:
        password.append(chr(random.randint(65, 90)))
    else:
        password.append(chr(random.randint(97, 122)))
print(*password, sep='')

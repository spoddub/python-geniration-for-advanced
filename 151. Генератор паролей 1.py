# Напишите программу, которая с помощью модуля random генерирует
# n
# n паролей длиной
# m
# m символов, состоящих из строчных и прописных английских букв и цифр, кроме тех, которые легко перепутать между собой:
#
# «l» (L маленькое);
# «I» (i большое);
# «1» (цифра);
# «o» и «O» (большая и маленькая буквы);
# «0» (цифра).
# Формат входных данных
# На вход программе подаются два числа
# n
# n и
# m
# m, каждое на отдельной строке.
#
# Формат выходных данных
# Программа должна вывести
# n
# n паролей длиной
# m
# m символов в соответствии с условием задачи, каждый на отдельной строке.
#
# Примечание 1. Считать, что числа
# n
# n и
# m
# m всегда таковы, что требуемые пароли сгенерировать возможно.
#
# Примечание 2. В каждом пароле необязательно должна присутствовать хотя бы одна цифра и буква в верхнем и нижнем регистре.
#
# Примечание 3. Решение задачи удобно оформить в виде двух вспомогательных функций:
#
# функция generate_password(length) – возвращает случайный пароль длиной length символов;
# функция generate_passwords(count, length) – возвращает список, состоящий из count случайных паролей длиной length символов.


import string, random

def generate_password(length):
    symbols = string.ascii_uppercase + string.ascii_lowercase + string.digits[2:]
    symbols = ''.join([symbol for symbol in symbols if symbol not in "lIoO"])
    return ''.join(random.sample(symbols, length))

def generate_passwords(count, length):
    return [generate_password(length) for _ in range(count)]

n, m = int(input()), int(input())
print(*generate_passwords(n, m), sep='\n')

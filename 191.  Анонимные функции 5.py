# Напишите функцию is_non_negative_num,
# используя синтаксис анонимных функций, которая принимает строковый аргумент и возвращает значение True,
# если переданный аргумент является неотрицательным числом (целым или вещественным) и False в противном случае.

is_non_negative_num = lambda number: number.replace('.', '', 1).isdigit()

# Напишите функцию is_num, используя синтаксис анонимных функций,
# которая принимает строковый аргумент и возвращает значение True,
# если переданный аргумент является числом (целым или вещественным) и False в противном случае.

is_non_negative_num = lambda q: q.replace('.', '', 1).isdigit()

is_num = lambda q: is_non_negative_num(q[1:]) if q[0] == '-' else is_non_negative_num(q)


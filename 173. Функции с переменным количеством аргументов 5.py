# Напишите функцию print_products(),
# которая принимает произвольное количество аргументов и выводит список продуктов (любая непустая строка) по образцу:
# <номер продукта>) <название продукта> (нумерация продуктов начинается с единицы).
# Если среди переданных аргументов нет ни одного продукта, необходимо вывести текст Нет продуктов.
#
# Примечание 1. Обратите внимание, что функция должна принимать не список, а именно произвольное количество аргументов.
#
# Примечание 2. Числа, списки, кортежи, словари, множества
# и другие нестроковые объекты продуктами не являются и их нужно игнорировать.

def print_products(*args):
    product_list = []
    for product in args:
        if type(product) is str:
            if len(product) > 0:
                product_list.append(product)
    if len(product_list) > 0:
        for num, product in enumerate(product_list, start=1):
            print(str(num) + ')', product)
    else:
        print('Нет продуктов')


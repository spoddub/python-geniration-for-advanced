# На вход программе подается строка натуральных чисел. Из элементов строки формируется список чисел.
#
# Напишите программу сортировки списка чисел в порядке неубывания суммы их цифр.
# При этом, если два числа имеют одинаковую сумму цифр, следует сохранить их взаиморасположение в начальном списке.
#
# Формат входных данных
# На вход программе подается строка текста, содержащая натуральные числа, разделенные пробелами.
#
# Формат выходных данных
# Программа должна вывести отсортированный список чисел в соответствии с условием задачи,
# разделяя его элементы одним пробелом.

string = input().split()


def summing(num):
    n = []
    for i in num:
        n.append(int(i))
    return sum(n)


string.sort(key=summing)
print(*string)

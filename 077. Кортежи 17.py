# Дополните приведенный код так, чтобы он вывел список, содержащий средние арифметические значения чисел
# каждого вложенного кортежа в заданном кортеже кортежей numbers.

numbers = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4), (90, 10))
new_numbers = []
for i in numbers:
    i = list(i)
    new_numbers.append(i)
average_list = []
for i in new_numbers:
    average = 0
    average = sum(i) / len(i)
    average_list.append(average)

print(average_list)

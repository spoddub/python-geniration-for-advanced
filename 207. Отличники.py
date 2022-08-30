# Учитель Тимур проверял контрольные работы по математике в нескольких классах онлайн-школы BEEGEEK
# и решил убедиться, что в каждом классе есть хотя бы один отличник –
# ученик с оценкой 5 по контрольной работе.
# Напишите программу с использованием встроенных функций all(), any() для помощи Тимуру в проверке.

n = int(input())
students = []
for _ in range(n):
    m = int(input())
    temp = []
    for _ in range(m):
        surname, mark = input().split()
        temp.append((surname, int(mark)))
    students.append(temp)

result = all(map(lambda x: any(map(lambda y: y[1] == 5, x)), students))
print('YES' if result else 'NO')

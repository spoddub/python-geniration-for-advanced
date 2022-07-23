# объявление функции
def func(num1, num2):
    s = 'делится'
    s1 = 'не делится'
    if num1 % num2 == 0:
        return s
    else:
        return s1



# считываем данные
num1, num2 = int(input()), int(input())

# вызываем функцию
if func(num1, num2):
    print(True)
else:
    print(False)
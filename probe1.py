x, y = int(input()), int(input())
if x == 'камень' and y == 'ножницы':
    print('Тимур')
elif x == 'ножницы' and y == 'бумага':
    print('Тимур')
elif x == 'бумага' and y == 'камень':
    print('Тимур')
elif x == y:
    print('ничья')
else:
    print('Руслан')

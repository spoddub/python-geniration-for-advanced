# Тимур и Руслан пытаются разделить фронт работы по курсу "Python для профессионалов".
# Для этого они решили сыграть в камень, ножницы и бумагу.
# Помогите ребятам бросить честный жребий и определить, кто будет делать очередной модуль нового курса.
#
# Формат входных данных
# На вход программе подаются две строки текста, содержащие слова "камень", "ножницы" или "бумага".
# На первой строке записан выбор Тимура, на второй – выбор Руслана.
#
# Формат выходных данных
# Программа должна вывести результат жеребьёвки, то есть кто победит: Тимур, Руслан или же они сыграют вничью.
#
# Примечание. Правила игры стандартные: камень побеждает ножницы, но проигрывает бумаге, а ножницы побеждают бумагу.

x, y = input(), input()
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
# На вход программе подается строка, состоящая из трех слов.
# Верно ли, что для записи всех трех слов был использован один и тот же набор букв?
#
# Формат входных данных
# На вход программе подается строка, состоящая из трех слов.
#
# Формат выходных данных
# Программа должна вывести YES, если для записи всех трех слов был использован один и тот же набор букв
# и NO в противном случае.


s = input().split()
if set(s[0]) == set(s[1]) == set(s[2]):
    print('YES')
else:
    print('NO')

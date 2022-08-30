# На вход программе подаются три строки текста с вещественными числами,
# значениями абсцисс (x), ординат (y) и аппликат (z) точек трехмерного пространства.
# Напишите программу для проверки расположения всех точек с введенными координатами
# внутри либо на поверхности шара с центром в начале координат и радиусом R =2.

abscissas = [float(i) for i in input().split()]
ordinates = [float(i) for i in input().split()]
applicates = [float(i) for i in input().split()]

print(all(map(lambda x: x[0]**2+x[1]**2+x[2]**2 <= 4, zip(abscissas, ordinates, applicates))))

# Даны по 10-балльной шкале оценки по математике трех учеников.
# Напишите программу, которая выводит множество оценок, имеющихся у учеников,
# которые встречаются не более, чем у двух из указанных учеников.
#
# Формат входных данных
# На вход программе подаются оценки трех учеников, разделенные символом пробела
# (оценки каждого ученика на отдельной строке).
#
# Формат выходных данных
# Программа должна вывести множество оценок в порядке возрастания на одной строке,
# разделенных пробелами, в соответствии с условием задачи.
#
# Примечание. Оценка ученика находится в диапазоне от 0 до 10 включительно.


set1, set2, set3 = [set([int(i) for i in input().split()]) for k in range(3)]
print(*sorted((set1 | set2 | set3) - (set1 & set2 & set3)))

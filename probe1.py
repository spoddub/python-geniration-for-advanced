n = int(input())
matrix = []
for i in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)

for i in matrix:
    average = 0
    summa = 0
    for j in i:
        average = sum(i) / len(i)
        if average < int(j):
            summa += 1
    print(summa)


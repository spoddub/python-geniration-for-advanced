n = int(input())
matrix = []
for i in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)
summa = 0

for i in range(n):
    summa += matrix[i][i]

print(summa)
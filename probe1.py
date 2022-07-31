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


n, m = map(int, input().split())
matrix = []
counter = 1

for i in range(n):
    matrix.append([])
    for j in range(m):
        matrix[i].append(counter)
        counter += 1

        print(f'{matrix[i][j]}'.ljust(3), end='')
    print()
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

    numbers = ((0, (9, 2)), (1, (4, 6, 3), (5, 2, 3), 8, 3))


tuples = [(10, 20, 40), (40, 50, 60), (70, 80, 90), (10, 90), (1, 2, 3, 4), (5, 6, 10, 2, 1, 77)]
new_tuples = list(tuples)
for i in new_tuples:
    i[-1] = 100


print(new_tuples)
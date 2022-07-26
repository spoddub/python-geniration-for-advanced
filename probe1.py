n, m = int(input()), int(input())
matrix = []
for i in range(n):
    row = []
    for j in range(m):
        row.append(input())
    matrix.append(row)

for r in range(n):
    for c in range(m):
        print(matrix[r][c], end=' ')
    print()

print()

for r in range(m):
    for c in range(n):
        print(matrix[c][r], end=' ')
    print()

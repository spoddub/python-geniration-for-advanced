n = int(input())
virus = 'anton'
for i in range(1, n + 1):
    s = input()
    answer = ''
    for j in virus:
        if j in s:
            
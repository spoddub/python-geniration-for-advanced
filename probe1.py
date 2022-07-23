n = input().split()
total = []
for i in n:
    if i not in total:
        total.append(i)

print(len(total))
string = input().split()


def summing(num):
    n = []
    for i in num:
        n.append(int(i))
    return sum(n), int(num)


string.sort(key=summing)
print(*string)

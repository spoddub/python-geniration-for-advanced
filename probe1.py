import random
res, a = '', 0
for i in range(4):
    a = str(random.randint(0, 255)) + '.'
    res += a
print(res[:-1])

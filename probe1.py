import random

length = int(input())
password = []
for symbol in range(length):
    num = random.randint(1, 2)
    if num == 1:
        password.append(chr(random.randint(65, 90)))
    else:
        password.append(chr(random.randint(97, 122)))
print(*password, sep='')
import random


lottery = set()
for i in range(100):
    if len(lottery) < 7:
        lottery.add(random.randint(1, 49))
    else:
        continue
print(*sorted(lottery))
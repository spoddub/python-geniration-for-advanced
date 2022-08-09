import random

n = int(input())    # количество попыток
for _ in range(n):
    print(random.randint('Орел', 'Решка'))



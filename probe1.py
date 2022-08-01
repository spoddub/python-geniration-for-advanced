poets = [
    ('Тургенев', 14),
    ('Есенин', 13),
    ('Маяковский', 28),
    ('Фет', 15),
    ('Лермонтов', 20)]

for i in range(len(poets)):
    for j in range(i+1, len(poets)):
        if poets[i] > poets[j]:
            poets[i], poets[j] = poets[j], poets[i]

print(poets[0])
print(poets[-1])





n = int(input())

for i in range(n):
    print(input())

myset4 = set((10, 20, 30, 40))
print(myset4)


print(len(set(input())))

s = input().split()
if s[0] == s[1] == s[2]:
    print('YES')
else:
    print('NO')


n = int(input())
for i in range(n):
    print(len(set((input().lower()))))


s = input().split()
num = 0
for i in s:
    if i.lstrip() == num:
        print('YES')
    else:
        print('NO')
    num = i


ms1, ms2 = set(input().split()), set(input().split())
print(ms1)
print(ms2)





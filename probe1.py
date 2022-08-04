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



n = int(input())
names = set(int(input()))
for i in range(n):
    names = names - set(int(input()))
print(*names)



users = [{'name': 'Todd', 'phone': '551-1414', 'email': 'todd@gmail.com'},
         {'name': 'Helga', 'phone': '555-1618', 'email': 'helga@mail.net'},
         {'name': 'Olivia', 'phone': '449-3141', 'email': ''},
         {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@gmail.net'},
         {'name': 'Ruslan', 'phone': '422-145-9098', 'email': 'rus-lan.cha@yandex.ru'},
         {'name': 'John', 'phone': '233-421-32', 'email': ''},
         {'name': 'Lara', 'phone': '+7998-676-2532', 'email': 'g.lara89@gmail.com'},
         {'name': 'Alina', 'phone': '+7948-799-2434', 'email': 'ali.ch.b@gmail.com'},
         {'name': 'Robert', 'phone': '420-2011', 'email': ''},
         {'name': 'Riyad', 'phone': '128-8890-128', 'email': 'r.mahrez@mail.net'},
         {'name': 'Khabib', 'phone': '+7995-600-9080', 'email': 'kh.nurmag@gmail.com'},
         {'name': 'Olga', 'phone': '6449-314-1213', 'email': ''},
         {'name': 'Roman', 'phone': '+7459-145-8059', 'email': 'roma988@mail.ru'},
         {'name': 'Maria', 'phone': '12-129-3148', 'email': 'm.sharapova@gmail.com'},
         {'name': 'Fedor', 'phone': '+7445-341-0545', 'email': ''},
         {'name': 'Tim', 'phone': '242-449-3141', 'email': 'timm.ggg@yandex.ru'}]
for user in users:
    for phone in users[1]:
        if phone.endswith('8'):
            print(users['name'])


users = [{'name': 'Todd', 'phone': '551-1414', 'email': 'todd@gmail.com'},
         {'name': 'Helga', 'phone': '555-1618'},
         {'name': 'Olivia', 'phone': '449-3141', 'email': ''},
         {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@gmail.net'},
         {'name': 'Ruslan', 'phone': '422-145-9098', 'email': 'rus-lan.cha@yandex.ru'},
         {'name': 'John', 'phone': '233-421-32', 'email': ''},
         {'name': 'Lara', 'phone': '+7998-676-2532', 'email': 'g.lara89@gmail.com'},
         {'name': 'Alina', 'phone': '+7948-799-2434'},
         {'name': 'Robert', 'phone': '420-2011', 'email': ''},
         {'name': 'Riyad', 'phone': '128-8890-128', 'email': 'r.mahrez@mail.net'},
         {'name': 'Khabib', 'phone': '+7995-600-9080', 'email': 'kh.nurmag@gmail.com'},
         {'name': 'Olga', 'phone': '6449-314-1213', 'email': ''},
         {'name': 'Roman', 'phone': '+7459-145-8059'},
         {'name': 'Maria', 'phone': '12-129-3148', 'email': 'm.sharapova@gmail.com'},
         {'name': 'Fedor', 'phone': '+7445-341-0545', 'email': ''},
         {'name': 'Tim', 'phone': '242-449-3141', 'email': 'timm.ggg@yandex.ru'}]
names = []
for mail in users:
    if 'email' in mail:
        if mail['email'] == '':
            names.append(mail['name'])
        else:
            continue
    else:
        names.append(mail['name'])

print(*sorted(names))

numbers = {'0': 'zero', '1': 'one', '2': 'two', '3': 'three',
           '4': 'four', '5': 'five', '6': 'six', '7': 'seven',
           '8': 'eight', '9': 'nine'}
letters = []
number = str(input())
for i in number:
    letters.append(numbers[i])
print(*letters)


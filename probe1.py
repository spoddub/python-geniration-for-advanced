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


keys = {
    "CS101": "CS101: 3004, Хайнс, 8:00",
    "CS102": "CS102: 4501, Альварадо, 9:00",
    "CS103": "CS103: 6755, Рич, 10:00",
    "NT110": "NT110: 1244, Берк, 11:00",
    "CM241": "CM241: 1411, Ли, 13:00"
}
number = input()

print(keys[number])


keyboard = {
    ".": '1', ",": '11', "?": '111', "!": '1111', ":": '11111',
    "A": '2', "B": '22', "C": '222',
    "D": '3', "E": '33', "F": '333',
    "G": '4', "H": '44', "I": '444',
    "J": '5', "K": '55', "L": '555',
    "M": '6', "N": '66', "O": '666',
    "P": '7', "Q": '77', "R": '777', "S": '7777',
    "T": '8', "U": '88', "V": '888',
    "W": '9', "X": '99', "Y": '999', "Z": '9999',
    " ": '0'
}
message = input().upper()

output = []

for key in message:
    output.append(keyboard[message])

print(*output)


result = {}
for i in range(1, 15):
    result = result.setdefault(i, i * i)
print(result)
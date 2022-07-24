my_list = []
n = int(input())
for i in range(1, n + 1):
    my_list.append(i)
my_list = [my_list] * n
print(*my_list, sep='\n')

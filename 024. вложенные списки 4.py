# Дополните приведенный код так, чтобы список list1 имел вид:
#
# list1 = [[8, 7, 1], [102, 7, 9], [105, 106, 102], [103, 98, 99, 100], [3, 2, 1]]

list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
for i in list1:
    i = i.reverse()


print(list1)
# Дополните приведенный код, так чтобы получить список,
# содержащий только непустые кортежи исходного списка tuples, не меняя порядка их следования.


tuples = [(), (), ('',), ('a', 'b'), (), ('a', 'b', 'c'), (1,), (), (), ('d',), ('', ''), ()]
non_empty_tuples = []
for i in tuples:
    if len(i) > 0:
        non_empty_tuples.append(i)

print(non_empty_tuples)

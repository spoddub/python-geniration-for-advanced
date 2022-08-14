def sq_sum(*args):
    sp = []
    for i in args:
        sp.append(i ** 2)
    return sum(sp)

print(sq_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
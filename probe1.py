def mean(*args):
    sp = []
    for i in args:
        if type(i) in (int, float):
            sp.append(i)
    return sum(sp) / len(sp)
def greet(*args):
    sp = []
    for i in args:
        sp.append(i)
    for i in sp:
        if len(sp) > 1:
            return 'Hello,', *sp,

def map(function, items):
    result = []
    for item in items:
        result.append(function(item))
    return result

numbers = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.12013, 23.22222, 90.09873, 45.45, 314.1528, 2.71828,
           1.41546]


def rounding(items):
    res = []
    for number in items:
        res.append(round(number, 2))
    return res


print(map(rounding, numbers))


from math import sqrt
points = [(-1, 1), (5, 6), (12, 0), (4, 3), (0, 1), (-3, 2), (0, 0), (-1, 3), (2, 0), (3, 0), (-9, 1), (3, 6), (8, 8)]
def distance(a):
    point = (a[0] ** 2 + a[1] ** 2)
    point = sqrt(point)
    return point

print(sorted(points, key=distance))

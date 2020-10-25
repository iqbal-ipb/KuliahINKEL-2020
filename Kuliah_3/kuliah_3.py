import math


def rata(a):
    jumlah = 0
    rata = 0
    for i in a:
        jumlah = jumlah + i
    rata = jumlah / len(a)
    return rata


def sd(a):
    jumlah = 0
    rata2 = rata(a)
    for i in a:
        jumlah = jumlah + (i - rata2)**2
    return math.sqrt(jumlah/len(a)-1)


def maksimal(a):
    return max(a)


def minimal(a):
    return min(a)


c = [21, 30, 29, 16, 27, 12, 3, 12, 34]
print(rata(c))
print(sd(c))

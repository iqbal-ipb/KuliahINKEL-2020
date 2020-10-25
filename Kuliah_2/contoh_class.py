from contoh.statistikku import stats

data = [1, 2, 3, 4, 5, 6, 7]
data2 = [1, 2, 3, 4, 5, 6, 7]

halo = stats(data)
halo2 = stats(data2)
print(halo.sd())
print(halo.rata())

print(halo2.sd())
print(halo2.rata())

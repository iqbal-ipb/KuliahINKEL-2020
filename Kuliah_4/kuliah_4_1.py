
f = open('pandas_tutorial_read.csv', 'r')
baris = f.readline()
baris = baris.rstrip('\n')
baris = baris.split(';')
print(baris)

baris[0]

for line in f:
    print(line)


filename = "pandas_tutorial_read.csv"
filehandle = open(filename, 'r')
while True:
    # baca setiap baris
    line = filehandle.readline()
    if not line:
        break
    print(line)

filehandle.close()

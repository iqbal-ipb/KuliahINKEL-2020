
try:
    n = int(input("Mohon masukan angka: "))
    print("terima kasih, yang dimasukan integer")
except:
    print("yang dimasukan bukan integer")


while True:
    try:
        n = input("Masukan angka Integer: ")
        n = int(n)
        break
    except ValueError:
        print("No valid integer! coba lagi ...")
print("Anak ganteng, terima kasih sudah memasukan nilai Integer!")


try:
    f = open('pandas_tutorial_read.csv')
    baris = f.readline()
    baris = baris.rstrip('\n')
    baris = baris.split(';')
    i = int(baris[1])
except (IOError, ValueError):
    print("An I/O error or a ValueError occurred")
except:
    print("An unexpected error occurred")
    raise

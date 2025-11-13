
# Data
a = []
while True:
    t1 = int(input("Masukkan nilai 1: "))
    t2 = int(input("Masukkan nilai 2: "))
    if t1 == 0 and t2 == 0:
        break
    elif t1 == 0 or t2 == 0:
        print("Masukkan kedua elemen!")
        continue
    else:
        a.append(t1)
        a.append(t2)

b =[]
for angka in a:
    if angka not in b:
        b.append(angka)

n = len(b)
for i in range(n):
    for j in range(0, n - i - 1):
        if b[j] < b[j + 1]:
            # tukar posisi menggunakan temp
            temp = b[j]
            b[j] = b[j + 1]
            b[j + 1] = temp
hasil = tuple(b)

print(hasil)

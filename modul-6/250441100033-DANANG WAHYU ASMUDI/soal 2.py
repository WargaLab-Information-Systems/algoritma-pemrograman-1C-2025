t1 = (3, 1, 4)
t2 = (1, 5, 9)

gabungan = t1 + t2

hasil = []
for angka in gabungan:
    if angka not in hasil:
        hasil.append(angka)

n = len(hasil)
for i in range(n - 1):
    for j in range(n - i - 1):
        if hasil[j] < hasil[j + 1]:
            hasil[j], hasil[j + 1] = hasil[j + 1], hasil[j]

hasil_akhir = tuple(hasil)

print(hasil_akhir)

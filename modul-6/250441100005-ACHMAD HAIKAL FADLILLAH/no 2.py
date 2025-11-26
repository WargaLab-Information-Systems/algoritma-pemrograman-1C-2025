# t1 = (3, 1, 4)
# t2 = (1, 5, 9)
t1 = input("masukkan beberapa angka: ")
t2 = input("masukkan beberapa angka: ")
gabung = t1 + t2

tanpa_duplikat = []
for angka in gabung:
    if angka not in tanpa_duplikat:
        tanpa_duplikat.append(angka)

for i in range(len(tanpa_duplikat)):
    for j in range(0, len(tanpa_duplikat) - i - 1):
        if tanpa_duplikat[j] < tanpa_duplikat[j + 1]:
            tanpa_duplikat[j], tanpa_duplikat[j + 1] = tanpa_duplikat[j + 1], tanpa_duplikat[j]

hasil_akhir = tuple(tanpa_duplikat)

print("Tuple pertama :", t1)
print("Tuple kedua   :", t2)
print("Hasil akhir   :", hasil_akhir)

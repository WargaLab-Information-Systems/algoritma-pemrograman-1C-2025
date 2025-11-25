#soal2
t1 = (3, 1, 4)
t2 = (1, 5, 9)
# gabungkan tuple
gabung = t1 + t2
# hapus angka duplikat tapi urutan tetap
tanpa_duplikat = []
for angka in gabung:
    if angka not in tanpa_duplikat:
        tanpa_duplikat.append(angka)
#pake bubble sort
for i in range(len(tanpa_duplikat)):
    for j in range(len(tanpa_duplikat) - 1):
        if tanpa_duplikat[j] < tanpa_duplikat[j + 1]:
            sementara = tanpa_duplikat[j]
            tanpa_duplikat[j] = tanpa_duplikat[j + 1]
            tanpa_duplikat[j + 1] = sementara
# ubah ke tuple
hasil_akhir = tuple(tanpa_duplikat)
print("Hasil akhir:", hasil_akhir)
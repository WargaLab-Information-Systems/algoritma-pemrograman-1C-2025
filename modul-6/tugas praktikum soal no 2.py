def gabung_dan_urutkan(t1, t2):
    # Gabungkan tuple
    gabungan = t1 + t2
    
    # Hapus duplikat
    tanpa_duplikat = []
    for angka in gabungan:
        if angka not in tanpa_duplikat:
            tanpa_duplikat.append(angka)
    
    # Sorting manual (terbesar ke terkecil)
    n = len(tanpa_duplikat)
    for i in range(n):
        for j in range(0, n - 1):
            if tanpa_duplikat[j] < tanpa_duplikat[j + 1]:
                tanpa_duplikat[j], tanpa_duplikat[j + 1] = tanpa_duplikat[j + 1], tanpa_duplikat[j]
    
    return tuple(tanpa_duplikat)

# Input dan output
t1 = tuple(map(int, input("Tuple pertama: ").split()))
t2 = tuple(map(int, input("Tuple kedua: ").split()))
print("Hasil:", gabung_dan_urutkan(t1, t2))
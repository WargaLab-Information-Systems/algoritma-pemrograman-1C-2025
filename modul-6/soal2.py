def gabung_tuple(t1, t2):
    # Gabungkan kedua tuple jadi satu list
    gabungan = (t1 + t2)

    # Hapus angka yang sama (duplikat), urutan pertama dipertahankan
    unik = []
    for angka in gabungan:
        if angka not in unik:
            unik.append(angka)

    # Urutkan manual secara menurun (descending)
    for i in range(len(unik)): 
        for j in range(i + 1, len(unik)):
            if unik[i] < unik[j]:  # tukar posisi jika elemen kiri lebih kecil
                unik[i], unik[j] = unik[j], unik[i]

    # Kembalikan hasil dalam bentuk tuple
    return (unik)


# Contoh penggunaan
t1 = (3, 1, 4)
t2 = (1, 5, 9)
hasil = gabung_tuple(t1, t2)
print("Hasil akhir:", hasil)
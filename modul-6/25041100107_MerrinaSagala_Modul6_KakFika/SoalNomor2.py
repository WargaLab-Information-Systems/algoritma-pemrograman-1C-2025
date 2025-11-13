def gabung_tuple(t1, t2):
    # Gabungkan kedua tuple menjadi satu list
    gabung = list(t1 + t2)

    # Hapus duplikat, tapi urutan aslinya tetap dipertahankan
    unik = []
    for angka in gabung:
        if angka not in unik:
            unik.append(angka)

    #  Urutkan secara menurun (descending) tanpa sorted()
    for i in range(len(unik)):
        for j in range(i + 1, len(unik)):
            if unik[i] < unik[j]:  # kalau elemen sekarang lebih kecil → tukar
                unik[i], unik[j] = unik[j], unik[i]

    #  Kembalikan hasil dalam bentuk tuple
    return tuple(unik)


# -------Contoh penggunaan
t1 = (3, 1, 4)
t2 = (1, 5, 9)

hasil = gabung_tuple(t1, t2)
print(hasil)

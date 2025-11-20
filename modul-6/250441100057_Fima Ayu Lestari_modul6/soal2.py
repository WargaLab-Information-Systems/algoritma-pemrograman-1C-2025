def gabung_tuple(t1, t2):
    gabung = t1 + t2
    hasil = []

    for x in gabung:
        if x not in hasil:
            hasil.append(x)

    for i in range(len(hasil)):
        for j in range(i + 1, len(hasil)):
            if hasil[i] < hasil[j]:
                hasil[i], hasil[j] = hasil[j], hasil[i]

    return tuple(hasil)

t1 = tuple(int(x) for x in input("Masukkan angka tuple pertama: ").split())
t2 = tuple(int(x) for x in input("Masukkan angka tuple kedua: ").split())
print("Hasil akhir:", gabung_tuple(t1, t2))

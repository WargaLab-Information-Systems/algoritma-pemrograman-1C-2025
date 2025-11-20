def gabung_dan_urutkan(t1, t2):
    gabungan = t1 + t2

    tanpa_duplikat = []
    for angka in gabungan:
        if angka not in tanpa_duplikat:
            tanpa_duplikat.append(angka)

    for i in range(len(tanpa_duplikat)):
        for j in range(i + 1, len(tanpa_duplikat)):
            if tanpa_duplikat[i] < tanpa_duplikat[j]:
                tanpa_duplikat[i], tanpa_duplikat[j] = tanpa_duplikat[j], tanpa_duplikat[i]

    return tuple(tanpa_duplikat)

print("=== Program Gabung dan Urutkan Tuple Mac Allister ===")
input1 = input("Masukkan angka untuk tuple 1 (pisahkan dengan spasi): ") 
input2 = input("Masukkan angka untuk tuple 2 (pisahkan dengan spasi): ")    

list1 = []
for angka in input1.split():
    list1.append(int(angka))

list2 = []
for angka in input2.split():
    list2.append(int(angka))

t1 = tuple(list1)
t2 = tuple(list2)

hasil = gabung_dan_urutkan(t1, t2)

print("Hasil akhir (urut menurun, tanpa duplikat):", hasil)

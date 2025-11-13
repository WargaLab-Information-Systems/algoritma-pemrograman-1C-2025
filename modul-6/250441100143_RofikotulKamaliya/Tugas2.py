def input_tuple(nama):
    while True:
        try:
            data = input(f"Masukkan elemen {nama} (pisahkan dengan spasi): ").strip()
            tup = tuple(map(int, data.split()))
            if not tup:
                print("Data tidak boleh kosong. Coba lagi.")
                continue
            return tup
        except ValueError:
            print("Input tidak valid! Pastikan hanya memasukkan angka, pisahkan dengan spasi.\n")
t1 = input_tuple("tuple pertama")
t2 = input_tuple("tuple kedua")
gabungan = t1 + t2
duplikat = []
for angka in gabungan:
    if angka not in duplikat:
        duplikat.append(angka)

for i in range(len(duplikat)):
    for j in range(i + 1, len(duplikat)):
        if duplikat[i] < duplikat[j]:
            duplikat[i], duplikat[j] = duplikat[j], duplikat[i]
hasil = tuple(duplikat)
print("\nHasilnya adalah:")
print(hasil)
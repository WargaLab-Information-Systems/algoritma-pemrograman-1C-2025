# Program Gabung Dua Tuple tanpa Duplikat dan Urut Menurun (tanpa sorted, pakai input)

# Input data tuple pertama
t1_input = input("Masukkan angka-angka untuk tuple pertama (pisahkan dengan spasi): ")
t1 = tuple(map(int, t1_input.split()))

# Input data tuple kedua
t2_input = input("Masukkan angka-angka untuk tuple kedua (pisahkan dengan spasi): ")
t2 = tuple(map(int, t2_input.split()))

# Gabungkan kedua tuple
gabung = t1 + t2

# Hapus angka duplikat, urutan tetap seperti kemunculan pertama
hasil_unik = []
for angka in gabung:
    if angka not in hasil_unik:
        hasil_unik.append(angka)

# Urutkan secara manual dari terbesar ke terkecil (descending)
for i in range(len(hasil_unik)):
    for j in range(i + 1, len(hasil_unik)):
        if hasil_unik[i] < hasil_unik[j]:
            hasil_unik[i], hasil_unik[j] = hasil_unik[j], hasil_unik[i]

# Ubah menjadi tuple kembali
hasil_akhir = tuple(hasil_unik)

# Tampilkan hasil akhir
print("Tuple hasil akhir:", hasil_akhir)

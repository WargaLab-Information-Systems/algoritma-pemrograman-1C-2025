# soal 1

harga_per_buku = 5000
harga_per_pensil = 4500
pajak = 0.10

total_harga = harga_per_buku * 3 + harga_per_pensil * 2
total_pajak = total_harga * pajak
total_harga_setelah_pajak = total_harga+ total_pajak
print("Total harga yang harus dibayar: Rp", int (total_harga_setelah_pajak))

# soal 2
panjang = input("Masukkan panjang nilai panjang balok: ")
lebar = input("Masukkan nilai lebar balok: ")
tinggi = input("Masukkan nilai tinggi balok: ")

volume = int(panjang) * int(lebar) * int(tinggi)
luas_permukaan = 2 * (int(panjang) * int(lebar) + int(panjang) * int(tinggi) + int(lebar) * int(tinggi))

print("Volume balok adalah:", volume, "cm")
print("Luas permukaan balok adalah:", luas_permukaan, "cm")

# soal 3
bola_merah = input("Masukkan 8 bola merah: ")
bola_biru = input("Masukkan 6 bola biru: ")

total_bola = int(bola_merah) + int(bola_biru)
diAmbil = 3

#rumus kombinasi itu c(total, diAmbil) = total! / (diAmbil! * (total - diAmbil)!) = 14! / (3! * (14 - 3)!)
kombinasi =  14 * 13 * 12 // (3 * 2 * 1) # 14! / (3! * (14 - 3)!) = 14! / (3! * 11!) = 14 * 13 * 12 / (3 * 2 * 1) Jadi 11! di coret
print("Jumlah cara memilih 3 bola secara acak adalah:", kombinasi)
#Cara ini hanya untuk menghitung kombinasi 14 diambil 3, jika ingin menghitung kombinasi lain harus diubah rumusnya
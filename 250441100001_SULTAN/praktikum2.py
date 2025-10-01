#data belanja
# harga_buku = 5000
# harga_pensil = 4500
# jumlah_buku = 3
# jumlah_pensil = 2

# total_buku = harga_buku * jumlah_buku
# total_pensil = harga_pensil * jumlah_pensil
# total_harga_semua_barang = total_buku + total_pensil

# #pajak 10%
# pajak = total_harga_semua_barang * 10//100

# total_setelah_pajak = total_harga_semua_barang + pajak

# print("==== Hasil Perhitungan Belanja ===")
# print("Total sebelum pajak:", total_harga_semua_barang)
# print("Pajak (10%):", pajak)
# print("Total yang harus dibayar:", total_setelah_pajak)

# # Soal 2: Menghitung volume dan luas permukaan balok

# # Input dari user
# p = int(input("Masukkan panjang balok (cm): "))
# l = int(input("Masukkan lebar balok (cm): "))
# t = int(input("Masukkan tinggi balok (cm): "))

# Hitung volume
# p = int(input("Masukkan panjang balok (cm): "))
# l = int(input("Masukkan lebar balok (cm): "))
# t = int(input("Masukkan tinggi balok (cm): "))

# # Hitung volume
# volume = p * l * t

# # Hitung luas permukaan
# luas_permukaan = 2 * ((p * l) + (p * t) + (l * t))

# print("=== Hasil Perhitungan Balok ===")
# print("Volume balok:", volume, "cm^3")
# print("Luas permukaan balok:", luas_permukaan, "cm^2")


# Soal 3: Menghitung kombinasi pengambilan bola

# Soal 3: Menghitung kombinasi bola
Total_bola = 8 + 6
Diambil = 3

#Input dari user
a = int(input("Masukkan jumlah total bola: "))
b = int(input("Masukkan jumlah bola yang diambil: "))

# Faktorial  (14)
faktorial_jumlah_bolabiru_bolamerah = 14 * 13 * 12 * 11 * 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1
# Faktorial  (3)
faktorial_bola_terambil = 3 * 2 * 1
# Faktorial (n - r) = 11
faktorial_nr = 11 * 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1

# Rumus kombinasi
kombinasi = faktorial_jumlah_bolabiru_bolamerah // (faktorial_bola_terambil * faktorial_nr)

print("Jumlah kemungkinan kombinasi bola:", kombinasi)



# Soal 1

# Harga satuan barang
harga_buku = 5000
harga_pensil = 4500

# Julah barang yang dibeli
jumlah_buku = 3
jumlah_pensil = 2

# Hitung total harga sebelum pajak
total_sebelum_pajak = (harga_buku * jumlah_buku) + (harga_pensil * jumlah_pensil)

# Hitung pajak 10%
pajak = total_sebelum_pajak * 0.10

# Total setelah pajak
total_setelah_pajak = total_sebelum_pajak + pajak

# Hasil
print("TOTAL harga sebelum pajak : Rp", total_sebelum_pajak)
print("Pajak 10%                 : Rp", int(pajak))
print("Total yang harus dibayar  : Rp", int(total_setelah_pajak))


# Soal 2

# Program menghitung volume dan luas permukaan balok

# Input dari user 
panjang = int(input("Masukkan panjang balok (cm): "))
lebar = int(input("Masukkan lebar balok (cm) "))
tinggi = int(input("Masukkan tinggi balok (cm): "))

# Hitung volume
volume = panjang * lebar * tinggi

# Hitung luas permukaan 
luas_permukaan = ((panjang * lebar) + (panjang * tinggi) + (lebar * tinggi))

# Tampilkan hasil
print("\n=== Hasil Perhitungan Balok ===")
print("Volume balok        :", volume, "cm³")
print("Luas permukaan balok:", luas_permukaan, "cm²")


# Soal 3
import math

# Program menghitung kombinasi pengambilan bola

# Jumlah bola
bola_merah = 8
bola_biru = 6
total_bola = bola_merah + bola_biru

# Banyak bola yang diambil
ambil = 3

# Hitung kombinasi dengan rumus C(n, r)
kombinasi = math.comb(total_bola, ambil)

# Tampilkan hasil
print("=== Perhitungan Kombinasi Bola ===")
print(f"Jumlah bola merah : {bola_merah}")
print(f"Jumlah bola biru  : {bola_biru}")
print(f"Total bola        : {total_bola}")
print(f"Jumlah bola yang diambil: {ambil}")
print(f"Banyak kemungkinan kombinasi = {kombinasi}")

# Program menghitung kombinasi pengambilan bola secara dinamis

# Input jumlah bola dari pengguna
bola_merah = int(input("Masukkan jumlah bola merah: "))
bola_biru = int(input("Masukkan jumlah bola biru: "))
r = int(input("Masukkan jumlah bola yang diambil: "))

# Hitung total bola
total_bola = bola_merah + bola_biru

# Hitung pembilang dengan operator aritmatika (* dan -)
pembilang = total_bola * (total_bola - 1) * (total_bola - 2)

# Hitung penyebut dengan operator aritmatika (* dan -)
penyebut = r * (r - 1) * (r - 2)

# Hitung kombinasi dengan operator pembagian (/)
kombinasi = pembilang / penyebut

# Tampilkan hasil
print("\n=== Hasil Perhitungan Kombinasi ===")
print("Total bola:", total_bola)
print("Jumlah bola yang diambil:", r)
print("Jumlah kombinasi yang mungkin:", kombinasi)

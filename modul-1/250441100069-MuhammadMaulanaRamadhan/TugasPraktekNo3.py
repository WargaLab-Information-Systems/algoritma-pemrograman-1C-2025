import math

# input jumlah bola
bola_merah = int(input("Masukkan bola merah: "))
bola_biru = int(input("Masukkan bola biru: "))
k = int(input("Masukkan jumlah yang diambil: "))

n = bola_merah + bola_biru

# hitung kombinasi
kombinasi = math.factorial(n) // (math.factorial(k) * math.factorial(n - k))

# hasil
print("Banyak kemungkinan kombinasi bola yang dapat diambil adalah:", kombinasi)

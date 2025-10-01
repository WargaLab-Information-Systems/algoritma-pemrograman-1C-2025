import math

# total bola 
bola_merah = 8
bola_biru = 6
n = bola_merah + bola_biru

# ambil bola
k = 3

# Hitung kombinasi
kombinasi = math.factorial(n) // (math.factorial(k) * math.factorial(n - k))

# hasil
print("Banyak kemungkinan kombinasi bola yang dapat diambil adalah:", kombinasi)
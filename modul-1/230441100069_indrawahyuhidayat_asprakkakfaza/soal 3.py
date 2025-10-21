
import math

# Fungsi menghitung kombinasi C(n, r)
def kombinasi(n, r):
    return math.comb(n, r)  # Untuk Python 3.8 ke atas

# Total bola: 8 merah + 6 biru
total_bola = 8 + 6
jumlah_diambil = 3

# Hitung banyak kombinasi
hasil = kombinasi(total_bola, jumlah_diambil)

# Tampilkan hasil
print(f"Banyak kombinasi pengambilan 3 bola dari 14 bola adalah: {hasil}")

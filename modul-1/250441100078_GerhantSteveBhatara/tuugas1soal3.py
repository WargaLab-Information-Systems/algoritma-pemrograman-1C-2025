# # Soal 3

# # Program menghitung kombinasi pengambilan bola

# # Jumlah bola 
# bola_merah = int(input("Masukkan angka bola merah:"))
# bola_biru = int(input("Masukkan angka bola biru:"))
# total_bola = bola_merah + bola_biru

# # Banyak bola yang diambil
# ambil = int(input("Masukkan bola yang diambil:"))

# # Hitung kombinasi dengan rumus C(n, r)
# numerator = total_bola * (total_bola-1) * (total_bola-2)
# denominator = ambil * (ambil-1) * (ambil-2)

# kombinasi = numerator//denominator
# ()
# # Tampilkan hasil
# print("Jumlah bola merah :", bola_merah)
# print("Jumlah bola biru  :", bola_biru)
# print("Total bola        :", total_bola)
# print("Jumlah bola yang diambil:", ambil)
# print("Banyak kemungkinan kombinasi =", kombinasi)
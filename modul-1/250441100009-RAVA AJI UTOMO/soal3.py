#menghitung berapa banyak kemungkinan kombinasi bola yang di ambil
bola_merah = 3 #jumlah bola merah
bola_biru = 3 #jumlah bola biru
bola_acak_diambil = 3 #jumlah bola yang diambil
total_bola = bola_merah + bola_biru #total bola
kombinasi = (total_bola * (total_bola - 1) * (total_bola - 2)) / (bola_acak_diambil * (bola_acak_diambil - 1) * (bola_acak_diambil - 2)) #rumus kombinasi   
print("Banyak kemungkinan kombinasi bola yang diambil adalah:", kombinasi) #mencetak hasil kombinasi
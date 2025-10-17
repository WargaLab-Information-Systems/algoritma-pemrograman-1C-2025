merah = int(input("Masukkan jumlah bola merah : "))
biru = int(input("Masukkan jumlah bola biru : "))
ambil = int(input("Masukkan total ambil bola : "))
total_bola = merah + biru
total_ambil= ambil

pembilang = total_bola   * (total_bola - 1) * (total_bola - 2)
penyebut = total_ambil * (total_ambil-1) * (total_ambil-2)
kombinasi = pembilang // penyebut

print("Jumlah kemungkinan kombinasi:",(kombinasi))



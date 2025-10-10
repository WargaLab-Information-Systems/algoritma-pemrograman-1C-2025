# # Soal1
# buku_tulis = 5000
# pensil = 4500
# total_buku_tulis = 3
# total_pensil = 2
# total_harga_buku_tulis = buku_tulis * total_buku_tulis
# total_harga_pensil = pensil * total_pensil
# total_belanja = total_harga_buku_tulis + total_harga_pensil
# print("Total belanja adalah Rp", total_belanja)
# pajak_pembelian = total_belanja * 0.10
# total_belanja_setelah_pajak = total_belanja + pajak_pembelian
# print("Total belanja setelah pajak adalah Rp", total_belanja_setelah_pajak)

# # Soal2
# panjang = int(input("Masukkan panjang balok: "))
# lebar = int(input("Masukkan lebar balok: "))
# tinggi = int(input("Masukkan tinggi balok: "))
# volume = panjang * lebar * tinggi
# luas_permukaan = 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)
# print("Volume balok adalah:", volume)
# print("Luas permukaan balok adalah:", luas_permukaan)

# Soal3
bola_merah = 8
bola_biru = 6
bola_acak = 3
total_bola = bola_merah + bola_biru
# rumus kombinasi:C(n,r) = n! / (r! * (n-r)!)
# r = 3
# C(n,3) = n * (n-1) * (n-2) / (3 * (r-1) * (r-2))
hitung_kombinasi = total_bola * (total_bola - 1) * (total_bola - 2) / (3 * (3 - 1) * (3 - 2))
print("Total kombinasi pengambilan 3 bola adalah:", hitung_kombinasi)
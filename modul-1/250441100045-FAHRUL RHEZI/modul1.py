#Modul 1 Praktikum
#Soal 1
harga_buku_tulis = 5000
harga_pensil = 4500
pajak = 0.10
j_buku_tulis = 3
j_pensil = 2

j_harga_buku_tulis = harga_buku_tulis * j_buku_tulis
j_harga_pensil = harga_pensil * j_pensil
total_biaya = j_harga_buku_tulis + j_harga_pensil
biaya_pajak = total_biaya * pajak
setelah_pajak = total_biaya + biaya_pajak

print(f"total biaya: Rp.{total_biaya}")
print(f"pajak 10%: Rp.{biaya_pajak}")
print(f"total biaya : Rp.{setelah_pajak}")

#Soal 2
panjang = int(input("Masukkan panjang : "))   #10
lebar = int(input("Masukkan lebar : "))    #6  
tinggi = int(input("Masukkan tinggi : "))  #4

volume = panjang * lebar * tinggi
luas_permukaan = 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)
print(f"Volume Balok : {volume}cm³")
print(f"Luas Permukaan Balok : {luas_permukaan}cm")

#Soal 3
bola_merah = int(input("masukkan jumlah bola merah: "))   #8
bola_biru = int(input("masukkan jumlah bola biru: "))    #6
a = int(input("jumlah bola yang diambil: "))   #3
tb = bola_merah + bola_biru


numerator = tb * (tb-1) * (tb-2)
denominator = a * (a-1) * (a-2)
kombinasi = numerator // denominator

print(f"jumlah bola merah: {bola_merah}")
print(f"jumlah bola biru: {bola_biru}")
print(f"total bola: {tb}")
print(f"jumlah bola yang diambil: {a}")
print(f"dumerator: {numerator}")
print(f"denominator: {denominator}")
print(f"kemungkinan kombinasi: {kombinasi}")
#SOAL NOMOR 1
Harga Barang
harga_buku = 5000
jumlah_buku = 3
harga_pensil = 4500
jumlah_pensil = 2

#Total harga barang sebelum pajak
total_harga = (harga_buku*jumlah_buku) + (harga_pensil*jumlah_pensil)

#Pajak 10%
pajak = total_harga * 0.10

#Total bayar
total_bayar = total_harga + pajak

print ("total belanja sebelum pajak:", total_harga)
print ("pajak 10% :, pajak")
print ("total yang harus dibayar ;", total_bayar)

#SOAL NOMOR 2
panjang = int(input("masukkan panjang balok (cm):"))
lebar = int(input("Masukkan lebar balok(cm):"))
tinggi = int(input("Masukkan tinggi balok (cm):"))

#Menghitung Volume 
volume = panjang*lebar*tinggi
#Menghitung Luas permukaan
luas_permukaan = 2*((panjang*lebar) + (panjang*tinggi) + (lebar*tinggi) )

print ("Hasil perhitungan Balok:")
print ("Volume balok:", volume, "cm³")
print ("Luas permukaan balok:", luas_permukaan, "cm²")




# SOAL NOMOR 3
#tb : total bola
#a : Jumlah bola yang diambil
tb = int(input("Masukkan total bola :"))
a = int (input("Masukkan jumlah bola yang diambil"))

numerator = tb* (tb-1)* (tb-2)
denominator = a* (a-1)* (a-2)

kombinasi = numerator//denominator

print (f"dumerator :{numerator}")
print (f"denominator:{denominator}")

print (f"kemungkinan kombinasi:{kombinasi}")

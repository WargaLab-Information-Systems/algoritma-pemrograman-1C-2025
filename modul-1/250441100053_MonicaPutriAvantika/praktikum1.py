AS 1

#harga satuan
harga_buku = 5000
harga_pensil = 4500
#jumlah barang yang di beli
jumlah_buku = 3
jumlah_pensil = 2
#hitung total harga sebelum pajak
total_harga = (harga_buku * jumlah_buku)+(harga_pensil*jumlah_pensil)

#hitung pajak 10% 
pajak = total_harga*0.10

#hitung total yang harus dibayar
total_bayar = total_harga + pajak

print("total harga sebelum pajak:Rp", total_harga)
print("pajak(10%):Rp",int(pajak))
print("total yang harus dibayar:Rp", int(total_bayar))#TUG

#TUGAS 2


panjang =int(input("masukkan panjang balok(cm): ")) 
lebar = int(input("masukkan lebar balok(cm): "))
tinggi =int(input("masukkan tinggi balok(cm): "))

#hitung volume
volume = panjang * lebar * tinggi

#hitung luas permukaan
luas_permukaan = 2*(panjang * lebar + panjang * tinggi + lebar * tinggi )

#tampilkan hasil
print("Hasil perhitungan.")
print("volume balok =", volume, "cm")
print("luas permukaan balok=", luas_permukaan, "cm")


#TUGAS 3
# tb: total bola
# a: jumlah bola yang diambil

tb_merah = int(input("masukkan total bola merah: "))
tb_biru = int(input("masukkan total bola biru: "))
tb = tb_merah + tb_biru
a= int(input("jumlah bola yang diambil: "))
numerator = tb * (tb-1) * (tb-2)        
denominator = a * (a-1) * (a-2)      

kombinasi = numerator // denominator

print(f"dumerator: {numerator}")
print(f"denominator: {denominator}")
print(f"kemungkinan kombinasi: {kombinasi}")
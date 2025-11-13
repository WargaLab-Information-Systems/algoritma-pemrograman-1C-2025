#===TUGAS1====
# Harga satuan
harga_buku = 5000
harga_pensil = 4500

# Jumlah barang yang dibeli
jumlah_buku = 3
jumlah_pensil = 2

# Hitung total harga sebelum pajak
total_harga_barang = (harga_buku * jumlah_buku) + (harga_pensil * jumlah_pensil)

# Hitung pajak 10%
pajak = 0.10 * total_harga_barang

# Total yang harus dibayar
total_bayar = total_harga_barang + pajak

# Tampilkan hasil
print("Total harga barang sebelum pajak: Rp", total_harga_barang)
print("Pajak (10%): Rp", int(pajak))
print("Total yang harus dibayar: Rp", int(total_bayar))

#====TUGAS2====
# Ukuran balok
panjang = int(input("masukkan panjang"))
lebar = int(input("masukkan lebar"))
tinggi = int(input("masukkan tinggi"))

# Hitung volume
volume = panjang * lebar * tinggi

# Hitung luas permukaan
luas_permukaan = 2 * ((panjang * lebar) + (panjang * tinggi) + (lebar * tinggi))

# Tampilkan hasil
print("Volume balok:", volume, "cm³")
print("Luas permukaan balok:", luas_permukaan, "cm²")

#===TUGAS3===
# tb = total bola
# a: jumlah bola yang di ambil
tb = int(input("Masukkan total bola: ")) 
a = int(input("Masukkan jumlah bola yang diambil: "))

numerator = tb * (tb-1) * (tb-2)
denominator = a * (a-1) * (a-2)
kombinasi= numerator // denominator

print(f"dumerator: {numerator}")
print(f"dumerator: {denominator}")
print(f"kemungkinan kombinasi: {kombinasi}")
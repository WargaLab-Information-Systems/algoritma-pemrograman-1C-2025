# Harga dan jumlah barang
harga_buku = 5000
jumlah_buku = 3
harga_pensil = 4500
jumlah_pensil = 2

# Total harga barang sebelum pajak
total_harga = (harga_buku * jumlah_buku) + (harga_pensil * jumlah_pensil)

# Pajak 10%
pajak = total_harga * 0.10

# Total bayar
total_bayar = total_harga + pajak

print("Total belanja sebelum pajak:", total_harga)
print("Pajak 10%:", pajak)
print("Total yang harus dibayar:", total_bayar)
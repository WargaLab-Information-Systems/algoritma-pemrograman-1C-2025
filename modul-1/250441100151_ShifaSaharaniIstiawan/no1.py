# soal 1
# Harga satuan masing-masing barang
harga_buku = 5000
harga_pensil = 4500

# Jumlah barang yang mau dibeli
jumlah_buku = 3
jumlah_pensil = 2

# Hitung total harga sebelum pajak
total_harga = (harga_buku * jumlah_buku) + (harga_pensil * jumlah_pensil)

# Pajak 10%
pajak = 0.10 * total_harga

# Total harga setelah pajak
total_bayar = total_harga + pajak
print("Total harga sebelum pajak: Rp", total_harga)
print("Pajak 10%: Rp", pajak)
print("Total yang harus dibayar: Rp", total_bayar)


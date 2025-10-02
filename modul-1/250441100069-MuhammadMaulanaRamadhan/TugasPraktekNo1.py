# harga barang
harga_buku_tulis = 5000
harga_pensil = 4500

# jumlah barang yang dibeli
jumlah_buku_tulis = 3
jumlah_pensil = 2

# hitung total harga barang sebelum dikenakan pajak
total_harga = (harga_buku_tulis * jumlah_buku_tulis) + (harga_pensil * jumlah_pensil)

# pajak 10%
pajak = 0.10 * total_harga

# total harga barang setelah dikenakan pajak
total_bayar = total_harga + pajak

# hasil
print (f"Total harga barang sebelum pajak: Rp. {total_harga}")
print (f"pajak 10%: Rp. {pajak}")
print (f"Total yang harus dibayar: Rp. {total_bayar}")
# Program menghitung total belanja Hallim setelah pajak

# Harga satuan
harga_buku = 5000
harga_pensil = 4500

# Jumlah barang
jumlah_buku = 3
jumlah_pensil = 2

# Hitung total harga sebelum pajak
total_harga_buku = harga_buku * jumlah_buku
total_harga_pensil = harga_pensil * jumlah_pensil
total_harga = total_harga_buku + total_harga_pensil

# Hitung pajak 10%
pajak = 0.10 * total_harga

# Hitung total akhir yang harus dibayar
total_setelah_pajak = total_harga + pajak

# Tampilkan hasil
print("Rincian Belanja Hallim:")
print(f"Total harga buku: Rp {total_harga_buku}")
print(f"Total harga pensil: Rp {total_harga_pensil}")
print(f"Total sebelum pajak: Rp {total_harga}")
print(f"Pajak (10%): Rp {int(pajak)}")
print(f"Total yang harus dibayar: Rp {int(total_setelah_pajak)}")

# Program menghitung total belanja setelah pajak

# Harga barang
harga_buku = 5000
harga_pensil = 4500

# Jumlah barang
jumlah_buku = 3
jumlah_pensil = 2

# Hitung total harga sebelum pajak
total_sebelum_pajak = (harga_buku * jumlah_buku) + (harga_pensil * jumlah_pensil)

# Hitung pajak 10%
pajak = 0.10 * total_sebelum_pajak

# Hitung total setelah pajak
total_setelah_pajak = total_sebelum_pajak + pajak

# Tampilkan hasil
print("Total belanja sebelum pajak : Rp", total_sebelum_pajak)
print("Pajak 10%                   : Rp", pajak)
print("Total yang harus dibayar   : Rp", total_setelah_pajak)

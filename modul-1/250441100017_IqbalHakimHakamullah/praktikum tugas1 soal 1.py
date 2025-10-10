# harga belanjaan halim
harga_buku_tulis = 5000
harga_pulpen = 4500

# jumlah item yang halim beli
jumlah_buku_tulis = 3
jumlah_pulpen = 2

# total belanja sebelum pajak
total_buku_sebelum_pajak = harga_buku_tulis * jumlah_buku_tulis
total_pulpen_sebelum_pajak = harga_pulpen * jumlah_pulpen
total_sebelum_pajak = total_buku_sebelum_pajak + total_pulpen_sebelum_pajak

# masukkan pajak 10%
pajak = 0.10 * total_sebelum_pajak

# total belanja setelah pajak
total_setelah_pajak = total_sebelum_pajak + pajak

print("TOTAL BELANJAAN HALIM")
print(f"total harga buku tulis = Rp. {total_buku_sebelum_pajak:,}")
print(f"total harga pulpen = Rp. {total_pulpen_sebelum_pajak:,}")
print(f"total belanja sebelum pajak = Rp. {total_sebelum_pajak:,}")
print(f"pajak 10% = Rp. {pajak:,}")
print(f"total belanja setelah pajak = Rp. {total_setelah_pajak:,}")
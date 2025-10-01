harga_buku_tulis = 5000
harga_pensil = 4500

jumlah_buku_tulis = 3
jumlah_pensil = 2

persen_pajak = 10

total_harga_buku_tulis= harga_buku_tulis * jumlah_buku_tulis
total_harga_pensil = harga_pensil * jumlah_pensil
total_harga_barang = total_harga_buku_tulis + total_harga_pensil
pajak = total_harga_barang * persen_pajak
total_belanja_setelah_pajak = total_harga_barang 
 

print(f"total harga buku tulis: Rp {total_harga_buku_tulis:,}")
print(f"total harga pensil: Rp {total_harga_pensil:,}")
print(f"total harga barang sebelum pajak: Rp {total_harga_barang:,}")
print(f"besar pajak (10%): Rp {pajak:}")
print(f"total belanja setelah pajak: Rp {total_belanja_setelah_pajak:,}")
print(f"total belanja yang harus di bayar oleh Hallim adalah: Rp {total_belanja_setelah_pajak:,}")
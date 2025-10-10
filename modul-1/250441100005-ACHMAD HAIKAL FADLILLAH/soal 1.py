harga_buku = 5000
harga_pensil = 4500
jumlah_buku = 3
jumlah_pensil = 2
pajak = 10/100

tot_harga_buku = harga_buku * jumlah_buku
tot_harga_pensil = harga_pensil * jumlah_pensil
tot_keseluruhan = tot_harga_buku + tot_harga_pensil
harga_pajak = pajak * tot_keseluruhan
setelah_pajak = harga_pajak + tot_keseluruhan

print("total harga buku adalah", tot_harga_buku)
print("total harga pensil adalah", tot_harga_pensil)
print("total harga keseluruhan adalah", tot_keseluruhan)
print("pajak dari", tot_keseluruhan, "adalah", harga_pajak) 
print("total harga yang harus dibayar ditambah pajak adalah", setelah_pajak)
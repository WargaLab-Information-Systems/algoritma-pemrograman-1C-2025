# a
harga_buku = 5000
harga_pensil = 4500
jumlah_buku = 3
jumlah_pensil = 2
pajak = 0.1

total_buku = harga_buku * jumlah_buku
total_pensil = harga_pensil * jumlah_pensil
total = total_buku + total_pensil
pajak = total * pajak
bayar = total + pajak

print(f"total:{total}")
print(f"pajak(10%:{int(pajak)}")
print(f"total bayar:{int(bayar)}")


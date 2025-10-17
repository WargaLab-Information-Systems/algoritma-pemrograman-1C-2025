harga_buku = 5000
harga_pensil = 4500
j_buku = 3
j_pensil = 2
pajak = 0.10 

t_buku = harga_buku * j_buku
t_pensil = harga_pensil * j_pensil
total = t_buku + t_pensil

pajak = total * pajak

bayar = total + pajak

print(f"total        :  {total}")
print(f"Pajak (10%)  :  {int(pajak)}")
print(f"Total bayar  :  {int(bayar)}")
buku=5000
pensil=4500

pcs_buku=3
pcs_pensil=2

total=(buku*pcs_buku)+(pensil*pcs_pensil)
print(f"harga total sebelum terkena pajak = {total}")
total_pajak=(total*10)//100
setelah_pajak=total_pajak+total
print(f"harga yang harus di bayar Setelah di pajak = {setelah_pajak}")
# # TUGAS1

# buku = 5000
# pensil =4500

# j_buku = 3
# j_pensil =2 
# pajak = 0.1

# t_buku = j_buku * buku
# t_pensil = j_pensil * pensil    
# total_belanja = t_buku + t_pensil

# total = (t_buku + t_pensil) 
# pajak = total_belanja * pajak
# bayar = total_belanja + pajak

# print(f"total: {total}")
# print(f"pajak: {pajak}")
# print(f"bayar: {bayar}")

# # TUGAS2

# p = int(input("Masukkan panjang   : "))
# l = int(input("Masukkan lebar     : "))
# t = int(input("Masukkan tinggi    : "))

# volume = p * l * t
# luas = 2 * (p * l + p * t + l * t)

# print(f"Volume balok    : {volume}")
# print(f"Luas permukaan  : {luas}")

# tugas3#

#  tb: total bola
# a: jumlah bola yang diambil
tb = int(input("Masukkan total bola: "))
a = int(input("Masukkan jumlah bola yang diambil: "))



numerator = tb * (tb-1) * (tb-2)        
denominator = a * (a-1) * (a-2)      

kombinasi = numerator // denominator

print(f"dumerator: {numerator}")
print(f"denominator: {denominator}")
print(f"kemungkinan kombinasi: {kombinasi}")

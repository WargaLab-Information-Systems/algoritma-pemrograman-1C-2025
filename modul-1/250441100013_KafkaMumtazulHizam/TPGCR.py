# TUGAS 1

# harga_buku = 5000
# harga_pensil = 4500
# j_buku = 3
# j_pensil = 2
# pajak = 0.10 

# t_buku = harga_buku * j_buku
# t_pensil = harga_pensil * j_pensil
# total = t_buku + t_pensil

# pajak = total * pajak

# bayar = total + pajak

# print(f"total        :  {total}")
# print(f"Pajak (10%)  :  {int(pajak)}")
# print(f"Total bayar  :  {int(bayar)}")



# TUGAS 2

p = int(input("masukan panjang: "))
l = int(input("masukan lebar: "))
t = int(input("masukan tinggi: "))

volume = p * l * t
luas = 2 * (p * l + p * t + l * t)

print(f"Volume balok    : {volume}")
print(f"Luas permukaan  : {luas}")



# TUGAS 3

# tb: total bola
# a: jumlah bola yang diambil
# tb = 14
# a = 3

# menghitung kombinatorik agar nilai r = 3
# numerator = tb * (tb-1) * (tb-2)        # 14*13*12 = 2184
# denominator = a * (a-1) * (a-2)      # 3*2*1 = 6

# kombinasi = numerator // denominator

# print(f"dumerator: {numerator}")
# print(f"denominator: {denominator}")
# print(f"kemungkinan kombinasi: {kombinasi}")
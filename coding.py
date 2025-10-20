#tugas1
# print("TOKO ALAT TULIS")
print("------------------------------------")
a = 5000
b = 4500
print("Harga buku:", a)
print("Harga pulpen:", b)

c = a * 3
d = b * 2
print("Harga total buku:", c)
print("Harga total pulpen:", d)
print("Pajak 10%")
e = c + d
print("Total belanja:", e)
g = 24000 - 2400
print(f"Total belanja setelah terkena pajak:, {g}")

#tugas2
p = int(input("Masukkan panjang   : "))
l = int(input("Masukkan lebar     : "))
t = int(input("Masukkan tinggi    : "))

volume = p * l * t
luas = 2 * (p * l + p * t + l * t)

print(f"Volume balok    : {volume}")
print(f"Luas permukaan  : {luas}")

#tugas3
#  tb: total bola
# a: jumlah bola yang diambil
tb = int(input("Masukkan total bola: "))
a = int(input("Masukkan jumlah bola yang diambil: "))



numerator = tb * (tb-1) * (tb-2)        
denominator = a * (a-1) * (a-2)      

kombinasi = numerator // denominator

print(f"dumerator: {numerator}")
print(f"denominator: {denominator}")
print(f"kemungkinan kombinasi: {kombinasi}")
# kasus
# panjang = 10
# lebar = 6
# tinggi = 4

panjang = int(input("Masukkan panjang: "))
lebar = int(input("Masukkan lebar: "))
tinggi = int(input("Masukkan tinggi: "))

volume = panjang * lebar * tinggi
luas_permukaan = 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)

print("Volume balok:", volume, "cm^3")
print("Luas permukaan balok:", luas_permukaan, "cm^2") 
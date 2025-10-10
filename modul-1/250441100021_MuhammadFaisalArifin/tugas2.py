panjang = int(input("Panjang: "))
lebar = int(input("Lebar: "))
tinggi = int(input("Tinggi: "))

volume = panjang * lebar * tinggi
luas = 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)

print("Volume balok:", volume,)
print("Luas balok:", luas,)
panjang = int(input("Masukkan ukuran panjang balok (cm): "))
lebar = int(input("Masukkan ukuran lebar balok (cm): "))
tinggi = int(input("Masukkan tinggi balok (cm)"))

volume = panjang * lebar * tinggi
luas_sebuah_permukaan = 2 * ((panjang * lebar) + (panjang * tinggi) + (lebar * tinggi))

print("ukuran volume balok:", volume, "cm")
print("luas pada permukaan balok:", luas_sebuah_permukaan, "cm")
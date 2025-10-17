panjang = float(input("Masukkan panjang balok (cm): "))
lebar = int(input("Masukkan lebar balok (cm): "))
tinggi = int(input("Masukkan tinggi balok (cm): "))

# Menghitung volume
volume = panjang * lebar * tinggi

# Menghitung luas permukaan
luas_permukaan = 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)

print("Hasil Perhitungan Balok:")
print("Volume balok:", volume, "cm³")
print("Luas permukaan balok:", luas_permukaan, "cm²")
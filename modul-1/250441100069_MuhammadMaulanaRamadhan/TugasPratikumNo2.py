# masukkan panjang, lebar,dan tinggi balok
panjang = float(input("Masukkan panjang balok (cm): "))
lebar = float(input("Masukkan lebar balok (cm): "))
tinggi = float(input("Masukkan tinggi balok (cm): "))

# hitung volume dan luas permukaan balok
volume = panjang * lebar * tinggi
luas_permukaan = 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)

# hasil
print(f"Volume balok = ", volume, "cm³")
print(f"Luas permukaan balok = ", luas_permukaan, "cm²")
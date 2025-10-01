# Program menghitung volume dan luas permukaan balok

# Input dari pengguna
panjang = float(input("Masukkan panjang balok (cm): "))
lebar = float(input("Masukkan lebar balok (cm): "))
tinggi = float(input("Masukkan tinggi balok (cm): "))

# Hitung volume dan luas permukaan
volume = panjang * lebar * tinggi
luas_permukaan = 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)

# Tampilkan hasil
print("\n==== Hasil Perhitungan Balok ====")
print("Volume balok          :", volume, "cm³")
print("Luas permukaan balok  :", luas_permukaan, "cm²")

# Program Menghitung Volume dan Luas Permukaan Balok
# Input: Panjang, Lebar, Tinggi (dalam cm)
# Output: Volume dan Luas Permukaan (dalam cm³ dan cm²)

print("Selamat datang! Program ini akan menghitung volume dan luas permukaan balok.")
print("Masukkan ukuran balok (dalam cm):")

# Input dari pengguna
panjang = float(input("Panjang: "))
lebar = float(input("Lebar: "))
tinggi = float(input("Tinggi: "))

# Hitung Volume: V = panjang * lebar * tinggi
volume = panjang * lebar * tinggi

# Hitung Luas Permukaan: LP = 2*(panjang*lebar + panjang*tinggi + lebar*tinggi)
luas_permukaan = 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)

# Output hasil
print("\nHasil Perhitungan:")
print(f"Volume Balok: {volume} cm³")
print(f"Luas Permukaan Balok: {luas_permukaan} cm²")

# Contoh dengan ukuran yang diberikan (10 cm, 6 cm, 4 cm)
# Jika dijalankan dengan input tersebut, volume = 240 cm³, luas permukaan = 248 cm²

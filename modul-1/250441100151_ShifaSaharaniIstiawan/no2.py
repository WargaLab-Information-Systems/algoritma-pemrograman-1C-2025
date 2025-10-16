# soal 2
panjang = int(input("Masukkan panjang balok (cm): "))
lebar = int(input("Masukkan lebar balok (cm): "))
tinggi = int(input("Masukkan tinggi balok (cm): "))

# Hitung volume dan luas permukaan

volume = panjang * lebar * tinggi
luas_permukaan = 2 *((panjang * lebar) + (panjang * tinggi) + (lebar * tinggi) )

# Tampilkan hasil
print(f"Volume balok adalah: {volume} cm³")
print(f"Luas permukaan balok adalah: {luas_permukaan} cm²")

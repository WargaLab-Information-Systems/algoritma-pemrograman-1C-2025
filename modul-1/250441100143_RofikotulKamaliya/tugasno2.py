# Soal No.2

panjang = float(input("Masukkan panjang balok (cm): "))
lebar = float(input("Masukkan lebar balok (cm): "))
tinggi = float(input("Masukkan tinggi balok (cm): "))

# Rumus Volume Balok: V = p x l x t
volume = panjang * lebar * tinggi

# Rumus Luas Permukaan Balok: L = 2 x (pl + pt + lt)
luas_permukaan = 2 * ( (panjang * lebar) + (panjang * tinggi) + (lebar * tinggi) )

print(f"Volume Balok: {volume} cm³")
print(f"Luas Permukaan Balok: {luas_permukaan} cm²")
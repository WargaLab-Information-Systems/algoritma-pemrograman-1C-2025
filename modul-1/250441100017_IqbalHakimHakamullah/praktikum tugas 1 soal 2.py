print("masukkan ukuran balok")

# input dari user
panjang = int(input("panjang="))
lebar = int(input("lebar="))
tinggi = int(input("tinggi="))

# menghitung volume balok
volume = panjang * lebar * tinggi

# menghitung luas permukaan balok
luas_permukaan = 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)

print("HASIL PERHITUNGAN")
print(f"volume balok = {volume} cm3")
print(f"luas permukaan balok = {luas_permukaan} cm2")

# Program Menghitung Volume dan Luas Permukaan Balok

def hitung_volume(panjang, lebar, tinggi):
    return panjang * lebar * tinggi

def hitung_luas_permukaan(panjang, lebar, tinggi):
    return 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)

# Input dari pengguna
try:
    panjang = float(input("Masukkan panjang balok (cm): "))
    lebar = float(input("Masukkan lebar balok (cm): "))
    tinggi = float(input("Masukkan tinggi balok (cm): "))

    # Validasi input tidak boleh negatif
    if panjang <= 0 or lebar <= 0 or tinggi <= 0:
        print("Panjang, lebar, dan tinggi harus lebih dari 0.")
    else:
        volume = hitung_volume(panjang, lebar, tinggi)
        luas_permukaan = hitung_luas_permukaan(panjang, lebar, tinggi)

        print(f"\nVolume balok: {volume} cm³")
        print(f"Luas permukaan balok: {luas_permukaan} cm²")

except ValueError:
    print("Input tidak valid. Harap masukkan angka.")

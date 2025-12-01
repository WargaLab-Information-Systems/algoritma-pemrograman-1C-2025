# Program untuk menentukan apakah dua kata merupakan anagram

def cek_anagram(kata1, kata2):
    """Fungsi untuk memeriksa apakah dua kata adalah anagram"""
    # Hilangkan spasi dan ubah ke huruf kecil agar perbandingan konsisten
    kata1 = kata1.replace(" ", "").lower()
    kata2 = kata2.replace(" ", "").lower()

    # Cek apakah panjangnya sama dan hurufnya memiliki susunan yang sama
    return sorted(kata1) == sorted(kata2)


# Program utama (dinamis)
print("=== Program Pengecekan Anagram ===")
kata1 = input("Masukkan kata pertama: ")
kata2 = input("Masukkan kata kedua: ")

# Panggil fungsi untuk memeriksa
hasil = cek_anagram(kata1, kata2)

# Tampilkan hasil
if hasil:
    print(f" '{kata1}' dan '{kata2}' adalah ANAGRAM.")
else:
    print(f" '{kata1}' dan '{kata2}' bukan anagram.")

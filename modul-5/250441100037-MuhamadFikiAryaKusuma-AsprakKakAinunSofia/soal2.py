def apakah_anagram(kata1, kata2):
    kata1 = kata1.replace(" ", "").lower()
    kata2 = kata2.replace(" ", "").lower()
    
    return sorted(kata1) == sorted(kata2)
# Input dari pengguna
kata1 = input("Masukkan kata pertama: ")
kata2 = input("Masukkan kata kedua: ")

# Memanggil fungsi dan menampilkan hasil
if apakah_anagram(kata1, kata2):
    print(kata1, "dan", kata2, "adalah anagram.")
else:
    print(kata1, "dan", kata2, "bukan anagram.")
def anagram(kata1, kata2):
    return sorted(kata1) == sorted(kata2)

print("Masukkan dua kata untuk mengecek apakah termasuk anagram atau bukan:")
kata1 = input("Kata pertama: ")
kata2 = input("Kata kedua: ")

if anagram(kata1, kata2):
    print(f"'{kata1}' dan '{kata2}' adalah anagram.")
else:
    print(f"'{kata1}' dan '{kata2}' bukan anagram.")
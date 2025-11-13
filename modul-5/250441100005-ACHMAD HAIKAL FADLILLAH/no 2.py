def is_anagram(kata1, kata2):
    kata1 = kata1.replace(" ", "").lower()
    kata2 = kata2.replace(" ", "").lower()
    
    return sorted(kata1) == sorted(kata2)

kata1 = input("Masukkan kata pertama: ")
kata2 = input("Masukkan kata kedua: ")

hasil = is_anagram(kata1, kata2)

if hasil:
    print(f"'{kata1}' dan '{kata2}' adalah anagram (True).")
else:
    print(f"'{kata1}' dan '{kata2}' bukan anagram (False).")

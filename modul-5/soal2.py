def is_anagram(word1, word2):
    # Konversi ke lowercase dan sort huruf-hurufnya
    sorted_word1 = sorted(word1.lower())
    sorted_word2 = sorted(word2.lower())
    # Bandingkan apakah sama
    return sorted_word1 == sorted_word2
# Program utama untuk input dinamis
kata1 = input("Masukkan kata pertama: ")
kata2 = input("Masukkan kata kedua: ")
hasil = is_anagram(kata1, kata2)
if hasil:
    print(f"Kata '{kata1}' dan '{kata2}' merupakan anagram.")
else:
    print(f"Kata '{kata1}' dan '{kata2}' bukan anagram.")
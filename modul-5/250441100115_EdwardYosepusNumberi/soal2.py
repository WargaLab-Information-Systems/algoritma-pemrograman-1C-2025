def is_anagram(word1, word2):
   
    return sorted(word1.lower()) == sorted(word2.lower())

word1 = input("Masukkan kata pertama: ")
word2 = input("Masukkan kata kedua: ")

result = is_anagram(word1, word2)
if result:
    print("Kedua kata adalah anagram.")
else:
    print("Kedua kata bukan anagram.")
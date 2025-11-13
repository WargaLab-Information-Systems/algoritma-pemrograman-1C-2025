def anagram(kata1, kata2):
    kata1 = kata1
    kata2 = kata2

    if sorted(kata1) == sorted(kata2):
        return True
    else:
        return False
kata1 = input("masukkan kata pertama : ")
kata2 = input("masukkan kata kedua : ")

if anagram(kata1, kata2):
    print(kata1, "dan", kata2, "adalah anagram")
else:
    print(kata1, "dan", kata2, "bukan anagram")
anagram(kata1, kata2)

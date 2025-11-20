def cek_anagram(kata1, kata2):
    k1 = ""
    k2 = ""
    for i in kata1.lower():
        if i != " ":
            k1 += i
    for j in kata2.lower():
        if j != " ":
            k2 += j
    return sorted(k1) == sorted(k2)

kata1 = input("Masukkan kata pertama: ")
kata2 = input("Masukkan kata kedua: ")

if cek_anagram(kata1, kata2):
    print("Kedua kata tersebut merupakan ANAGRAM!")
else:
    print("Kedua kata tersebut BUKAN anagram.")

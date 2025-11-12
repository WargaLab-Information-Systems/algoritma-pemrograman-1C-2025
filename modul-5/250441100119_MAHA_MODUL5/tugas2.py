def cek_anagram(kata1, kata2):
    kata1 = kata1.lower()
    kata2 = kata2.lower()

    if len(kata1) != len(kata2):
        return False
    
    for huruf in kata1:
        if huruf not in kata2:
            return False
        kata2 = kata2.replace(huruf,'', 1)
    return True

kata_pertama = input("masukkan kata pertama:")
kata_kedua = input("masukkan kata kedua:")
hasil = cek_anagram(kata_pertama, kata_kedua)

if hasil:
    print(f"{kata_pertama} dan {kata_kedua} adalah anagram!")
else:
    print(f"{kata_pertama} dan {kata_kedua} bukan anagram!")
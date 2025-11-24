def cek_anagram(kata1, kata2):
    if len(kata1) != len(kata2):
        return False
    cocok = 0  
    # cek tiap huruf di kata1, lalu bandingkan ke kata2
    for huruf1 in kata1:
        for huruf2 in kata2:
            if huruf1 == huruf2:
                cocok += 1
                break 
    if cocok == len(kata1):
        return True
    else:
        return False
# input dari user
kata_pertama = input("Masukkan kata pertama: ")
kata_kedua = input("Masukkan kata kedua: ")
# hasil
if cek_anagram(kata_pertama, kata_kedua):
    print("Ya, kedua kata adalah anagram.")
else:
    print("Tidak, kedua kata bukan anagram.")

def hitung_kemunculan(kata, huruf):
    jumlah = 0
    for i in kata:
        if i == huruf:
            jumlah += 1
    return jumlah

def is_anagram(kata1, kata2):
    if len(kata1) != len(kata2):
        return False
    
    for huruf in kata1:
        if hitung_kemunculan(kata1, huruf) != hitung_kemunculan(kata2, huruf):
            return False
        
    return True
    
kata1 = input("masukkan kata pertama: ")
kata2 = input("masukkan kata kedua: ")

hasil = is_anagram(kata1, kata2)
if hasil:
    print(f"{kata1} dan {kata2} adalah anagram. ")
else:
    print(f"{kata1} dan {kata2} bukan anagram. ") 

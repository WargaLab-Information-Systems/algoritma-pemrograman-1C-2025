#MENGECEK APAKAH DUA KATA ADALAH ANAGRAM    
def cek_anagram():
    k1 = input ("masukkan kata pertama:")
    k2 = input ("masukkan kata kedua:")

#MENGHILANGKAN SPASI DAN UBAH KE HURUF KECILL
    k1 = k1 .replace (" ", "") #replace digunakan menghilangkan spasi
    k2 = k2.replace (" ", "")

#MEMBANDINGKAN HURUF SETELAH DIURUTKAN
    if sorted(k1) == sorted (k2): #sorted mengurutkan huruf
        print (f"{k1} dan {k2} adalah anagram")
        # return True # jika anagram maka akan mengembalikan nilai True
    else:
        print (f"{k1} dan {k2} bukan anagram")
        # return False 

#PEMANGGILAN FUNGSI
cek_anagram()


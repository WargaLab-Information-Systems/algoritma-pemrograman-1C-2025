def anagram(nama1,nama2):
    spasi="" #inisialiasi sebagai tanda spasi 
    for huruf in nama2: #men-generete ulang satu persatu huruf di kalimat ke 2 menggunakan varibel huruf
        if huruf in spasi:# jika ada spasi di 
            cek_anagram=False # akan lanjut ke aksi selanjutnya
            break
        elif huruf in nama1: #jika di huruf di kata kedua juga ada di kata pertama maka
            cek_anagram=True # variabel cek_anagram akan bernilai true
        else:#jika di huruf kata kedua tidak ada sama sekali di kata pertama maka
            cek_anagram=False#variabel cek_anagram akan bernilai false dan akan
            break #stop

        if len(nama1)!=len(nama2):
            cek_anagram=False
    return cek_anagram #ujung fungsi ini akan di pegang oleh value cek_anagram

nama1=str(input("input kata ke 1 = "))#user meng input kata pertama
nama2=str(input("input kata ke 2 = "))#user meng input kata kedua
hasil=anagram(nama1,nama2)#variabel untuk memanggil fungsi 
print("kedua kata anagram = ",hasil) # perintah untuk cetak
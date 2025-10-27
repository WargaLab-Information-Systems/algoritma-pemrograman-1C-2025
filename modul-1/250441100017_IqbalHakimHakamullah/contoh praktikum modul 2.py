# seleksi kondisi
hewan1= "kucing"
hewan2= "ayam"
hewan3= "kambing"
pilih = int (input("masukkan inputan: "))
if pilih == 1 :
    print(hewan1)
    makan = input ("apa makanannya? :")
    if makan == "rumput" :
        print("salah")
    elif makan == "ikan" :
        print("benar")
    else :
        print("kucing makan apa?")
elif pilih == 2 :
    print(hewan2)
elif pilih == 3 :
    print(hewan3)
else :
    print("hanya ada 3 pilihan")

angka1 = 10
if angka1 >= 11 :
    print("salah")
elif angka1 < 11 :
    print("benar")
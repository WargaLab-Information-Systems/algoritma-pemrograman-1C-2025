list_awal = []
hasil=bool()


def membuat():
    while True:
        kualifikasi=(input(f"input angka pada list , N = tidak =  "))
        if kualifikasi.upper() != "N" :
            angka=int(kualifikasi)
            list_awal.append(angka)
        else:
            print("selesai")
            break

def menghapus():
    while True:
        kualifikasi_1=(input(f"input angka pada list yang ingin hapus , N = tidak =  "))
        if kualifikasi_1.upper() != "N" :
            angka_1=int(kualifikasi_1)
            list_awal.remove(angka_1)
        else:
            print("selesai")
            break

def menampilkan_data():
    print(list_awal)

def mengecek():
    if len(list_awal)%2==0: #mengecek apakah genap atau ganti berdasarka jumlah elemen list nya
        total_len=len(list_awal) #total elemen di dalam list
        pembagi=len(list_awal)//2 #untuk mencari nilai tengah 
        print(" bisa di bagi dua")
        bagian_pertama= list_awal[0:pembagi] #me motong dari elemen berdasarkan index awal juga sampai index tengah berdasarkan nilai pembagi
        bagian_kedua= list_awal[pembagi:total_len] #me motong dari elemen list dari index tengah sampai ujung berdasarkan value len list 
        hasil=(True) #variabel hasil di set true karena bsia di set 2
        print(bagian_pertama,end="")
        print(bagian_kedua)
        print("Bisa di bagi 2 = ",hasil)
    else:
        hasil=bool(False)
        print("Bisa di bagi 2 = ",hasil)

def menu():
    tabel_pilihan=int(input(f"[TAMBAH NILAI = 1] [HAPUS DATA = 2 ][TAMPILKAN value List = 3 ] [PROGRAM SELESAI = 0]  = "))
    return tabel_pilihan

while True:
    pilihan=menu()
    if pilihan==0:
         print("program selesai")
         break
    elif pilihan==1:
         membuat()
         mengecek()
    elif pilihan==2:
         menghapus()
    elif pilihan==3:
        menampilkan_data()
        print("bisa di bagi 2 = ",hasil)







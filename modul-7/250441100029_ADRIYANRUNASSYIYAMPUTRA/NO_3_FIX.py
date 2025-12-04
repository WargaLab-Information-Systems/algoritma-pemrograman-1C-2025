diskon={
    'ADRIYAN88':0.1, #diskon 10 persen
    'ROLEKECE25':0.2,
    'RAHASIA98':0.9,
    'GOKIL1000':1.0,


}
list_kupon=[]


def masukkan_diskon():
    total_belanja=int(input("input total pembelanjaan sementara = "))
    while True:
        kupon=str(input("input kode diskon = "))
        if diskon.get(kupon) is  None and kupon in list_kupon :
            print("kupon tidak valid dan sudah pernah di pakai")
        elif diskon.get(kupon) is  None and kupon not in list_kupon:
            print("kupon tidak valid")
        elif diskon.get(kupon) is not  None:
            print("kupon bisa di gunakan")
            pemotongan_harga=int(diskon[kupon]*total_belanja)
            pentotalan_akhir=int(total_belanja-pemotongan_harga)
            print(f"total produk    = {total_belanja:,}")
            print(f"potongan harga  = {pemotongan_harga:,}")
            print(f"total akhir     = {pentotalan_akhir:,}")
            list_kupon.append(kupon)
            del diskon[kupon]
            break
        

def tampilkan_diskon(): 
    print("=================KUPON YANG MASIH TERSEDIA=================")       
    for i in diskon:
        print(f"{i}")




def menu():
    while True:
        tabel_pemilihan=int(input(f"[0= untuk progran selesai][1=menampilkan diskon yang tersedia][2=proses transaksi] = "))
        if tabel_pemilihan not in [0,1,2]:
            print("input dengan benar")
        else:
            return tabel_pemilihan

while True:
    pilihan=menu()
    if pilihan==0:
         print("program selesai")
         break
    elif pilihan==1:
         tampilkan_diskon()
    elif pilihan==2:
         masukkan_diskon()

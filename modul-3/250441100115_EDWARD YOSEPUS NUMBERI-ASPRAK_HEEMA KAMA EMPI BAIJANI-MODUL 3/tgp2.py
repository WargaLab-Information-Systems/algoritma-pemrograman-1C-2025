Pin_benar = "25115"
kesempatan = 3

for i in range(kesempatan):
    pin = input ("masukan pin anda : ")
    if pin == Pin_benar:
        print("pin benar, pilih transaksi anda")
        break
    else:
        print("pin salah, coba lagi")
else:
    print("akses ditolak, kartu diblokir")
    

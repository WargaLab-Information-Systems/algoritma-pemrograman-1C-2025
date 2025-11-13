kesempatan = 3
while kesempatan > 0:
    pin = input("Masukkan PIN Anda: ")
    if pin == "25037":
        print("PIN benar, Akses diterima.")
        break
    else:
        kesempatan -= 1
        if kesempatan == 0:
            print("Akses ditolak. Kartu diblokir.")
        else:
            print("PIN salah, coba lagi")
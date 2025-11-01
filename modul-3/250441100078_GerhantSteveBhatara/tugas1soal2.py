pin_benar = "25078"
kesempatan = 3

while kesempatan > 0:
    pin = input("Masukkan PIN: ")
    if pin == pin_benar:
        print("PIN benar, akses diterima.")
        break
    else:
        kesempatan -= 1
        if kesempatan > 0:
            print("PIN salah, coba lagi.")
        else:
            print("Akses ditolak, kartu diblokir.")
pin_benar = "25131"
kesempatan = 3
status_login = False
while not status_login and kesempatan > 0 :
    pin =(input("masukkan pin (5 digit):"))

    if not pin.isdigit() or len(pin) !=5 :
        print("pin harus berupa angka dan harus 5 digit. \n")
        continue
    if pin == pin_benar :
        print("\npin benar, akses diterima")
        status_login = True
            

    else:
        kesempatan -= 1
        if kesempatan > 0:
            print(f"pin salah, coba lagi. sisa kesempatan: {kesempatan}\n")
        else:
            print("\nakses ditolak, kartu diblokir")
            break


print("Halo Selamat Datang di Mesin ATM")
PIN_BENAR = 25033
kesempatan = 3

while kesempatan > 0:
    pin_input = input("Silahkan Masukkan PIN Anda (5 digit angka): ")

    # Harus angka
    if not pin_input.isdigit():
        print("PIN salah, coba lagi.")
        kesempatan -= 1
    else:
        pin = int(pin_input)
        
        # Harus 5 digit
        if pin < 10000 or pin > 99999:
            print("PIN salah, coba lagi.")
            kesempatan -= 1
        elif pin != PIN_BENAR:
            print("PIN salah, coba lagi.")
            kesempatan -= 1
        else:
            print("PIN benar, akses diterima.")
            break
    if kesempatan == 0:
        print("Akses ditolak, kartu diblokir.")
    else:
        print("Sisa kesempatan:", kesempatan)
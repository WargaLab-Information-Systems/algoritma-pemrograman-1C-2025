PIN_BENAR = 25069
KESEMPATAN = 3

print("==== Selamat datang di ATM ====")

while KESEMPATAN > 0:
    pin_input = int(input(f"Masukkan PIN Anda(5 digit) ({KESEMPATAN} kesempatan tersisa): "))

    if pin_input == PIN_BENAR:
        print("\nPIN benar, akses diterima")
        break 
    else:
        KESEMPATAN -= 1
        if KESEMPATAN > 0:
            print("PIN salah, coba lagi.")

if KESEMPATAN == 0:
    print("\nAkses ditolak, kartu diblokir")
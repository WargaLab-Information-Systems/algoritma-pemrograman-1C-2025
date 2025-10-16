# Tugas no 2

pin_benar = 25057
kesempatan = 3

while kesempatan > 0:
    pin = int(input("Masukkan PIN (5 digit): "))

    if pin == pin_benar:
        print("PIN benar, akses diterima.")
        break
    else:
        kesempatan -= 1
        print("PIN salah, coba lagi.")

    if kesempatan == 0:
        print("Akses ditolak, kartu diblokir.")

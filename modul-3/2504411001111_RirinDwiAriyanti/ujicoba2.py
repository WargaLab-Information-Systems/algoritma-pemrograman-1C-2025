pin_benar = 25111
kesempatan = 3

while kesempatan > 0:
    pin_input = input("Masukkan PIN : ")

    if not pin_input.isdigit():
        print(" Masukkan pin anda!")
        continue
    pin = int(pin_input)

    if len(pin_input) != 5:
        print(" PIN harus berjumlah 5 digit!")
        continue
    if pin == pin_benar:
        print(" PIN benar, akses diterima")
        break
    else:
        kesempatan -= 1
        if kesempatan > 0:
            print(" PIN salah!coba lagi:")
        else:
            print(" Akses ditolak, kartu diblokir.")


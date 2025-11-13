pin = 25119
kesempatan = 3

while kesempatan > 0:
    pin_input = input("MASUKKAN PIN ANDA DENGAN BENAR:")

    if not pin_input.isdigit():
        print("PIN HARUS BERUPA ANGKA!")

    if len(pin_input) != 5:
        print("PIN TERDIRI DARI 5 DIGIT!")
        continue

    pin_input = int(pin_input)

    if pin_input == pin:
        print("PIN BENAR, AKSES DITERIMA")
        break
    else:
        kesempatan -= 1
        if kesempatan > 0:
            print("PIN SALAH, COBA LAGI")
        else:
            print("AKSES DITOLAK, KARTU DIBLOKIR")
pin_benar = 25135

for i in range(3):
    pin = input("Masukkan PIN (5 digit): ")

    if not pin.isdigit():
        print("PIN harus berupa angka!\n")
        continue

    if len(pin) != 5:
        print("PIN harus 5 digit!\n")
        continue

    if int(pin) == pin_benar:
        print("PIN benar, akses diterima!")
        break
    else:
        print("PIN salah, coba lagi!")
else:
    print("Akses ditolak, kartu diblokir!")

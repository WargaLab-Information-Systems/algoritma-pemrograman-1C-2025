PIN_BENAR = 25127
kesempatan = 3

for i in range(kesempatan):
    pin = input("Masukkan PIN (5 digit): ")

    if len(pin) != 5:
        print("PIN harus 5 digit!")
        continue

    if pin == "25127":
        print("PIN benar, akses diterima.")
        break
    else:
        print("PIN salah, coba lagi.")

else:
    print("Akses ditolak, kartu diblokir.")

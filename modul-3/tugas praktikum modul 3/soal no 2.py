pin_benar = "25139"
percobaan_gagal = 0

while percobaan_gagal <3:
    pin_input = input("masukkan PIN (5 digit): ")

    if len(pin_input) == 5 and pin_input.isdigit():
        if pin_input == pin_benar:
            print("PIN benar, akses diterima")
            break
        else:
            percobaan_gagal += 1
            print("PIN salah, coba lagi")
    else:
        print("input tidak valid. PIN harus 5 angka.")
if percobaan_gagal == 3:
    print("Akses ditolak, kartu diblokir")




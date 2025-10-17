kunci = "25005"
maks = 3
percobaan = 0
while percobaan < maks :
    pin = (input("masukkan pin anda (2 NIM awal, 3 NIM akhir): "))
    if len(pin) != 5 :
        print("pin harus terdiri dari 5 digit")
        continue
    if pin == kunci:
        print("PIN benar, akses diterima")
        break
    else:
        percobaan += 1
        sisa = maks - percobaan
        if sisa > 0 :
            print("PIN salah, coba lagi")
        else:
            print("akses ditolak, kartu anda diblokir")
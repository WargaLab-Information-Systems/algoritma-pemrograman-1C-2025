# Simulasi mesin ATM dengan 3 kali percobaan PIN
# Menggunakan While

pin_benar = "25107"   # PIN yang benar
percobaan = 0        # Menghitung jumlah percobaan

while percobaan < 3:
    pin = input("Masukkan PIN (5 digit): ")

    if pin == pin_benar:
        print("PIN benar, akses diterima.")
        break
    else:
        percobaan += 1
        if percobaan < 3:
            print("PIN salah, coba lagi.")
        else:
            print("PIN salah 3 kali. Kartu diblokir.")

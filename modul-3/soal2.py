PIN_BENAR = 25073
kesempatan = 3
percobaan = 0

print("=== Selamat Datang di Mesin ATM ===")

while percobaan < kesempatan:
    try:
        pin = int(input("Masukkan PIN: "))

        if pin == PIN_BENAR:
            print("PIN benar, akses diterima ✅")
            break
        else:
            percobaan += 1
            sisa = kesempatan - percobaan
            if sisa > 0:
                print("PIN salah, coba lagi. Sisa kesempatan:",{sisa})
            else:
                print("Akses ditolak, kartu diblokir ❌")

    except ValueError:
        print("PIN harus berupa angka!Coba lagi.") 
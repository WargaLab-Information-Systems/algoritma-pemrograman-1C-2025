 main
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
main

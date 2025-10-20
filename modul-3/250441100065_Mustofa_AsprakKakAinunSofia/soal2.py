# Program Simulasi Mesin ATM
# PIN berdasarkan NIM: XXYYY (X = 2 digit awal, Y = 3 digit akhir)
# NIM kamu -> X = 25, Y = 065 => PIN = 25065

PIN_BENAR = 25065
kesempatan = 3

print("=== Simulasi Mesin ATM ===")

while kesempatan > 0:
    pin = input("Masukkan PIN (5 digit): ")

    if not pin.isdigit():
        print("PIN harus berupa angka!")
    elif len(pin) != 5:
        print("PIN harus 5 digit!")
    else:

        pin = int(pin)

        if pin == PIN_BENAR:
            print("PIN benar, akses diterima")
            break
        else:
            kesempatan = kesempatan - 1
            if kesempatan > 0:
                print("PIN salah, coba lagi. Sisa percobaan:", kesempatan)
            else:
                print("Akses ditolak, kartu diblokir")
# PIN dari NIM
pin_benar = "25009"
print("Masukkan PIN (5 digit):")
kesalahan = 0  # Hitung kesalahan PIN
while kesalahan < 3:  
    pin = input("PIN: ")
    jumlah_digit = 0     # manual
    for angka in pin:
        jumlah_digit = jumlah_digit + 1
    if jumlah_digit != 5: # Cek digit benar (harus 5)
        print("PIN harus 5 digit!")  # Tidak dihitung sebagai kesalahan
    else:
        if pin == pin_benar:
            print("PIN benar, akses diterima")
            break #keluar
        else:
            kesalahan = kesalahan + 1
            if kesalahan < 3:
                print("PIN salah, coba lagi")
            else:
                print("Akses ditolak, kartu diblokir")
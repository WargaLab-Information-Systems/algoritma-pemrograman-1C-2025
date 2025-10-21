nim = str(25029)
password_benar = False
print("========SELAMAT DATANG==========")
kesempatan_digit = 5
kesempatan_password = 3

while kesempatan_digit > 0 and kesempatan_password > 0:
    pin = input("Masukkan Password: ")  # input() sudah string
    jumlah_digit = 0  # RESET setiap percobaan
    
    for digit in pin:
        jumlah_digit += 1
    
    if kesempatan_digit==0 or kesempatan_digit==0:
        break
    
    print(f"Jumlah digit: {jumlah_digit}")

    if pin == '25029' and jumlah_digit == 5:
        print("PIN benar, akses diterima")
        password_benar = True
        break
    elif jumlah_digit != 5 and jumlah_digit>5 or jumlah_digit<5:
        kesempatan_digit -= 1
        print(f"Kesalahan digit, kesempatan tersisa: {kesempatan_digit}")
    elif pin != '25029' and jumlah_digit == 5:
        kesempatan_password -= 1
        print(f"Kesalahan password, kesempatan tersisa: {kesempatan_password}")
    else:  #pin salah dan digit salah
        kesempatan_password -= 1
        print(f"Kesalahan digit dan password, kesempatan tersisa - digit: {kesempatan_digit}, password: {kesempatan_password}")

# Cek setelah sudah loop
if not password_benar:
    if kesempatan_digit <= 0:
        print("❌ KARTU DIBLOKIR karena kesalahan digit berulang!")
    elif kesempatan_password <= 0:
        print("❌ KARTU DIBLOKIR karena kesalahan password berulang!")
PIN_BENAR = 25095

for percobaan in range( 4):
    pin = input("Masukkan PIN 5 digit: ")

    if not pin.isdigit() or len(pin) != 5:
        print("PIN harus berupa 5 digit angka!")
        continue

    if int(pin) == PIN_BENAR:
        print("PIN benar, akses diterima.")
        break
    else:
        print(f"PIN salah, coba lagi. ({percobaan}/3)")
else:
    print("Akses ditolak, kartu diblokir.")
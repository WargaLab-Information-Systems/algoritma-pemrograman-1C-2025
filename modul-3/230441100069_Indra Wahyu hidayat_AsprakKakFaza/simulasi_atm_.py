# Program simulasi mesin ATM sederhana
# PIN terdiri dari 5 digit (XXYYY) berdasarkan NIM
# User memiliki 3 kesempatan untuk memasukkan PIN dengan benar

print("=== SIMULASI MESIN ATM ===")

# Meminta input NIM pengguna untuk membuat PIN
nim = input("Masukkan NIM Anda: ")

# Validasi panjang NIM minimal 5 digit
if len(nim) < 5:
    print("NIM terlalu pendek! Pastikan NIM memiliki minimal 5 digit.")
else:
    # Membentuk PIN dari 2 angka awal dan 3 angka terakhir NIM
    pin_benar = int(nim[:2] + nim[-3:])
    print(f"(PIN Anda adalah kombinasi XXYYY dari NIM: {pin_benar})\n")

    kesempatan = 3  # Jumlah percobaan

    # Perulangan hingga 3 kali percobaan
    for percobaan in range(1, kesempatan + 1):
        try:
            pin = int(input(f"Percobaan ke-{percobaan}: Masukkan PIN (5 digit): "))

            # Cek panjang PIN
            if len(str(pin)) != 5:
                print("❗ PIN harus terdiri dari 5 digit angka!\n")
                continue

            # Cek apakah PIN benar
            if pin == pin_benar:
                print("✅ PIN benar, akses diterima.")
                break
            else:
                print("❌ PIN salah, coba lagi.\n")

        except ValueError:
            print("❗ Input tidak valid! Masukkan angka saja.\n")

    else:
        # Jika sudah 3 kali gagal
        print("🔒 Akses ditolak, kartu diblokir.")

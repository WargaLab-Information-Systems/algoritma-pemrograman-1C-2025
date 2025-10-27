# # Simulasi sederhana mesin ATM

# pin_benar = 25041
# kesempatan = 3

# print("=== Simulasi Mesin ATM ===")

# for i in range(kesempatan):
#     pin = input("Masukkan PIN (5 digit): ")

#     # Cek apakah input hanya angka
#     if not pin.isdigit():
#         print("PIN harus berupa angka!\n")
#         continue

#     # Ubah ke integer agar bisa dibandingkan
#     pin = int(pin)

#     if pin == pin_benar:
#         print("PIN benar, akses diterima")
#         break
#     else:
#         sisa = kesempatan - (i + 1)
#         if sisa > 0:
#             print(f"PIN salah, coba lagi. Kesempatan tersisa: {sisa}\n")
#         else:
#             print("Akses ditolak, kartu diblokir ")




























# Simulasi sederhana mesin ATM

pin_benar = 25041
kesempatan = 3

print("=== Simulasi Mesin ATM ===")

for i in range(kesempatan):
    pin_input = input("Masukkan PIN (5 digit): ")

    # Cek apakah input berupa angka
    if not pin_input.isdigit():
        sisa = kesempatan - (i + 1)
        if sisa > 0:
            print(f"PIN harus berupa angka! Kesempatan tersisa: {sisa}\n")
        else:
            print("PIN harus berupa angka! Akses ditolak, kartu diblokir ")
        continue

    pin = int(pin_input)

    if pin == pin_benar:
        print("PIN benar, akses diterima")
        break
    else:
        sisa = kesempatan - (i + 1)
        if sisa > 0:
            print(f"PIN salah, coba lagi. Kesempatan tersisa: {sisa}\n")
        else:
            print("Akses ditolak, kartu diblokir")

pin = "25143"
kesempatan = 3
print("Masukkan PIN anda (5 digit angka):")
for i in range(kesempatan):
    pin_input = input(f"Percobaan {i+1}/{kesempatan}: ")
    if not (pin_input and len(pin_input) == 5):
        print("PIN harus berupa 5 digit angka. Coba lagi.")
        continue
    if pin_input == pin:
        print("PIN benar, akses diterima")
        exit()
    else:
        print("PIN salah, coba lagi")
print("Akses ditolak, kartu di blokir")
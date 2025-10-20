# Simulasi mesin ATM

pin_benar = "25087"  
kesempatan = 3

for i in range(kesempatan):
    pin = input("Masukkan PIN (5 digit): ")
    
    if not pin.isdigit() or len(pin) != 5:
        print("PIN harus berupa 5 digit angka!")
        continue
    
    if pin == pin_benar:
        print("PIN benar, akses diterima.")
        break
    else:
        print("PIN salah, coba lagi.")
else:
    print("Akses ditolak, kartu diblokir.")

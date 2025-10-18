#===NO2===
#membuat simulasi sederhana di ATM
correct_pin = "25099"  # Ganti sesuai NIM

#Kesempatan mencoba PIN
percobaan = 3

while percobaan > 0:
    pin = input("Masukkan PIN (5 digit angka): ")
    
    # Cek apakah PIN 5 digit dan angka
    if not pin.isdigit(): #karna harus 5 digit dan harus berupa angka maka menggunakan (or not pin.isdigit())
        print("PIN harus 5 digit angka")
        continue
    
    if pin == correct_pin:
        print("PIN benar, akses diterima")
        break
    else:
        percobaan = percobaan - 1
        print("PIN salah, coba lagi")
        print("Sisa kesempatan:", percobaan)

if percobaan == 0:
    print("Akses ditolak, kartu diblokir")
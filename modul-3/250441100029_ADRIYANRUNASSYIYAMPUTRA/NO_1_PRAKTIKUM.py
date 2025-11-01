print("=== PROGRAM BILANGAN PRIMA ===")
n = int(input("Masukkan nilai n: "))

print(f"Bilangan prima dari 1 sampai {n}:")


jumlah_prima = 0


for angka in range(2, n + 1):

    is_prima = True
    

    for pembagi in range(2, angka):# semua kemungkinan di coba karena setiap for pembagi angka selalu reset mengikuti for angka , atau ini adalah perulangan terakhir dan semua kemungkinan di coba sampai program terjalankan
        if angka % pembagi == 0:
            is_prima = False
            break  
    

    if is_prima:
        print(angka, end=" ")
        jumlah_prima = jumlah_prima + 1

print(f"\nTotal ada {jumlah_prima} bilangan prima")
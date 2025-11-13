# Meminta input jumlah baris lampu
jumlah_baris = int(input("masukkan jumlah baris lampu: "))

# Loop untuk setiap baris
for baris in range(1, jumlah_baris + 1):
    # Meminta input jumlah lampu pada baris tersebut
    jumlah_lampu = int(input(f"masukkan jumlah lampu pada baris {baris}: "))
    
    # Loop untuk setiap lampu pada baris
    for lampu in range(1, jumlah_lampu + 1):
        if lampu % 3 == 0:
            # Jika lampu kelipatan 3, rusak
            print(f"lampu ke-{lampu} pada baris {baris} rusak")
        else:
            # Jika bukan kelipatan 3, menyala
            print(f"lampu ke-{lampu} pada baris {baris} menyala")
    
    # Jika ini baris terakhir, tambahkan pesan periksa sambungan daya
    if baris == jumlah_baris:
        print("periksa sambungan daya utama")

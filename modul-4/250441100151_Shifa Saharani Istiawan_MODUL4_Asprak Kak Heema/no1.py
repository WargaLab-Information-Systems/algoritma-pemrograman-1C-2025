# Meminta input jumlah baris lampu
n = int(input("Masukkan jumlah baris lampu: "))
# Inisialisasi nomor lampu global
total_lamps = 0
# Loop untuk setiap baris
for i in range(1, n + 1):
    # Meminta input jumlah lampu di baris i
    lamps_in_row = int(input(f"Masukkan jumlah lampu di baris {i}: "))
    
    # Loop untuk setiap lampu di baris i
    for j in range(1, lamps_in_row + 1):
        x = total_lamps + j  # Nomor lampu global
        if x % 3 == 0:
            print(f"Lampu ke-{x} pada baris {i} rusak.")
        else:
            print(f"Lampu ke-{x} pada baris {i} menyala.")
    
    # Update total lampu
    total_lamps += lamps_in_row
    
    # Jika baris terakhir, tambahkan pesan
    if i == n:
        print("Periksa sambungan daya utama.")
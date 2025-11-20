# Program untuk menampilkan kondisi lampu di taman kota

# Meminta input jumlah baris lampu
n = int(input("Masukkan jumlah baris lampu: "))

total_lampu = 0

# Loop untuk setiap baris
for i in range(1, n + 1):
    m = int(input(f"Masukkan jumlah lampu di baris {i}: "))
    
    for j in range(1, m + 1):
        total_lampu += 1
    
        x = total_lampu
        if j % 3 == 0:
            print(f"Lampu ke-{x} pada baris {i} rusak.")
        else:
            print(f"Lampu ke-{x} pada baris {i} menyala.")
    
    if i == n:
        print("Periksa sambungan daya utama.")


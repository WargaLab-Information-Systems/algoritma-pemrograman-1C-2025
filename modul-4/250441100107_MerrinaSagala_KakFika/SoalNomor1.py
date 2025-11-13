#PROGRAM LAMPU TAMAN KOTA

# Meminta input jumlah baris lampu
n = int(input("Masukkan jumlah baris lampu: ")) #mengulang proses berdasarkan jumlah baris lampu

# Inisialisasi nomor lampu global
total_lampu = 0 

# Loop untuk setiap baris
for i in range(1, n + 1): #perulangan mulai dari 1 sampai jumlah baris 
    
    # Meminta input jumlah lampu di baris i
    lampu_yang_dalam = int(input(f"Masukkan jumlah lampu di baris {i}: ")) 
    
    # Loop untuk setiap lampu di baris i
    for j in range(1, lampu_yang_dalam + 1): #mengatur jumlah lampu pada setaip baris
        x = total_lampu + j  # Nomor lampu global
        if x % 3 == 0: 
            print(f"Lampu ke-{x} pada baris {i} rusak.") #bilanagan x habis dibagi 3 maka lampu akan rusak
        else:
            print(f"Lampu ke-{x} pada baris {i} menyala.") # selain itu lampu nyala
    
    # Update total lampu
    total_lampu += lampu_yang_dalam #menambahkan jumlah lampu yang sudah diproses

    # Jika baris terakhir, tambahkan pesan
    if i == n: 
        print("Periksa sambungan daya utama.")

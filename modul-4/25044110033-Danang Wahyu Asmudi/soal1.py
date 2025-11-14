# Meminta input jumlah baris lampu
jumlah_baris = int(input("Masukkan jumlah baris lampu: "))
# Memproses setiap baris lampu
for baris in range(1, jumlah_baris + 1):
    jumlah_lampu = int(input(f"Masukkan jumlah lampu pada baris {baris}: "))
    # Memeriksa kondisi setiap lampu di baris tersebut
    for lampu in range(1, jumlah_lampu + 1):
        if lampu % 3 == 0:
            print(f"Lampu ke-{lampu} pada baris {baris} rusak.")
        else:
            print(f"Lampu ke-{lampu} pada baris {baris} menyala.")
    # Tambahkan pesan khusus jika ini adalah baris terakhir
    if baris == jumlah_baris:
        print("Periksa sambungan daya utama.")
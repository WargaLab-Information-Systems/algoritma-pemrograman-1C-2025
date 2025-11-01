# Program Kondisi Lampu di Taman Kota

jumlah_baris = int(input("Masukkan jumlah baris lampu: "))
nomor_lampu = 0

for y in range(1, jumlah_baris + 1):
    print(f"\nBaris ke-{y}:")
    jumlah_lampu = int(input(f"Masukkan jumlah lampu pada baris ke-{y}: "))

    for x in range(1, jumlah_lampu + 1):
        nomor_lampu += 1
        if nomor_lampu % 3 == 0:
            print(f"Lampu ke-{nomor_lampu} pada baris {y} rusak.")
        else:
            print(f"Lampu ke-{nomor_lampu} pada baris {y} menyala.")
        
    if y == jumlah_baris:
        print("Periksa sambungan daya utama.")


jumlah_baris = int(input("Masukkan jumlah baris lampu: "))

for baris in range(1, jumlah_baris + 1):
    jumlah_lampu = int(input(f"\nMasukkan jumlah lampu pada baris {baris}: "))
    print(f"\n--- Kondisi Lampu pada Baris {baris} ---")

    for lampu in range(1, jumlah_lampu + 1):
        if lampu % 3 == 0:
            print(f"Lampu ke-{lampu} pada baris {baris} rusak.")
        else:
            print(f"Lampu ke-{lampu} pada baris {baris} menyala.")

    if baris == jumlah_baris:
        print("\nPeriksa sambungan daya utama.")

print("\nPemeriksaan selesai")

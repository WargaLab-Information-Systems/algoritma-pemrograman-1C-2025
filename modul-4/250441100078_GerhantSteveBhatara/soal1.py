j_baris = int(input("Masukkan jumlah baris lampu: "))

for y in range(1, j_baris + 1):
    j_lampu = int(input(f"Masukkan jumlah lampu pada baris ke-{y}: "))

    for x in range(1, j_lampu + 1):
        if x % 3 == 0:
            print(f"Lampu ke-{x} pada baris {y} rusak.")
        else:
            print(f"Lampu ke-{x} pada baris {y} menyala.")

    if y == j_baris:
        print("Periksa sambungan daya utama.\n")
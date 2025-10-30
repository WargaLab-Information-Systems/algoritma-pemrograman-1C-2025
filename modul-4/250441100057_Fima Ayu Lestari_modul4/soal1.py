baris = int(input("Masukkan jumlah baris lampu: "))

for y in range(1, baris + 1):
    lampu = int(input(f"Jumlah lampu di baris {y}: "))
    for x in range(1, lampu + 1):
        if x % 3 == 0:
            kondisi = "rusak"
        else:
            kondisi = "menyala"
        print(f"Lampu ke-{x} pada baris {y} {kondisi}.")
    if y == baris:
        print("Periksa sambungan daya utama.")



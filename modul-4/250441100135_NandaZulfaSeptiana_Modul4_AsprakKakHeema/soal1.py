baris = int(input("Jumlah baris lampu : "))

for y in range(1, baris + 1):
    lampu = int(input(f"Jumlah lampu baris {y} : "))

    for x in range(1, lampu + 1):
        if x % 3 == 0:
            print(f"Lampu ke-{x} pada baris {y} rusak.")
        else:
            print(f"Lampu ke-{x} pada baris {y} menyala.")
   
    if y == baris:
        print("Periksa sambungan daya utama.")

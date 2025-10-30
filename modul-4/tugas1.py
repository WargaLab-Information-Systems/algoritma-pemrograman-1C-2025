baris_lampu = int(input("masukkan jumlah baris lampu:"))

for y in range(1, baris_lampu + 1):
    print(f"baris {y}:")

    lampu = int(input(f"masukkan jumlah lampu di baris {y}:"))
    for x in range(1, lampu + 1):
        if x % 3 == 0:
            print(f"lampu ke-{x} pada baris {y} rusak")
        else:
            print(f"lampu ke-{x} pada baris {y} menyala")

    if y == baris_lampu:
        print("periksa sambungan daya utama")
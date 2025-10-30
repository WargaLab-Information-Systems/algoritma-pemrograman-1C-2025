# Program: Pemantauan Lampu di Taman Kota

baris = int(input("Masukkan jumlah baris lampu: "))
y = 1

while y <= baris:
    lampu = int(input(f"Masukkan jumlah lampu pada baris ke-{y}: "))
    x = 1

    while x <= lampu:
        kondisi = "rusak" if x % 3 == 0 else "menyala"
        print(f"Lampu ke-{x} pada baris {y} {kondisi}.")
        x += 1

    if y == baris:
        print("Periksa sambungan daya utama.")

    y += 1

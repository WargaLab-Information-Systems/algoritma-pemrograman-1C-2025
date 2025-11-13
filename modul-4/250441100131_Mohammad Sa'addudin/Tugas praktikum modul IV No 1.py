jumlah_baris = int(input("masukkan jumlah baris lampu: "))
nomor_lampu = 1

for baris in range(1, jumlah_baris + 1):
    jumlah_lampu = int(input(f"masukkan jumlah lampu untuk baris ke-{baris}: "))

    for i in range(1, jumlah_lampu + 1):
        if nomor_lampu %3 == 0:
            print(f"lampu ke-{nomor_lampu} pada baris {baris} rusak")
        else:
            print(f"lampu ke-{nomor_lampu} pada baris {baris} menyala")

        nomor_lampu += 1
    if baris == jumlah_baris:
        print("periksa sambungan daya utama")
#soal 1
jumlah_baris = int(input("Masukkan jumlah baris lampu: "))
for nomor_baris in range(1, jumlah_baris + 1):
    print("Masukkan jumlah lampu pada baris ke-", nomor_baris, ": ", end="")
    jumlah_lampu = int(input())
    # Perulangan untuk setiap lampu
    for nomor_lampu in range(1, jumlah_lampu + 1):
        if nomor_lampu % 3 == 0:
            print("Lampu ke-", nomor_lampu, "pada baris", nomor_baris, "rusak.")
        else:
            print("Lampu ke-", nomor_lampu, "pada baris", nomor_baris, "menyala.")
    # Jika baritambahkan pesan tambahan
    if nomor_baris == jumlah_baris:
        print("Periksa sambungan daya utama.")
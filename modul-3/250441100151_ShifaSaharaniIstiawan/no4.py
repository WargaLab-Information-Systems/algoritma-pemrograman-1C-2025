# Program menampilkan struk pembelian IndoMei

while True:
    nama = input("Masukkan nama pembeli: ")
    daftar_barang = []
    total = 0

    while True:
        barang = input("Masukkan nama barang: ")
        harga = float(input(f"Masukkan harga {barang}: "))
        daftar_barang.append((barang, harga))
        total += harga

        lagi = input("Tambah barang lagi? (y/n): ")
        if lagi == 'n':
            break


    print("\n===== STRUK PEMBELIAN =====")
    print(f"Nama Pembeli: {nama}")
    print("----------------------------")
    for barang, harga in daftar_barang:
        print(f"{barang:20} Rp{harga:,.0f}")
    print("----------------------------")
    print(f"Total Harga:       Rp{total:,.0f}")
    print("Terima kasih telah berbelanja di IndoMei.")
    print("============================\n")

    pembeli_berikut = input("Apakah ada pembeli berikutnya? (y/n): ")
    if pembeli_berikut == 'n':
        print("Sistem kasir IndoMei ditutup. Terima kasih!")
        break
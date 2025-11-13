while True:
    nama = input("Masukkan nama pembeli: ")
    jumlah_barang = int(input("Masukkan jumlah barang: "))

    daftar_barang = []
    total = 0

    for i in range(jumlah_barang):
        nama_barang = input(f"Nama barang {i+1}: ")
        harga = float(input(f"Harga {nama_barang}: "))
        daftar_barang += [(nama_barang, harga)]
        total += harga
 
    print("\n=== STRUK PEMBELIAN INDoMEI ===")
    print(f"Customer : {nama}")
    print("------------------------------")
    for barang, harga in daftar_barang:
        print(f"{barang:20} Rp{harga:,.0f}")
    print("------------------------------")
    print(f"Total Harga   : Rp{total:,.0f}")
    print("\nTerima kasih telah berbelanja di IndoMei.\n")

    lanjut = input("Apakah ada pembeli berikutnya? (y/n): ")
    if lanjut == 'y':
        continue
    else:
        print("Selesai!")
        break

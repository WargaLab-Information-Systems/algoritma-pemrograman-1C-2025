while True:
    nama = input("Masukkan nama pembeli: ")
    daftar_barang = []
    total = 0

    while True:
        barang = str(input("Masukkan nama barang (atau ketik 'selesai' untuk berhenti): "))
        if barang == "selesai" or barang == "Selesai" or barang == "SELESAI":
            break
        harga = int(input(f"Masukkan harga {barang}: Rp "))
        daftar_barang.append((barang))
        total += harga

    print("\n===== STRUK PEMBELIAN INDOMEI =====")
    print("Nama Pembeli :", nama)
    print("-----------------------------------")
    for b, h in daftar_barang:
        print(f"{b:20} Rp {h}")
    print("-----------------------------------")
    print("Total Harga : Rp", total)
    print("Terima kasih telah berbelanja di IndoMei!")
    print("===================================\n")

    lanjut = input("Apakah ada pembeli berikutnya? (y/n): ")
    if lanjut == "n" or lanjut == "N":
        print("Program selesai.")
        break

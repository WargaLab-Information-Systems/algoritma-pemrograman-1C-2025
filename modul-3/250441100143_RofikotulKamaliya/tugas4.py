while True:
    nama = input("Masukkan nama pembeli: ")
    daftar_barang = []
    total = 0
    print("Masukkan nama dan harga barang satu per satu.")
    print("Ketik 'selesai' untuk mengakhiri input barang.\n")
    while True:
        nama_barang = input("Nama barang: ")
        if nama_barang == "selesai":
            break
        try:
            harga = int(input("Harga barang: "))
        except ValueError:
            print("Harga harus berupa angka! Ulangi input barang.")
            continue
        daftar_barang.append((nama_barang, harga))
        total += harga
    print("\n====== STRUK PEMBELIAN ======")
    print(f"Nama Pembeli: {nama}")
    print("\nDaftar Barang:")
    for barang, harga in daftar_barang:
        print(f"- {barang}: Rp{harga}")
    print(f"\nTotal Harga: Rp{total}")
    print("Terima kasih telah berbelanja di IndoMei.")
    lanjut = input("\nApakah ada pembeli berikutnya? (y/n): ")
    if lanjut != 'y':
        print("Program selesai.")
        break
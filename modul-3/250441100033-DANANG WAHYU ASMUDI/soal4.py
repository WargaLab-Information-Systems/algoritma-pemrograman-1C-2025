while True:
    nama = input("Masukkan nama pembeli: ")
    jumlah_barang = int(input("Jumlah barang yang dibeli: "))

    total = 0
    nomor = 1
    daftar = ""  #  untuk menyimpan daftar barang dalam bentuk teks

    while nomor <= jumlah_barang:
        nama_barang = input("Nama barang ke-" + str(nomor) + ": ")
        harga_barang = int(input("Harga barang: "))
        total = total + harga_barang
        daftar = daftar + str(nomor) + ". " + nama_barang + " : Rp" + str(harga_barang) + "\n"
        nomor = nomor + 1

    print("\n=== STRUK PEMBELIAN IndoMei ===")
    print("Nama pembeli:", nama)
    print("Daftar barang yang dibeli:\n" + daftar)
    print("Total harga: Rp", total)
    print("Terima kasih telah berbelanja di IndoMei.")

    lanjut = input("\nApakah ada pembeli berikutnya? (y/n): ")
    if lanjut == "n":
        break
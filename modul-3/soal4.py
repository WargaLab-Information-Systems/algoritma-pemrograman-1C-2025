while True:
    print("=== Program Struk Pembelian IndoMei ===")
    nama = input("Masukkan nama pembeli: ")
    jumlah_barang = int(input("Berapa jumlah barang yang dibeli? "))
    daftar_barang = []
    total_harga = 0

    for i in range(jumlah_barang):
        print(f"Barang ke-{i+1}")
        nama_barang = input("Nama barang  : ")
        harga_barang = int(input("Harga barang : "))
        daftar_barang.append((nama_barang, harga_barang))
        total_harga += harga_barang

    print("=== STRUK PEMBELIAN ====")
    print(f"Nama pembeli: {nama}")
    
    print("Daftar Barang:")
    for barang, harga in daftar_barang:
        print(f"- {barang}: Rp{harga}")

    print(f"Total harga: Rp{total_harga}")
    print("Terima kasih telah berbelanja di IndoMei.")
    lanjut = input("Apakah ada pembeli berikutnya? (y/n): ")
    if lanjut != 'y':
        break


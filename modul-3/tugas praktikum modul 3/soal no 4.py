while True:
    nama_pembeli = input("masukkan nama pembeli: ")
    daftar_barang = []
    total_harga = 0

    while True:
        nama_barang = input("masukkan nama barang (ketik 'selesai' jika sudah): ")
        if nama_barang == 'selesai':
            break
        harga_barang = float(input(f"masukkan harga {nama_barang}: "))
        daftar_barang.append({'nama': nama_barang, 'harga': harga_barang})
        total_harga += harga_barang

    print("\n" + "="*30)
    print("struk pembelian Indomei")
    print("="*30)
    print(f"nama pembeli: {nama_pembeli}")
    print("-"*30) 
    print("daftar barang:")

    for barang in daftar_barang:
        print(f"- {barang['nama']}: Rp{barang['harga']:,}")
    print("-"*30)
    print(f"total harga keseluruhan: Rp{total_harga:,}")
    print("="*30)
    print("terima kasih telah berbelanja di IndoMei.")
    print("="*30 + "\n")

    tanya_lagi = input("apakah ada pembeli berikutnya? (y/n): ")
    if tanya_lagi() == 'n':
        break
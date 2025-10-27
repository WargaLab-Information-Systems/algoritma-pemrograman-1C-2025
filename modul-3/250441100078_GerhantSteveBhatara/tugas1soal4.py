while True:
    nama = input("Nama pembeli:")
    total = 0
    
    while True:
        barang = input("Nama barang: ")
        harga = int(input("Harga barang: "))
        jumlah = int(input("Jumlah barang: "))
        total += harga * jumlah
        
        lagi = input("Tambah barang lain? (ya/tidak): ").lower()
        if lagi == "tidak":
            break
        
    print("=== STRUK PEMBELIAN ===")
    print("Nama pembeli:", nama)
    print("Total belanja: Rp", total)
    print("Terimakasih telah berbelanja di IndoMei!\n")
        
    lanjut = input("Apakah ada pembeli berikut? (ya/tidak): ").lower()
    if lanjut == "tidak":
        print("Program selesai.")
        break
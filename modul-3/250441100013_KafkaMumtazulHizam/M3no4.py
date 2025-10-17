while True:
    print("=== Selamat Datang Di Toko Kami ===")
    nama = input("Masukkan nama pembeli: ")

    th = 0
    db = ""
    
    jb = int(input("Berapa jumlah barang yang akan dibeli? "))

    for i in range(jb):
        print(f"Barang ke-{i+1}:")
        b = input("Nama barang: ")
        h = int(input("Harga barang: "))
        th += h
        db += f"{b:15} Rp {h}\n"

    print("========= Struk Pembelian ========")
    print(f"Nama pembeli : {nama}")
    print("-----------------------------------")
    print(db)
    print("-----------------------------------")
    print(f"Total harga barang anda sebesar Rp {th}")
    print("Terima kasih telah berbelanja di toko kami.")
    print("===================================")

    lagi = input("Apakah ada pembeli berikutnya? (ya/tidak): ")
    if lagi.lower() == "tidak":
        break
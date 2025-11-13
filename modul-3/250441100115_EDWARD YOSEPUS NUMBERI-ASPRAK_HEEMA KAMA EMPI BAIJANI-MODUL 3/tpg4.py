# Program struk pembelian IndoMei

while True:
    nama_pembeli = input("Masukkan nama pembeli: ")
    total = 0
    daftar_barang = []

    while True:
        barang = input("Nama barang (atau ketik 'selesai'): ")
        if barang  == 'selesai':
            break
        harga = float(input(f"Harga {barang}: "))
        daftar_barang.append((barang, harga))
        total += harga

    print(" STRUK PEMBELIAN ")
    print(f"Nama Pembeli: {nama_pembeli}") 

    for b, h in daftar_barang:
        print(f"{b:15} Rp{h:,.0f}")

    print(f"Total harga : Rp{total:,.0f}")
    print("Terima kasih telah berbelanja di IndoMei!")

    lagi = input("Apakah ada pembeli berikutnya? (y/n): ")
    if lagi != "y":
        print("Program selesai.")
        break
  
    
while True:
    print("\n--- TRANSAKSI BARU ---")
    nama_pembeli = input("Nama Pembeli: ")
    
    daftar_item = [] 
    while True:
        nama_barang = input("Barang (ketik 'done' jika selesai): ")
        if nama_barang.lower() == 'done':
            break
        harga = float(input("Harga barang: "))
        daftar_item.append((nama_barang, harga)) 
    
    # hasil
    print("======== STRUK IndoMei ========")
    print(f"Pembeli: {nama_pembeli}")
    print("-"*31)
    
    total = 0
    for item, harga_item in daftar_item:
        print(f"- {item:<20} Rp {harga_item:,.2f}")
        total += harga_item

    print("-"*31)
    print(f"Total Belanja: Rp {total:,.2f}")
    print("="*31)
    print("Terima kasih telah berbelanja di IndoMei")
    print("="*31)

    # perulangan
    while True:
        lanjut = input("Ada pembeli berikutnya? (y/n): ").lower()
        if lanjut in ('y', 'n'):
            break
        print("Salah, silahkan coba lagi.")

    if lanjut == 'n':
        break

print("Program selesai.")

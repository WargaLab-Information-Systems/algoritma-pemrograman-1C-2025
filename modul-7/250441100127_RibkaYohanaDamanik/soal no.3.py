kupon = {
    "HEMAT10": 10,
    "DISKON20": 20,
    "SALE50": 50
}

while True:
    print("\n=== SISTEM KUPON DISKON ===")
    print("1. Tampilkan kupon tersedia")
    print("2. Proses transaksi")
    print("3. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        if not kupon:
            print("Tidak ada kupon tersedia.")
        else:
            for kode, diskon in kupon.items():
                print(f"Kode: {kode}, Diskon: {diskon}%")

    elif pilihan == "2":
        try:
            total = float(input("Masukkan total belanja: "))
        except ValueError:
            print("Input harus berupa angka!")
            continue

        kode = input("Masukkan kode kupon: ").upper()

        if kode in kupon:
            diskon = kupon[kode]
            potongan = total * (diskon / 100)
            total_bayar = total - potongan

            print(f"Diskon {diskon}% diterapkan. Total bayar: Rp {total_bayar}")
            
            # Hapus kupon setelah dipakai
            del kupon[kode]
            print("Kupon telah digunakan dan dihapus.")
        else:
            print("Kupon tidak valid atau sudah dipakai.")

    elif pilihan == "3":
        print("Keluar...")
        break

    else:
        print("Menu tidak valid.")

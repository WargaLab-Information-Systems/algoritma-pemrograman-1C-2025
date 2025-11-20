kupon = {
    "DISKON10": 10,
    "MURAH20": 20,
    "GILA50": 50
}

while True:
    print("\n===== MENU =====")
    print("1. Tampilkan Semua Kupon")
    print("2. Proses Transaksi")
    print("3. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        if not kupon:
            print("Tidak ada kupon yang tersedia.")
        else:
            print("\n=== Daftar Kupon Tersedia ===")
            for kode, diskon in kupon.items():
                print(f"{kode} - Diskon {diskon}%")

    elif pilihan == "2":
        total_input = input("Masukkan total belanja (angka saja): ")

        if total_input.replace(".", "", 1).isdigit():
            total = float(total_input)
        else:
            print("Input total belanja tidak valid!")
            continue

        kode = input("Masukkan kode kupon: ").upper()

        if kode in kupon:
            diskon = kupon[kode]
            potongan = total * (diskon / 100)
            total_bayar = total - potongan

            print(f"\nKupon valid! Diskon: {diskon}%")
            print(f"Potongan: Rp {potongan:,.0f}")
            print(f"Total bayar: Rp {total_bayar:,.0f}")

            del kupon[kode]
            print("\nKupon telah digunakan dan dihapus dari sistem.")
        else:
            print("Kode kupon tidak valid atau sudah digunakan!")

    elif pilihan == "3":
        print("Terima kasih berbelanja disini!")
        break

    else:
        print("Pilihan tidak valid.")

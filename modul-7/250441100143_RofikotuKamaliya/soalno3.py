kupon_diskon = {
    "HEMAT10": 10,
    "DISKON20": 20,
    "SALE50": 50
}
while True:
    print("\n=== SISTEM KASIR - VALIDASI KUPON ===")
    print("1. Transaksi")
    print("2. Tampilkan Semua Kupon")
    print("3. Keluar")
    pilihan = input("Pilih menu: ")
    if pilihan == "1":
        while True:
            try:
                total = float(input("Masukkan total belanja: Rp "))
                if total < 0:
                    print("Total belanja tidak boleh negatif.")
                elif total == 0:
                    print("Total belanja tidak boleh 0. Masukkan nilai lebih dari 0.")
                else:
                    break
            except ValueError:
                print("Masukkan angka yang valid.")
        kode_kupon = input("Masukkan kode kupon: ").upper()
        if kode_kupon in kupon_diskon:
            diskon = kupon_diskon[kode_kupon]
            potongan = total * (diskon / 100)
            total_bayar = total - potongan
            print("\nKupon valid!")
            print(f"Diskon       : {diskon}%")
            print(f"Potongan     : Rp {potongan:,.2f}")
            print(f"Total Bayar  : Rp {total_bayar:,.2f}")
            del kupon_diskon[kode_kupon]
            print("Kupon telah digunakan dan sekarang dihapus.")
        else:
            print("\nKupon tidak valid atau sudah digunakan!")
    elif pilihan == "2":
        if not kupon_diskon:
            print("Tidak ada kupon tersedia.")
        else:
            print("\n=== DAFTAR KUPON TERSEDIA ===")
            for kode, diskon in kupon_diskon.items():
                print(f"Kode : {kode}")
                print(f"Diskon : {diskon}%")
            print("----------------------------")
    elif pilihan == "3":
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid.")

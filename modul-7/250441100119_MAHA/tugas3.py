kupon = {
    "DISCOUNT10": 10,
    "HEMAT20": 20,
    "PROMO5": 5
}

def tampilkan_kupon():
    if not kupon:
        print("Tidak ada kupon tersedia.")
    else:
        print("Daftar Kupon Tersedia:")
        for kode in kupon:
            print("Kode:", kode, "- Diskon:", kupon[kode], "%")
    print()

def proses_transaksi():
    total = float(input("Masukkan total belanja: "))

    if total == 0:
        print("Total belanja 0, tidak menggunakan kupon.")
        print("Total yang harus dibayar: 0")
        print()
        return

    kode = input("Masukkan kode kupon: ")

    if kode in kupon:
        diskon = kupon[kode]
        potongan = total * diskon / 100
        total_bayar = total - potongan

        print("Kupon valid!")
        print("Diskon:", diskon, "%")
        print("Total potongan:", potongan)
        print("Total yang harus dibayar:", total_bayar)

        del kupon[kode]
        print("Kupon telah digunakan dan dihapus.")
    else:
        print("Kupon tidak valid atau sudah digunakan.")
        print("Total yang harus dibayar:", total)
    print()

while True:
    print("MENU KUPON DISKON")
    print("1. Tampilkan Semua Kupon")
    print("2. Proses Transaksi")
    print("3. Keluar")

    pilihan = input("Pilih menu (1-3): ")

    if pilihan == "1":
        tampilkan_kupon()
    elif pilihan == "2":
        proses_transaksi()
    elif pilihan == "3":
        print("Terima kasih.")
        break
    else:
        print("Pilihan tidak valid.")
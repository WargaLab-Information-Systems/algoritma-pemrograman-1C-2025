kupon = {
    "promo10": 10,
    "diskon20": 20,
    "promo5": 5,
    "bigsale": 40,
    "weekend": 30
}

def tampilkan_kupon():
    if not kupon:
        print("\nTidak ada kupon tersedia.\n")
    else:
        print("\n--- Daftar Kupon Tersedia ---")
        for kode, diskon in kupon.items():
            print(f"Kode: {kode}  |  Diskon: {diskon}%")
        print()

def proses_transaksi():
    nama = input("\nMasukkan nama pembeli: ")

    try:
        total = float(input("Masukkan total belanja: Rp "))
    except ValueError:
        print("Input tidak valid! Masukkan angka.\n")
        return

    kode = input("Masukkan kode kupon (Opsional): ").lower()

    diskon = 0
    potongan = 0

    if kode == "":
        print("\nPembeli tidak menggunakan kupon.\n")

    elif kode not in kupon:
        print("\nKupon tidak valid atau sudah digunakan!\n")

    else:
        diskon = kupon[kode]
        potongan = total * (diskon / 100)
        del kupon[kode]
        print(f"\nKupon '{kode}' berhasil digunakan.\n")

    total_bayar = total - potongan

    try:
        bayar = float(input("Masukkan uang pembayaran: Rp "))
    except ValueError:
        print("Input tidak valid! Masukkan angka.\n")
        return

    if bayar < total_bayar:
        print("\nUang tidak cukup! Transaksi dibatalkan.\n")
        return

    kembalian = bayar - total_bayar

    print("\n===== STRUK BELANJA =====")
    print(f"Total Belanja : Rp {total}")
    print(f"Diskon        : {diskon}%")
    print(f"Potongan      : Rp {potongan}")
    print(f"Total Bayar   : Rp {total_bayar}")
    print(f"Uang Bayar    : Rp {bayar}")
    print(f"Kembalian     : Rp {kembalian}")
    print("==========================\n")

while True:
    print("""
=== SISTEM VALIDASI KUPON DISKON ===
1. Tampilkan semua kupon
2. Proses transaksi
3. Keluar
""")

    pilih = input("Pilih menu (1-3): ")

    if pilih == "1":
        tampilkan_kupon()
    elif pilih == "2":
        proses_transaksi()
    elif pilih == "3":
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid!\n")
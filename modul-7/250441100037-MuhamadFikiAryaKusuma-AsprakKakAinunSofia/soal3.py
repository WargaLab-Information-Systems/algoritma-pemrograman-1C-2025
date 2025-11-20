def tampilkan_kupon(coupons):
    if not coupons:
        print("\nTidak ada kupon yang tersedia.\n")
    else:
        print("\n=== Daftar Kupon Tersedia ===")
        for kode, diskon in coupons.items():
            print(f"Kode Kupon : {kode} | Diskon : {diskon}%")
        print()

def proses_transaksi(coupons):
    try:
        total = float(input("Masukkan total belanja: "))
    except ValueError:
        print("Input total belanja tidak valid.\n")
        return

    kode = input("Masukkan kode kupon: ")

    if kode not in coupons:
        print("\nKupon tidak valid atau sudah digunakan.")
        print(f"Total belanja tanpa diskon: Rp {total}\n")
        return

    # Jika kupon valid
    diskon = coupons[kode]
    potongan = total * (diskon / 100)
    total_bayar = total - potongan

    print(f"\nKupon valid! Diskon {diskon}% diterapkan.")
    print(f"Total belanja : Rp {total}")
    print(f"Potongan      : Rp {potongan}")
    print(f"Total bayar   : Rp {total_bayar}\n")

    # Hapus kupon setelah dipakai
    del coupons[kode]
    print("Kupon telah digunakan dan dihapus dari sistem.\n")


def main():
    coupons = {
        "DISC10": 10,
        "HEMAT20": 20,
        "SUPER50": 50
    }

    while True:
        print("=== MENU SISTEM KUPON DISKON ===")
        print("1. Tampilkan Semua Kupon")
        print("2. Proses Transaksi dengan Kupon")
        print("3. Keluar")

        pilihan = input("Pilih menu (1-3): ")

        if pilihan == '1':
            tampilkan_kupon(coupons)
        elif pilihan == '2':
            proses_transaksi(coupons)
        elif pilihan == '3':
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Coba lagi.\n")

main()
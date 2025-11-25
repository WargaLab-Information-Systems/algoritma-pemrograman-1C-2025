kupon = {
    "HEMAT10": 10,
    "DISKON25": 25,
    "PROMO50": 50
}


def tampilkan_kupon():
    print("\n=== Daftar Kupon Tersedia ===")
    if not kupon:
        print("Tidak ada kupon tersedia.")
    else:
        for kode, diskon in kupon.items():
            print(f"Kode: {kode} | Diskon: {diskon}%")


def proses_transaksi():
    print("\n=== Proses Transaksi ===")

    total_input = input("Masukkan total belanja (angka bulat): Rp ")

    if not total_input.isdigit():
        print("Input harus berupa angka bulat!")
        return

    total = int(total_input)

    kode = input("Masukkan kode kupon: ").upper()

    if kode in kupon:  
        diskon = kupon[kode]
        potongan = total * diskon / 100
        total_bayar = total - potongan

        print(f"\nKupon valid! Diskon {diskon}% digunakan.")
        print(f"Potongan : Rp {int(potongan)}")
        print(f"Total bayar setelah diskon : Rp {int(total_bayar)}")

        del kupon[kode]
        print("\nKupon telah dihapus, tidak bisa digunakan lagi.")
    else:
        print("\nKode kupon tidak valid atau sudah digunakan.")
        print(f"Total bayar : Rp {total}")


# ===== MENU UTAMA =====
while True:
    print("\n=== SISTEM KASIR VALIDASI KUPON ===")
    print("1. Tampilkan semua kupon")
    print("2. Proses transaksi")
    print("3. Keluar")

    pilihan = input("Pilih menu (1-3): ")

    if pilihan == "1":
        tampilkan_kupon()
    elif pilihan == "2":
        proses_transaksi()
    elif pilihan == "3":
        print("Program selesai. Terima kasih!")
        break
    else:
        print("Pilihan tidak valid! Silakan pilih menu 1-3.")
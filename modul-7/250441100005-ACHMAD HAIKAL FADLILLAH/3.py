kupon_diskon = {
    "DISKON11": 10,
    "SUPER11": 20,
    "HEMAT11": 5
}

def tampilkan_kupon():
    print("\n=== DAFTAR KUPON TERSEDIA ===")
    if not kupon_diskon:
        print("Tidak ada kupon tersisa.")
    else:
        for kode, diskon in kupon_diskon.items():
            print(f"Kode: {kode} | Diskon: {diskon}%")

def proses_transaksi():
    print("\n=== PROSES TRANSAKSI ===")
    try:
        total_belanja = float(input("Masukkan total belanja: "))
    except ValueError:
        print("Input tidak valid! Total belanja harus angka.")
        return
    
    kode = input("Masukkan kode kupon: ").upper()

    if kode not in kupon_diskon:
        print("Kupon tidak valid atau sudah digunakan!")
        return

    diskon = kupon_diskon[kode]
    potongan = (diskon / 100) * total_belanja
    total_bayar = total_belanja - potongan

    print(f"\nKupon valid! Diskon {diskon}%")
    print(f"Potongan: Rp {potongan:.2f}")
    print(f"Total yang harus dibayar: Rp {total_bayar:.2f}")

    del kupon_diskon[kode]
    print("Kupon berhasil digunakan dan dihapus dari daftar.")

def menu():
    while True:
        print("\n=== SISTEM KUPON DISKON ===")
        print("1. Tampilkan Semua Kupon")
        print("2. Proses Transaksi Menggunakan Kupon")
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
            print("Pilihan tidak valid!")

# Jalankan program
menu()

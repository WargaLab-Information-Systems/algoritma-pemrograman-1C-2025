kupon = {
    "hemat10": 10,
    "diskon20": 20,
    "sale50": 50
}

def tampil_kupon():
    if not kupon:
        print("Tidak ada kupon tersedia.")
    else:
        print("\nDaftar Kupon:")
        for k, d in kupon.items():
            print(f"- {k} : {d}%")

def proses_transaksi():
    try:
        total = float(input("Masukkan total belanja: "))
    except:
        print("Total belanja harus angka!")
        return

    if total == 0:
        print("Total belanja 0. Tidak perlu menggunakan kupon.")
        print("Total yang harus dibayar: Rp 0")
        return

    kode = input("Masukkan kode kupon: ").lower()

    if kode in kupon:
        diskon = kupon[kode]
        potongan = total * diskon / 100
        bayar = total - potongan

        print(f"Kupon valid! Diskon {diskon}%")
        print(f"Total potongan: Rp {potongan}")
        print(f"Total bayar: Rp {bayar}")

        del kupon[kode]  
        print(f"Kupon {kode} telah dihapus dan tidak bisa digunakan lagi.")
    else:
        print("Kupon tidak valid atau sudah dipakai!")
        print(f"Total bayar tanpa kupon: Rp {total}")   # ← TAMBAHAN

def menu():
    while True:
        print("\n=== MENU KUPON DISKON ===")
        print("1. Tampilkan semua kupon")
        print("2. Proses transaksi")
        print("3. Keluar")

        pilih = input("Pilih menu: ")

        if pilih == "1":
            tampil_kupon()
        elif pilih == "2":
            proses_transaksi()
        elif pilih == "3":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid!")

menu()

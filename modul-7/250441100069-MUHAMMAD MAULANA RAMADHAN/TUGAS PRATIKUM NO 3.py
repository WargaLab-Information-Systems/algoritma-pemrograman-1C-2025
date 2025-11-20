kupon = {
    "DISKON10": 10,
    "HEMAT20": 20,
    "SUPER30": 30,
    "SPESIAL50": 50,
    "FLASHSALE70": 70,
}

def tampilkan_kupon():
    if not kupon:
        print("\nTidak ada kupon yang tersedia.")
    else:
        print("\n=== Daftar Kupon Tersedia ===")
        for kode, diskon in kupon.items():
            print(f"Kode : {kode} | Diskon : {diskon}%")
        print("------------------------------")

def proses_transaksi():
    while True:

        while True:
            try:
                total = float(input("\nMasukkan total belanja: "))
                if total <= 0:
                    print("Total belanja harus lebih dari 0!")
                else:
                    break
            except ValueError:
                print("Input harus berupa angka!")

        punya_kupon = input("Apakah kamu mempunyai kupon? (y/n): ").strip().lower()

        if punya_kupon == "y":
            if not kupon:
                print("\nTidak ada kupon yang tersedia!")
                print("Transaksi akan diproses tanpa diskon.")
                print(f"Total Dibayar : Rp {total:.2f}")
                break

            kode = input("Masukkan kode kupon: ").strip().upper()

            if kode in kupon:
                diskon = kupon[kode]
                potongan = total * (diskon / 100)
                total_bayar = total - potongan

                print("\n=== Kupon Valid ===")
                print(f"Total Belanja     : Rp {total:.2f}")
                print(f"Diskon ({diskon}%)      : Rp {potongan:.2f}")
                print(f"Total Dibayar     : Rp {total_bayar:.2f}")

                del kupon[kode]
                print("\nKupon telah digunakan!")
                break

            else:
                print("\nKode kupon tidak valid atau sudah terpakai!")
                print("Silahkan ulangi transaksi.\n")

        elif punya_kupon == "n":
            print("\n=== TRANSAKSI TANPA KUPON ===")
            print(f"Total Belanja  : Rp {total:.2f}")
            print(f"Total Dibayar  : Rp {total:.2f}")
            print("\nTransaksi selesai tanpa diskon.")
            break

        else:
            print("Input harus (y/n)!")

while True:
    print("\n=== SISTEM VALIDASI KUPON DISKON ===")
    print("1. Tampilkan semua kupon")
    print("2. Proses transaksi")
    print("3. Keluar")

    pilihan = input("Pilih menu (1-3): ")

    if pilihan == "1":
        tampilkan_kupon()
    elif pilihan == "2":
        proses_transaksi()
    elif pilihan == "3":
        print("\nProgram selesai")
        break
    else:
        print("\nPilihan tidak valid!")

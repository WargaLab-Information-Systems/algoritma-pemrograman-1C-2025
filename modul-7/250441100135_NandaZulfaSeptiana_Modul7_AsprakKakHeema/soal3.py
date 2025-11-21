kupon = {
    "HEMAT10": 10,
    "POTONG20": 20,
    "DISKON50": 50
}

def tampilkan_kupon():
    print("\n--- Kupon Tersedia ---")
    if not kupon:
        print("Tidak ada kupon.")
        return
    
    for k, v in kupon.items():
        print(f"{k} : {v}%")

def proses_transaksi():
    try:
        total = float(input("Total belanja: Rp "))
    except ValueError:
        print("Masukkan angka yang benar!")
        return

    kode = input("Masukkan kode kupon: ")

    if kode in kupon:
        diskon = kupon[kode]
        potongan = total * diskon / 100
        total_bayar = total - potongan

        print(f"Kupon valid! Diskon {diskon}%")
        print(f"Potongan: Rp {potongan:,.2f}")
        print(f"Total bayar: Rp {total_bayar:,.2f}")

        del kupon[kode]
    else:
        print("Kupon tidak valid atau sudah digunakan.")

def menu():
    tampilkan_kupon()

    while True:
        print("\n===== PILIH SALAH SATU =====")
        print("1. Proses Transaksi")
        print("2. Keluar")

        pilih = input("Pilih (1-2): ")

        if pilih == "1":
            proses_transaksi()
            tampilkan_kupon()  
        elif pilih == "2":
            print("Selesai. Terima kasih!")
            break
        else:
            print("Pilihan salah.")

menu()

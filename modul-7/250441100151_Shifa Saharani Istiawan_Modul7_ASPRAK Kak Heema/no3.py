# Dictionary kupon: kode : diskon(%)
kupon = {
    "DISC10": 10,
    "HEMAT20": 20,
    "SALE30": 30
}

def tampil_kupon():
    if not kupon:
        print("Tidak ada kupon tersedia.\n")
    else:
        for k, d in kupon.items():
            print(f"{k} = {d}%")
        print()

def proses_transaksi():
    try:
        total = float(input("Total belanja: "))
    except:
        print("Masukkan angka yang benar!\n")
        return

    kode = input("Masukkan kode kupon: ").strip()

    if kode not in kupon:
        print("Kupon tidak valid atau sudah dipakai!\n")
        return

    diskon = kupon[kode] #mengambilnilai diskon dlm persen
    potongan = total * (diskon / 100)
    bayar = total - potongan

    print(f"Kupon berlaku! Diskon {diskon}%")
    print(f"Total setelah diskon: {bayar}\n")

    del kupon[kode]  # kupon dihapus setelah dipakai
    print("Kupon telah dihapus (tidak bisa dipakai lagi).\n")

while True:
    print("1. Tampilkan kupon")
    print("2. Proses transaksi")
    print("3. Keluar")
    p = input("Pilih menu: ")

    if p == "1": tampil_kupon()
    elif p == "2": proses_transaksi()
    elif p == "3": break
    else: print("Pilihan tidak valid!\n")
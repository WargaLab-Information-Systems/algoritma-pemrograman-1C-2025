kupon = {
    "DISC10": 10,
    "HEMAT20": 20,
    "PROMO5": 5
}

def tampil():
    if not kupon: print("Tidak ada kupon tersedia."); return
    for k, d in kupon.items(): 
        print(f"{k} -> {d}%") 

def transaksi():
    total = float(input("Total belanja: "))
    kode = input("Kode kupon: ").upper()

    if kode not in kupon: 
        print("Kupon tidak valid atau sudah digunakan.")
        return

    diskon = kupon[kode]
    total_bayar = total - (total * diskon / 100) 
    print(f"Diskon {diskon}% digunakan. Total bayar: {total_bayar:.2f}")

    del kupon[kode]  
    print("Kupon berhasil digunakan dan dihapus.")

def menu():
    while True:
        print("\n1. Tampilkan Kupon  2. Proses Transaksi  3. Keluar")
        p = input("Pilih: ")

        if p == "1": tampil()
        elif p == "2": transaksi()
        elif p == "3": break
        else: print("Pilihan tidak valid")

menu()
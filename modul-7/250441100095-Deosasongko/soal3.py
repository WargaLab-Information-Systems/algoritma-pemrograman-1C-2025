# # Dictionary kupon: kode : diskon(%)
# kupon = {
#     "DISC10": 10,
#     "HEMAT20": 20,
#     "SALE30": 30
# }

# def tampil_kupon():
#     if not kupon:
#         print("Tidak ada kupon tersedia.\n")
#     else:
#         for k, d in kupon.items():
#             print(f"{k} = {d}%")
#         print()

# def proses_transaksi():
#     try:
#         total = float(input("Total belanja: "))
#     except:
#         print("Masukkan angka yang benar!\n")
#         return

#     # Menanyakan apakah punya kupon
#     punya = input("Apakah Anda punya kupon? (y/n): ").strip().lower()

#     # Jika tidak punya → langsung bayar penuh
#     if punya == "n":
#         print(f"Total yang harus dibayar: {total}\n")
#         return

#     # Jika jawabannya bukan y atau n
#     if punya not in ["y", "n"]:
#         print("Pilihan tidak valid!\n")
#         return

#     # Jika punya kupon → wajib masukkan kupon sampai benar
#     while True:
#         kode = input("Masukkan kode kupon: ").strip()

#         # Jika kupon tidak ada dalam dictionary
#         if kode not in kupon:
#             print("Kupon tidak valid! Coba lagi.\n")
#             continue

#         # Jika kupon sudah dipakai (dicabut dari dictionary)
#         if kupon[kode] == "USED":
#             print("Kupon sudah dipakai!\n")
#             return

#         # Kupon valid → proses diskon
#         diskon = kupon[kode]
#         potongan = total * (diskon / 100)
#         bayar = total - potongan

#         print(f"\nKupon berlaku! Diskon {diskon}%")
#         print(f"Total setelah diskon: {bayar}\n")

#         # Menandai kupon sebagai sudah dipakai
#         kupon[kode] = "USED"
#         print("Kupon telah dihapus (tidak bisa dipakai lagi).\n")
#         return


# while True:
#     print("1. Tampilkan kupon")
#     print("2. Proses transaksi")
#     print("3. Keluar")
#     p = input("Pilih menu: ")

#     if p == "1": tampil_kupon()
#     elif p == "2": proses_transaksi()
#     elif p == "3": break
#     else: 
#         print("Pilihan tidak valid!\n")

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
    # Input nama barang
    nama_barang = input("Masukkan nama barang: ").strip()
    if not nama_barang.replace(" ", "").isalpha():
        print("Nama barang hanya boleh huruf!\n")
        return
    
    # Input total belanja
    try:
        total = float(input("Total belanja: "))
    except:
        print("Masukkan angka total belanja yang benar!\n")
        return

    # Menanyakan apakah punya kupon
    punya = input("Apakah Anda punya kupon? (y/n): ").strip().lower()

    # Jika tidak punya kupon → bayar penuh
    if punya == "n":
        print(f"\nNama barang      : {nama_barang}")
        print(f"Total dibayar    : {total}\n")
        return

    if punya not in ["y", "n"]:
        print("Pilihan tidak valid!\n")
        return

    # Jika punya kupon → harus masukkan kupon sampai benar
    while True:
        kode = input("Masukkan kode kupon: ").strip()

        # Jika kupon tidak ada
        if kode not in kupon:
            print("Kupon tidak valid! Silakan coba lagi.\n")
            continue

        # Jika kupon sudah dipakai
        if kupon[kode] == "USED":
            print("Kupon sudah dipakai!\n")
            return

        # Kupon valid → proses diskon
        diskon = kupon[kode]
        potongan = total * (diskon / 100)
        bayar = total - potongan

        print(f"\nNama barang         : {nama_barang}")
        print(f"Kupon berlaku       : {diskon}%")
        print(f"Total setelah diskon: {bayar}\n")

        # Tandai kupon sudah digunakan
        kupon[kode] = "USED"
        print("Kupon telah dihapus (tidak bisa dipakai lagi).\n")
        return


while True:
    print("1. Tampilkan kupon")
    print("2. Proses transaksi")
    print("3. Keluar")
    p = input("Pilih menu: ")

    if p == "1": tampil_kupon()
    elif p == "2": proses_transaksi()
    elif p == "3": break
    else:
        print("Pilihan tidak valid!\n")


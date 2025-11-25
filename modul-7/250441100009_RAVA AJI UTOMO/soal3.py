# Data kupon 
kode_diskon = {
    "hemat10": 10,
    "belanja20": 20,
    "promo50": 50
}

# Tampil kupon
def tampilkan_data():
    if not kode_diskon:
        print("Tidak ada kupon tersedia.")
    else:
        print("Daftar Kupon:")
        for kd, persen in kode_diskon.items():
            print(" ", kd, ":", persen, "%")

# Proses transaksi
def transaksi():
    total_input = input("Masukkan total belanja: ")
    total_belanja = float(total_input)
    kode_input = input("Masukkan kode kupon (kosongkan jika tidak ada): ")
    if kode_input == "":
        print("Total yang harus dibayar: Rp", total_belanja)
        return

    if kode_input in kode_diskon:
        nilai_diskon = kode_diskon[kode_input]
        potongan = total_belanja * (nilai_diskon / 100.0)
        final_total = total_belanja - potongan

        print("Kupon valid! Diskon", nilai_diskon, "%")
        print("Total setelah diskon: Rp", final_total)
        print("Kupon telah digunakan dan dihapus.")  
        
        del kode_diskon[kode_input]  # Hapus kupon
    else:
        print("Kupon tidak valid! Tidak ada diskon.")
        print("Total yang harus dibayar: Rp", total_belanja)

# Menu utama
def menu():
    while True:
        print("\n=== SISTEM KASIR ===")
        print("1. Tampilkan kupon")
        print("2. Proses transaksi")
        print("3. Keluar")

        pilih_menu = input("Pilih menu: ")

        if pilih_menu == "1":
            tampilkan_data()
        elif pilih_menu == "2":
            transaksi()
        elif pilih_menu == "3":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid.")

menu()
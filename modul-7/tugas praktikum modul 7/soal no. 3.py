kupon = {
    "HEMAT10": 10,
    "DISKON20": 20,
    "SUPER50": 50
}

def menampilkan_kupon():
    print("\n--- Kupon Tersedia ---")
    if not kupon:
        print("Tidak ada kupon tersedia saat ini.")
    else:
        for kode, diskon in kupon.items():
            print(f"Kode: {kode} | Diskon: {diskon}%")
    print("----------------------")

def proses_transaksi(total_pembelian, kode_kupon):
    if kode_kupon in kupon:
        diskon_persen = kupon[kode_kupon]
        diskon_jumlah = (total_pembelian * diskon_persen) / 100
        total_akhir = total_pembelian - diskon_jumlah
        print(f"\nKupon '{kode_kupon}' valid. Diskon {diskon_persen}%.")
        print(f"Jumlah diskon: Rp{diskon_jumlah:,.2f}")
        print(f"Total yang harus dibayar: Rp{total_akhir:,.2f}")
        
        del kupon[kode_kupon]
        print(f"Kupon '{kode_kupon}' telah dihapus.")
        return total_akhir
    else:
        print(f"\nKupon '{kode_kupon}' tidak valid atau sudah digunakan.")
        print(f"Total yang harus dibayar: Rp{total_pembelian:,.2f}")
        return total_pembelian

def menu():
    while True:
        print("\n===========================")
        print("Sistem Kasir Validasi Kupon")
        print("===========================")
        print("1. Tampilkan Kupon Tersedia")
        print("2. Proses Transaksi")
        print("3. Keluar")
        
        pilihan = input("Masukkan pilihan Anda (1/2/3): ")
        
        if pilihan == '1':
            menampilkan_kupon()
        elif pilihan == '2':
            try:
                total_pembelian = float(input("Masukkan total belanja (Rp): "))
                kode_kupon = input("Masukkan kode kupon: ")
                proses_transaksi(total_pembelian, kode_kupon)
            except ValueError:
                print("Input total belanja tidak valid. Harap masukkan angka.")
        elif pilihan == '3':
            print("Terima kasih telah menggunakan sistem kasir.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

menu()
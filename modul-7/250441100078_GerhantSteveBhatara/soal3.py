coupons = {
    "DISCOUNT10": 10.0,  # Contoh kupon 10%
    "SAVE20": 20.0,      # Contoh kupon 20%
    "HALFPRICE": 50.0    # Contoh kupon 50%
}  # Dictionary untuk menyimpan kupon

def display_menu(): #menampilkan menu display
    print("\n=== MENU VALIDASI KUPON DISKON ===")
    print("1. Tampilkan semua kupon yang tersedia")
    print("2. Proses transaksi")
    print("3. Cek apakah ada kupon")
    print("4. Keluar")

def display_coupons(): #menampilkan semua kupon yang tersedia
    if not coupons: #cek apakah dictionary kosong
        print("Tidak ada kupon yang tersedia.")
    else: #jika dictionary tidak kosong
        print("\n=== DAFTAR KUPON TERSEDIA ===")
        for code, discount in coupons.items(): #mengambil kode dan diskon dari kupon dictionary
            print(f"Kode: {code}, Diskon: {discount}%")

def check_coupons(): #fungsi baru untuk cek apakah ada kupon
    if not coupons:
        print("Tidak ada kupon yang tersedia.")
    else:
        print(f"Ada {len(coupons)} kupon yang tersedia.")

def process_transaction():
    while True:  # Loop utama untuk transaksi
        # Masukkan kode kupon dulu
        code = input("Masukkan kode kupon: ").strip().upper()  # Case-insensitive, ubah ke uppercase
        
        discount_percent = 0.0  # Default tanpa diskon
        if code in coupons: #cek apakah kode kupon ada di dictionary
            discount_percent = coupons[code] #mengambil persentase diskon dari dictionary
            print(f"Kupon {code} valid dengan diskon {discount_percent}%.")
        else:
            print("Kode kupon tidak valid atau sudah digunakan. Melanjutkan tanpa diskon.")
        
        # Sekarang tambahkan belanja
        total_purchase = 0.0
        while True:
            try:
                purchase = float(input("Masukkan total belanja (atau 0 untuk selesai menambah): ").strip())
                if purchase < 0:
                    print("Total belanja tidak boleh negatif.")
                    continue
                if purchase == 0:
                    break
                total_purchase += purchase
                print(f"Total belanja sementara: {total_purchase:.2f}")
                add_more = input("Ingin menambahkan total belanja lagi? (y/n): ").strip().lower()
                if add_more != 'y':
                    break
            except ValueError:
                print("Input total belanja tidak valid. Harus berupa angka.")
        
        if total_purchase == 0:
            print("Tidak ada transaksi yang diproses.")
            break  # Keluar jika tidak ada belanja
        
        # Hitung total dengan diskon
        discount_amount = total_purchase * (discount_percent / 100) #menghitung jumlah diskon
        total_to_pay = total_purchase - discount_amount
        if discount_percent > 0:
            print(f"Diskon {discount_percent}% diterapkan. Potongan: {discount_amount:.2f}")
        print(f"Total yang harus dibayar: {total_to_pay:.2f}")
        
        # Hapus kupon setelah digunakan
        if code in coupons:
            del coupons[code]
            print("Kupon telah digunakan dan dihapus.")
        
        # Tanya apakah ingin menambahkan belanja lagi (dengan kupon baru)
        add_more_purchase = input("Ingin menambahkan total belanja lagi (dengan kupon baru)? (y/n): ").strip().lower()
        if add_more_purchase != 'y':
            break  # Keluar dari loop utama

# Loop utama program
while True:
    display_menu()
    choice = input("Pilih opsi (1-4): ").strip()
    
    if choice == "1":
        display_coupons()
    elif choice == "2":
        process_transaction()
    elif choice == "3":
        check_coupons()
    elif choice == "4":
        print("Terima kasih telah menggunakan Sistem Validasi Kupon Diskon!")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")

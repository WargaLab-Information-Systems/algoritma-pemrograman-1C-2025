
while True:
    print("\n=== RENTAL MOTOR ACONK ===")
    print("1. Motor Matic  = Rp 50.000/hari")
    print("2. Motor Sport  = Rp 75.000/hari")
    print("3. Motor Trail  = Rp 100.000/hari")

    pilihan = input("Pilih jenis motor (1/2/3): ")
    hari = int(input("Lama sewa (hari): "))

    if pilihan == '1':
        harga = 50000
        jenis = "Motor Matic"
    elif pilihan == '2':
        harga = 75000
        jenis = "Motor Sport"
    elif pilihan == '3':
        harga = 100000
        jenis = "Motor Trail"
    else:
        print("Pilihan tidak valid, coba lagi.")
        continue

    
    subtotal = harga * hari

    
    if hari > 3:
        asuransi = 15000 * hari  
    else:
        asuransi = 0

    total = subtotal + asuransi

    
    if subtotal > 150000:
        diskon = subtotal * 0.10
    else:
        diskon = 0

    total -= diskon

    kupon = input("Masukkan kupon diskon (jika ada): ")
    if kupon == "AconkGG":
        tambahan_diskon = total * 0.05
        total -= tambahan_diskon
        print("Kupon berhasil digunakan! Diskon tambahan 5%.")
    else:
        print("Kupon tidak berlaku atau salah.")

    # hasil
    print("\n=== STRUK RENTAL MOTOR ===")
    print(f"Jenis Motor   : {jenis}")
    print(f"Lama Sewa     : {hari} hari")
    print(f"Harga Sewa    : Rp {harga:,}")
    print(f"Subtotal      : Rp {subtotal:,}")
    print(f"Asuransi      : Rp {asuransi:,}")
    print(f"Diskon        : Rp {diskon:,}")
    print(f"Total Bayar   : Rp {total:,}")

  
    ulang = input("\nApakah ingin melakukan penyewaan kembali? (y/n): ")
    if ulang.lower() == 'n':
        print("Terima kasih telah menggunakan Rental Motor Aconk!")
        break
    elif ulang.lower() != 'y':
        print("Input salah, program dihentikan.")
        break




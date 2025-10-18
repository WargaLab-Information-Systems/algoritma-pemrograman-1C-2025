# Program Struk Pembelian IndoMei
print("=== Program Struk Pembelian IndoMei ===")

while True:
    print("\n--- Input Data Pembeli ---")
    nama = input("Masukkan nama pembeli: ")

    daftar_barang = []
    daftar_harga = []

    while True:
        barang = input("Masukkan nama barang (ketik 'selesai' jika sudah): ")
        if barang.lower() == 'selesai':
            break
        harga = float(input(f"Masukkan harga {barang}: "))
        daftar_barang.append(barang)
        daftar_harga.append(harga)

    total = sum(daftar_harga)

    # Tampilkan struk
    print("\n=== Struk Pembelian IndoMei ===")
    print(f"Nama Pembeli : {nama}")
    print("-------------------------------")
    for i in range(len(daftar_barang)):
        print(f"{i+1}. {daftar_barang[i]:20} Rp{daftar_harga[i]:,.2f}")
    print("-------------------------------")
    print(f"Total Harga : Rp{total:,.2f}")
    print("Terima kasih telah berbelanja di IndoMei!")
    print("===============================")

    # Tanya apakah ada pembeli berikutnya
    lanjut = input("\nApakah ada pembeli berikutnya? (y/n): ")
    if lanjut.lower() != 'y':
        print("\nProgram selesai. Sampai jumpa!")
        breakse
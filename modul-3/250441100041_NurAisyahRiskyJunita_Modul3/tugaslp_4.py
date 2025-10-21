# Program struk pembelian IndoMei

lanjut = "y"

while lanjut == "y":
    print("\n===== STRUK PEMBELIAN INDOMEI =====")

    # Input nama pembeli
    nama = input("Masukkan nama pembeli: ")

    # Daftar barang dan harga
    daftar_barang = []
    daftar_harga = []

    # Input barang
    barang = ""
    while barang != "selesai":
        barang = input("Masukkan nama barang (ketik 'selesai' jika sudah): ")
        if barang != "selesai":
            harga = int(input("Masukkan harga barang: "))
            daftar_barang.append(barang)
            daftar_harga.append(harga)

    # Hitung total harga manual
    total = 0
    for h in daftar_harga:
        total = total + h

    # Tampilkan struk
    print("\n========== STRUK PEMBELIAN ==========")
    print("Nama Pembeli:", nama)
    print("------------------------------------")
    for i in range(len(daftar_barang)):
        print(str(i + 1) + ".", daftar_barang[i], "- Rp", daftar_harga[i])
    print("------------------------------------")
    print("Total Harga: Rp", total)
    print("Terima kasih telah berbelanja di toko ayies")
    print("=====================================")

    # Tanya apakah ada pembeli berikutnya
    lanjut = input("\nApakah ada pembeli berikutnya? (y/n): ")

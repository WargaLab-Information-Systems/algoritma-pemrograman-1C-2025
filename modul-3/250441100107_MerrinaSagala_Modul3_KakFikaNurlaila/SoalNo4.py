#SoalNomor Empat
print("Program struk pembelian IndoMei")

while True:
    # Input nama pembeli
    nama = input("Masukkan nama pembeli: ")

    daftar_barang = []
    daftar_harga = []

    while True:
        barang = input("Masukkan nama barang (ketik selesai jika sudah): ")
        if barang == "selesai":
            break
        harga = input("Masukkan harga barang: Rp")
        harga = int(harga)
        # Tambahkan barang dan harga ke list dengan cara manual
        daftar_barang = daftar_barang + [barang]
        daftar_harga = daftar_harga + [harga]

    # Tampilkan struk pembelian
    print("\nStruk Pembelian")
    print("Nama Pembeli:", nama)
    total_harga = 0
    for i in range(len(daftar_barang)):
        print(f"- {daftar_barang[i]}: Rp{daftar_harga[i]}")
        total_harga = total_harga + daftar_harga[i]
    print("Total Harga: Rp", total_harga)
    print("Terima kasih telah berbelanja di IndoMei.\n") #kita make /n agar hasil print dapat  tersususn kebawah

    # Tanya apakah ada pembeli berikutnya
    jawab = input("Apakah ada pembeli berikutnya? (yes/no): ")
    if jawab != "yes":
        break

print("Program selesai.")

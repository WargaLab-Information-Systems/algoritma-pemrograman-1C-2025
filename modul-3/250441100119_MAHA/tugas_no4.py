ulang = "y"

while ulang == "y" or ulang == "Y":
    print("program struk pembelian IndoMei")

    nama = input("masukkan nama pembeli:")
    total = 0
    daftar_barang = []

    jumlah_barang = int(input("masukkan jumlah barangnya yang dibeli:"))

    for i in range(jumlah_barang):
        print("barang ke-", i+1)
        nama_barang = input("nama barang:")
        harga = int(input("harga barang:"))
        daftar_barang.append((nama_barang, harga))
        total += harga

    print("STRUK PEMBELIAN")
    print("nama pembeli :", nama)

    for barang, harga in daftar_barang:
        print(f"{barang} Rp{harga}")

    print("total harga: Rp", total)
    print("terima kasih telah shopping di IndoMei")
    ulang = input("Apakah ada pembeli berikutnya? (y/n): ")
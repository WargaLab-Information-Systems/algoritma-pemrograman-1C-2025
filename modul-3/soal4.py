# Tugas no 4

print("= Struk Pembelian IndoMei =")

ulang = "y"

while ulang == "y":
    nama = input("\nMasukkan nama pembeli: ")

    total = 0

    print("Masukkan daftar barang (ketik 'selesai' jika sudah):")
    while True:
        barang = input("Nama barang: ")
        if barang == "selesai":
            break
        harga = int(input("Harga barang: "))
        total = total + harga
        print("Barang ditambahkan!\n")

    print("\n--- STRUK PEMBELIAN ---")
    print("Nama Pembeli:", nama)
    print("Total Harga : Rp", total)
    print("Terima kasih telah berbelanja di IndoMei.\n")

    ulang = input("Apakah ada pembeli berikutnya? (y/n): ")

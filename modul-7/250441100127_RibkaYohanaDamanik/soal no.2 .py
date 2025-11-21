inventaris = {}

while True:
    print("\n=== INVENTARIS GUDANG ===")
    print("1. Tampilkan semua barang")
    print("2. Cari barang berdasarkan ID")
    print("3. Tambah barang")
    print("4. Update stok barang")
    print("5. Hapus barang")
    print("6. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        if not inventaris:
            print("Barang masih kosong.")
        else:
            for id_brg, data in inventaris.items():
                print(f"ID: {id_brg}, Nama: {data[0]}, Harga: {data[1]}, Stok: {data[2]}")

    elif pilihan == "2":
        id_brg = input("Masukkan ID barang: ")
        if id_brg in inventaris:
            data = inventaris[id_brg]
            print(f"Nama: {data[0]}, Harga: {data[1]}, Stok: {data[2]}")
        else:
            print("Barang tidak ditemukan.")

    elif pilihan == "3":
        id_brg = input("ID Barang: ")
        nama = input("Nama Barang: ")
        harga = int(input("Harga: "))
        stok = int(input("Stok: "))
        inventaris[id_brg] = [nama, harga, stok]
        print("Barang berhasil ditambahkan.")

    elif pilihan == "4":
        id_brg = input("Masukkan ID barang yang ingin diupdate stoknya: ")
        if id_brg in inventaris:
            tambahan = int(input("Tambah/Kurang stok (boleh minus): "))
            if inventaris[id_brg][2] + tambahan < 0:
                print("Stok tidak boleh negatif!")
            else:
                inventaris[id_brg][2] += tambahan
                print("Stok berhasil diperbarui.")
        else:
            print("Barang tidak ditemukan.")

    elif pilihan == "5":
        id_brg = input("Masukkan ID barang yang ingin dihapus: ")
        if id_brg in inventaris:
            del inventaris[id_brg]
            print("Barang berhasil dihapus.")
        else:
            print("Barang tidak ditemukan.")

    elif pilihan == "6":
        print("Keluar...")
        break

    else:
        print("Menu tidak valid.")

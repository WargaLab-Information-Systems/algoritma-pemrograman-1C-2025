inventaris = {}
while True:
    print("\n=== INVENTARIS GUDANG ===")
    print("1. Tambah Barang")
    print("2. Perbarui Stok Barang")
    print("3. Cari Barang")
    print("4. Tampilkan Semua Barang")
    print("5. Hapus Barang")
    print("6. Keluar")
    pilihan = input("Pilih menu: ")
    if pilihan == "1":
        while True:
            print("\n=== TAMBAH BARANG ===")
            id_barang = input("ID barang: ")
            if id_barang in inventaris:
                print("ID sudah digunakan! Coba ID lain.")
                continue
            nama = input("Nama barang: ")
            while True:
                try:
                    harga = float(input("Harga barang: "))
                    if harga < 0:
                        print("Harga tidak boleh negatif.")
                    elif harga == 0:
                        print("Harga harus lebih dari 0.")
                    else:
                        break
                except ValueError:
                    print("Masukkan angka yang valid.")
            while True:
                try:
                    stok = int(input("Stok barang: "))
                    if stok < 0:
                        print("Stok tidak boleh negatif.")
                    elif stok == 0:
                        print("stok yang diinputkan harus ada.")
                    else:
                        break
                except ValueError:
                    print("Masukkan angka yang valid.")
            inventaris[id_barang] = [nama, harga, stok]
            print("Barang berhasil ditambahkan!")
            lanjut = input("Tambah barang lagi? (y/n): ")
            if lanjut != "y":
                break
    elif pilihan == "2":
        update = input("ID barang: ")
        if update not in inventaris:
            print("Barang tidak ditemukan.")
        else:
            nama, harga, stok = inventaris[update]
            print(f"Stok saat ini: {stok}")
            while True:
                try:
                    perubahan = int(input("Perubahan stok (+ tambah / - kurang): "))
                    if stok + perubahan < 0:
                        print("Stok tidak boleh negatif.")
                    else:
                        inventaris[update][2] = stok + perubahan
                        print("Stok berhasil diperbarui!")
                        break
                except ValueError:
                    print("Masukkan angka yang valid.")
    elif pilihan == "3":
        id_cari = input("ID barang: ")
        if id_cari in inventaris:
            nama, harga, stok = inventaris[id_cari]
            print(f"\nBarang ditemukan!")
            print(f"Nama : {nama}")
            print(f"Harga: {harga}")
            print(f"Stok : {stok}")
        else:
            print("Barang tidak ditemukan.")
    elif pilihan == "4":
        if not inventaris:
            print("Inventaris masih kosong.")
        else:
            print("\n=== DAFTAR BARANG ===")
            for id_barang, data in inventaris.items():
                print(f"ID    : {id_barang}")
                print(f"Nama  : {data[0]}")
                print(f"Harga : Rp {data[1]:,.2f}")
                print(f"Stok  : {data[2]}")
                print("------------------------")
    elif pilihan == "5":
        id_hapus = input("ID barang: ")
        if id_hapus in inventaris:
            del inventaris[id_hapus]
            print("Barang berhasil dihapus.")
        else:
            print("Barang tidak ditemukan.")
    elif pilihan == "6":
        print("Program selesai. Terimakasih!")
        break
    else:
        print("Pilihan tidak valid.")
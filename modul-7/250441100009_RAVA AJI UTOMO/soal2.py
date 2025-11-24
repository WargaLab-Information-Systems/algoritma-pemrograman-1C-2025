def manajemen_inventaris():
    inventaris = {}
    id_barang = 1

    while True:
        print("\n----MANAJEMEN INVENTARIS GUDANG----")
        print("1. Tampilkan Semua Barang")
        print("2. Cari Barang berdasarkan ID")
        print("3. Tambah Barang Baru")
        print("4. Perbarui Stok Barang")
        print("5. Hapus Barang")
        print("6. Keluar")
        pilihan = input("Pilih menu (1-6): ")

        # tampil semua barang
        if pilihan == '1':
            if not inventaris:
                print("Gudang kosong! Tidak ada barang.")
            else:
                print("\nDAFTAR BARANG DI GUDANG")
                for key, data in inventaris.items():
                    print("ID:", key, "| Nama:", data[0], "| Harga: Rp", data[1], "| Stok:", data[2], "unit")

        # cari barang
        elif pilihan == '2':
            cari_id = input("Masukkan ID barang: ")
            if cari_id in inventaris:
                data = inventaris[cari_id]
                print("\nBarang ditemukan")
                print("ID   :", cari_id)
                print("Nama :", data[0])
                print("Harga: Rp", data[1])
                print("Stok :", data[2], "unit")
            else:
                print("Barang dengan ID", cari_id, "tidak ditemukan.")

        # tambah barang
        elif pilihan == '3':
            nama = input("Masukkan nama barang: ")
            if nama == "":
                print("Nama tidak boleh kosong.")
                continue

            harga_input = input("Masukkan harga per unit (Rp): ")
            if not harga_input.isdigit():
                print("Harga harus angka!")
                continue
            harga = int(harga_input)
            if harga < 0:
                print("Harga tidak boleh negatif.")
                continue

            stok_input = input("Masukkan stok awal: ")
            if not stok_input.isdigit():
                print("Stok harus angka!")
                continue
            stok = int(stok_input)
            if stok < 0:
                print("Stok tidak boleh negatif.")
                continue

            inventaris[str(id_barang)] = [nama, harga, stok]
            print("Barang", nama, "(ID:", id_barang, ") berhasil ditambahkan.")
            id_barang += 1

        # update stok
        elif pilihan == '4':
            update_id = input("Masukkan ID barang: ")
            if update_id not in inventaris:
                print("Barang dengan ID", update_id, "tidak ditemukan.")
                continue

            stok_lama = inventaris[update_id][2]
            print("Stok saat ini:", stok_lama, "unit")

            perubahan_input = input("Masukkan perubahan stok: ")
            if not perubahan_input.lstrip("+-").isdigit():
                print("Perubahan stok harus angka dengan tanda + atau -.")
                continue

            if perubahan_input[0] in "+-":
                tanda = perubahan_input[0]
                angka = perubahan_input[1:]
                if angka.isdigit():
                    perubahan = int(perubahan_input)
                else:
                    print("Format perubahan tidak valid.")
                    continue
            else:
                if perubahan_input.isdigit():
                    perubahan = int(perubahan_input)
                else:
                    print("Perubahan stok tidak valid.")
                    continue

            stok_baru = stok_lama + perubahan
            if stok_baru < 0:
                print("Stok tidak boleh negatif.")
            else:
                inventaris[update_id][2] = stok_baru
                print("Stok berhasil diperbarui menjadi", stok_baru, "unit")

        # hapus barang
        elif pilihan == '5':
            hapus_id = input("Masukkan ID barang yang akan dihapus: ")
            if hapus_id in inventaris:
                nama_barang = inventaris[hapus_id][0]
                del inventaris[hapus_id]
                print("Barang", nama_barang, "berhasil dihapus.")
            else:
                print("Barang dengan ID", hapus_id, "tidak ditemukan.")

        # keluar
        elif pilihan == '6':
            print("Keluar dari program...")
            break
        else:
            print("Pilihan tidak valid.")

manajemen_inventaris()

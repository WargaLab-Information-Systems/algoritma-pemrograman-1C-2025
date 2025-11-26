inventaris = {}

def tampilkan_semua():
    print("\n=== DAFTAR SEMUA BARANG ===")
    if not inventaris:
        print("Tidak ada data barang.")
    else:
        for id_barang, info in inventaris.items():
            print(f"ID Barang : {id_barang}")
            print(f"Nama Barang : {info[0]}")
            print(f"Harga : {info[1]}")
            print(f"Stok : {info[2]}\n")

def cari_barang():
    print("\n=== CARI BARANG BERDASARKAN ID ===")
    id_barang = input("Masukkan ID barang: ")

    if id_barang in inventaris:
        info = inventaris[id_barang]
        print(f"ID Barang : {id_barang}")
        print(f"Nama Barang : {info[0]}")
        print(f"Harga : {info[1]}")
        print(f"Stok : {info[2]}")
    else:
        print("Barang tidak ditemukan!")

def tambah_barang():
    print("\n=== TAMBAH BARANG BARU ===")
    id_barang = input("Masukkan ID barang baru: ")

    if id_barang in inventaris:
        print("ID barang sudah ada!")
        return

    nama = input("Masukkan nama barang: ")
    harga = float(input("Masukkan harga barang: "))
    stok = int(input("Masukkan jumlah stok: "))

    inventaris[id_barang] = [nama, harga, stok]
    print("Barang berhasil ditambahkan!")

def update_stok():
    print("\n=== UPDATE STOK BARANG ===")
    id_barang = input("Masukkan ID barang: ")

    if id_barang not in inventaris:
        print("Barang tidak ditemukan!")
        return

    try:
        perubahan = int(input("Masukkan jumlah perubahan stok (+ menambah, - mengurangi): "))
    except ValueError:
        print("Input tidak valid!")
        return

    stok_sekarang = inventaris[id_barang][2]
    stok_baru = stok_sekarang + perubahan

    if stok_baru < 0:
        print("Gagal! Stok tidak boleh menjadi negatif.")
        return

    inventaris[id_barang][2] = stok_baru
    print("Stok berhasil diperbarui!")

def hapus_barang():
    print("\n=== HAPUS BARANG ===")
    id_barang = input("Masukkan ID barang yang ingin dihapus: ")

    if id_barang not in inventaris:
        print("Barang tidak ditemukan!")
        return

    del inventaris[id_barang]
    print("Barang berhasil dihapus!")


while True:
    print("\n=== INVENTARIS GUDANG ===")
    print("1. Tampilkan Semua Barang")
    print("2. Cari Barang Berdasarkan ID")
    print("3. Tambah Barang Baru")
    print("4. Update Stok Barang")
    print("5. Hapus Barang")
    print("6. Keluar")

    pilihan = input("Pilih menu (1-6): ")

    if pilihan == "1":
        tampilkan_semua()
    elif pilihan == "2":
        cari_barang()
    elif pilihan == "3":
        tambah_barang()
    elif pilihan == "4":
        update_stok()
    elif pilihan == "5":
        hapus_barang()
    elif pilihan == "6":
        print("Program selesai. Terima kasih!")
        break
    else:
        print("Pilihan tidak valid!")

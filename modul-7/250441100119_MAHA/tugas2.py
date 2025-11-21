inventory = {}

def tampilkan_semua():
    if not inventory:
        print("Belum ada data barang.")
    else:
        print("Daftar Barang:")
        for id_barang in inventory:
            print("ID Barang:", id_barang)
            print("Nama:", inventory[id_barang][0])
            print("Harga:", inventory[id_barang][1])
            print("Stok:", inventory[id_barang][2])
    print()

def cari_barang():
    id_barang = input("Masukkan ID barang yang dicari: ")
    if id_barang in inventory:
        print("Barang ditemukan:")
        print("ID Barang:", id_barang)
        print("Nama:", inventory[id_barang][0])
        print("Harga:", inventory[id_barang][1])
        print("Stok:", inventory[id_barang][2])
    else:
        print("Barang tidak ditemukan.")
    print()

def tambah_barang():
    id_barang = input("Masukkan ID barang baru: ")
    if id_barang in inventory:
        print("Barang dengan ID ini sudah ada.")
    else:
        nama = input("Masukkan nama barang: ")
        harga = input("Masukkan harga barang: ")
        stok = input("Masukkan jumlah stok barang: ")
        inventory[id_barang] = [nama, harga, int(stok)]
        print("Barang berhasil ditambahkan.")
    print()

def update_stok():
    id_barang = input("Masukkan ID barang yang ingin diperbarui stoknya: ")
    if id_barang in inventory:
        print("Stok saat ini:", inventory[id_barang][2])
        stok_baru = int(input("Masukkan stok baru: "))
        if stok_baru < 0:
            print("Stok tidak boleh negatif.")
        else:
            inventory[id_barang][2] = stok_baru
            print("Stok berhasil diperbarui.")
    else:
        print("Barang tidak ditemukan.")
    print()

def hapus_barang():
    id_barang = input("Masukkan ID barang yang ingin dihapus: ")
    if id_barang in inventory:
        del inventory[id_barang]
        print("Barang berhasil dihapus.")
    else:
        print("Barang tidak ditemukan.")
    print()

while True:
    print("MENU INVENTARIS GUDANG")
    print("1. Tampilkan Semua Barang")
    print("2. Cari Barang")
    print("3. Tambah Barang")
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
        print("Terima Kasih.")
        break
    else:
        print("Pilihan tidak valid.")
daftar_barang = {}

def tampilkan_semua():
    print("\n=== DAFTAR BARANG ===")
    if not daftar_barang:
        print("Belum ada barang.")
    else:
        for id, data in daftar_barang.items():
            print(f"{id} - {data[0]} - Harga: {data[1]} - Stok: {data[2]}")


def cari_barang():
    id = input("Masukkan ID barang: ")
    if id in daftar_barang:
        nama, harga, stok = daftar_barang[id]
        print(f"Nama: {nama}, Harga: {harga}, Stok: {stok}")
    else:
        print("Barang tidak ditemukan.")


def tambah_barang():
    id = input("ID Barang: ")
    nama = input("Nama Barang: ")
    harga = int(input("Harga: "))
    stok = int(input("Stok: "))

    daftar_barang[id] = [nama, harga, stok]
    print("Barang berhasil ditambahkan!")


def update_stok():
    id = input("ID Barang: ")
    if id not in daftar_barang:
        print("Barang tidak ditemukan.")
        return

    perubahan = int(input("Perubahan stok (+ / -): "))
    daftar_barang[id][2] += perubahan
    if daftar_barang[id][2] < 0:
        daftar_barang[id][2] = 0

    print("Stok diperbarui!")


def hapus_barang():
    id = input("ID Barang yang dihapus: ")
    if id in daftar_barang:
        del daftar_barang[id]
        print("Barang dihapus.")
    else:
        print("Barang tidak ditemukan.")


while True:
    print("\n=== PILIH SALAH SATU ===")
    print("1. Tampilkan semua barang")
    print("2. Cari barang")
    print("3. Tambah barang")
    print("4. Update stok")
    print("5. Hapus barang")
    print("6. Keluar")

    pilih = input("Pilih menu (1-6): ")

    if pilih == "1":
        tampilkan_semua()
    elif pilih == "2":
        cari_barang()
    elif pilih == "3":
        tambah_barang()
    elif pilih == "4":
        update_stok()
    elif pilih == "5":
        hapus_barang()
    elif pilih == "6":
        print("Keluar...")
        break
    else:
        print("Pilihan tidak valid.")

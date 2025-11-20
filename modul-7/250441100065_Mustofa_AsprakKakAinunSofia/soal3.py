inventaris = {}

def tampilkan_barang():
    if not inventaris:
        print("Belum ada data barang.\n")
        return
    
    print("\n--- Daftar Inventaris ---")
    for idb, data in inventaris.items():
        print(f"ID Barang : {idb}")
        print(f"Nama      : {data[0]}")
        print(f"Harga     : {data[1]}")
        print(f"Stok      : {data[2]}\n")

def cari_barang():
    idb = input("Masukkan ID Barang: ").lower()
    if idb in inventaris:
        print("\nData ditemukan:")
        print(f"ID    : {idb}")
        print(f"Nama  : {inventaris[idb][0]}")
        print(f"Harga : {inventaris[idb][1]}")
        print(f"Stok  : {inventaris[idb][2]}\n")
    else:
        print("Barang tidak ditemukan.\n")

def tambah_barang():
    idb = input("Masukkan ID Barang: ").lower()

    if idb in inventaris:
        print("ID Barang sudah ada! Gunakan ID lain.\n")
        return

    nama = input("Masukkan nama barang: ")

    try:
        harga = int(input("Masukkan harga barang: "))
        stok = int(input("Masukkan stok awal: "))
    except:
        print("Input harga/stok harus berupa angka!\n")
        return

    inventaris[idb] = [nama, harga, stok]
    print("Barang berhasil ditambahkan!\n")

def update_stok():
    idb = input("Masukkan ID Barang yang akan diperbarui stoknya: ").lower()

    if idb not in inventaris:
        print("Barang tidak ditemukan.\n")
        return

    try:
        perubahan = int(input("Masukkan penambahan/pengurangan stok: "))
    except:
        print("Input harus berupa angka!\n")
        return

    stok_sekarang = inventaris[idb][2]
    stok_baru = stok_sekarang + perubahan

    if stok_baru < 0:
        print("Stok tidak boleh negatif! Pembaruan dibatalkan.\n")
    else:
        inventaris[idb][2] = stok_baru
        print("Stok berhasil diperbarui.\n")

def hapus_barang():
    idb = input("Masukkan ID Barang yang akan dihapus: ").lower()

    if idb in inventaris:
        del inventaris[idb]
        print("Barang berhasil dihapus.\n")
    else:
        print("Barang tidak ditemukan.\n")

while True:
    print("""
=== MENU INVENTARIS GUDANG ===
1. Tampilkan Semua Barang
2. Cari Barang
3. Tambah Barang
4. Perbarui Stok Barang
5. Hapus Barang
6. Keluar
""")

    pilih = input("Pilih menu: ")

    if pilih == "1":
        tampilkan_barang()
    elif pilih == "2":
        cari_barang()
    elif pilih == "3":
        tambah_barang()
    elif pilih == "4":
        update_stok()
    elif pilih == "5":
        hapus_barang()
    elif pilih == "6":
        print("Program selesai. Terima kasih!")
        break
    else:
        print("Pilihan tidak valid.\n")

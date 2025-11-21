def tampilkan_barang(inventory):
    if not inventory:
        print("\nTidak ada data barang dalam inventaris.\n")
    else:
        print("\n=== Daftar Inventaris Gudang ===")
        for item_id, data in inventory.items():
            print(f"ID Barang : {item_id}")
            print(f"Nama      : {data[0]}")
            print(f"Harga     : {data[1]}")
            print(f"Stok      : {data[2]}\n")


def cari_barang(inventory):
    item_id = input("Masukkan ID barang yang dicari: ")

    if item_id in inventory:
        print("\nBarang ditemukan:")
        print(f"ID    : {item_id}")
        print(f"Nama  : {inventory[item_id][0]}")
        print(f"Harga : {inventory[item_id][1]}")
        print(f"Stok  : {inventory[item_id][2]}\n")
    else:
        print("\nBarang tidak ditemukan.\n")


def tambah_barang(inventory):
    item_id = input("Masukkan ID barang baru: ")

    if item_id in inventory:
        print("ID sudah digunakan. Gunakan ID lain.\n")
        return

    nama = input("Masukkan nama barang: ")

    try:
        harga = float(input("Masukkan harga barang: "))
        stok = int(input("Masukkan stok barang: "))
    except ValueError:
        print("Input harga atau stok tidak valid (harus angka).\n")
        return

    if stok < 0:
        print("Stok tidak boleh negatif.\n")
        return

    inventory[item_id] = [nama, harga, stok]
    print("Barang berhasil ditambahkan!\n")


def update_stok(inventory):
    item_id = input("Masukkan ID barang yang ingin diperbarui: ")

    if item_id not in inventory:
        print("Barang tidak ditemukan.\n")
        return

    print(f"\nData saat ini:")
    print(f"Nama  : {inventory[item_id][0]}")
    print(f"Harga : {inventory[item_id][1]}")
    print(f"Stok  : {inventory[item_id][2]}\n")

    nama_baru = input("Masukkan nama baru (Enter untuk skip): ")
    if nama_baru:  
        inventory[item_id][0] = nama_baru

    harga_input = input("Masukkan harga baru (Enter untuk skip): ")
    if harga_input: 
        try:
            harga_baru = int(harga_input)
            if harga_baru < 0:
                print("Harga tidak boleh negatif. Update dibatalkan.\n")
                return
            inventory[item_id][1] = harga_baru
        except ValueError:
            print("Input harga tidak valid. Update dibatalkan.\n")
            return

    stok_input = input("Masukkan perubahan stok (contoh: +5 atau -3, Enter untuk skip): ")
    if stok_input:  
        try:
            perubahan = int(stok_input)
        except ValueError:
            print("Input stok tidak valid.\n")
            return

        stok_baru = inventory[item_id][2] + perubahan

        if stok_baru < 0:
            print("Stok tidak boleh negatif. Update dibatalkan.\n")
            return

        inventory[item_id][2] = stok_baru

    print("\nData barang berhasil diperbarui!\n")
    
def hapus_barang(inventory):
    item_id = input("Masukkan ID barang yang ingin dihapus: ")

    if item_id not in inventory:
        print("Barang tidak ditemukan.\n")
        return

    del inventory[item_id]
    print("Barang berhasil dihapus!\n")


def main():
    inventory = {}

    while True:
        print("=== MENU INVENTARIS GUDANG ===")
        print("1. Tampilkan Semua Barang")
        print("2. Cari Barang")
        print("3. Tambah Barang Baru")
        print("4. Update Stok Barang")
        print("5. Hapus Barang")
        print("6. Keluar")

        pilihan = input("Pilih menu (1-6): ")

        if pilihan == '1':
            tampilkan_barang(inventory)
        elif pilihan == '2':
            cari_barang(inventory)
        elif pilihan == '3':
            tambah_barang(inventory)
        elif pilihan == '4':
            update_stok(inventory)
        elif pilihan == '5':
            hapus_barang(inventory)
        elif pilihan == '6':
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Coba lagi.\n")

main()
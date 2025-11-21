def tampilkan_menu():
    """Menampilkan opsi menu utama kepada pengguna."""
    print("\n=== MENU MANAJEMEN INVENTARIS===")
    print("1. Tampilkan semua barang")
    print("2. Cari barang berdasarkan ID")
    print("3. Tambahkan barang baru")
    print("4. Perbarui stok barang")
    print("5. Hapus barang")
    print("6. Keluar")
    print("=============================")

def input_id():
    """Meminta input ID dari pengguna dengan penanganan error."""
    while True:
        try:
            id_barang = int(input("Masukkan ID barang: "))
            return id_barang
        except ValueError:
            print("ID harus berupa angka. Coba lagi.")

def cek_barang_ada(id_barang, inventaris):
    """Memeriksa apakah barang dengan ID tertentu ada dalam inventaris."""
    return id_barang in inventaris

def tampilkan_semua_barang(inventaris):
    """Menampilkan semua barang dalam inventaris."""
    if not inventaris:
        print("Inventaris kosong.")
        return
    print("\n--- Daftar Barang ---")
    print(f"{'ID':<5} | {'Nama Barang':<20} | {'Harga':<10} | {'Stok':<5}")
    print("-" * 50)
    for id_barang, detail in inventaris.items():
        nama, harga, stok = detail
        print(f"{id_barang:<5} | {nama:<20} | {harga:<10} | {stok:<5}")

def cari_barang(inventaris):
    """Mencari dan menampilkan detail barang berdasarkan ID."""
    id_barang = input_id()
    if cek_barang_ada(id_barang, inventaris):
        nama, harga, stok = inventaris[id_barang]
        print("\n--- Detail Barang ---")
        print(f"ID: {id_barang}")
        print(f"Nama: {nama}")
        print(f"Harga: {harga}")
        print(f"Stok: {stok}")
    else:
        print(f"Barang dengan ID {id_barang} tidak ditemukan.")

def tambah_barang_baru(inventaris):
    """Menambahkan barang baru ke inventaris."""
    id_barang = input_id()
    if cek_barang_ada(id_barang, inventaris):
        print(f"Barang dengan ID {id_barang} sudah ada. Gunakan fungsi perbarui jika ingin mengubah stok.")
        return

    nama = input("Masukkan nama barang: ")
    while True:
        try:
            harga = float(input("Masukkan harga barang: "))
            stok = int(input("Masukkan stok barang: "))
            if stok < 0:
                print("Stok tidak boleh negatif. Coba lagi.")
                continue
            break
        except ValueError:
            print("Harga harus berupa angka dan stok harus berupa bilangan bulat. Coba lagi.")

    inventaris[id_barang] = [nama, harga, stok]
    print(f"Barang '{nama}' berhasil ditambahkan.")

def perbarui_stok_barang(inventaris):
    """Memperbarui stok barang yang sudah ada."""
    id_barang = input_id()
    if cek_barang_ada(id_barang, inventaris):
        while True:
            try:
                stok_baru = int(input("Masukkan jumlah stok baru: "))
                if stok_baru < 0:
                    print("Stok tidak boleh menjadi negatif. Coba lagi.")
                    continue
                
                inventaris[id_barang][2] = stok_baru
                print(f"Stok barang ID {id_barang} berhasil diperbarui menjadi {stok_baru}.")
                break
            except ValueError:
                print("Stok harus berupa bilangan bulat. Coba lagi.")
    else:
        print(f"Barang dengan ID {id_barang} tidak ditemukan.")

def hapus_barang(inventaris):
    """Menghapus barang dari inventaris."""
    id_barang = input_id()
    if cek_barang_ada(id_barang, inventaris):
        del inventaris[id_barang]
        print(f"Barang ID {id_barang} berhasil dihapus.")
    else:
        print(f"Barang dengan ID {id_barang} tidak ditemukan.")

def main():
    inventaris_gudang = {}
    while True:
        tampilkan_menu()
        pilihan = input("Masukkan pilihan Anda (1-6): ")

        if pilihan == '1':
            tampilkan_semua_barang(inventaris_gudang)
        elif pilihan == '2':
            cari_barang(inventaris_gudang)
        elif pilihan == '3':
            tambah_barang_baru(inventaris_gudang)
        elif pilihan == '4':
            perbarui_stok_barang(inventaris_gudang)
        elif pilihan == '5':
            hapus_barang(inventaris_gudang)
        elif pilihan == '6':
            print("Terima kasih telah menggunakan program manajemen inventaris. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid. Silakan masukkan angka antara 1 dan 6.")

if __name__ == "__main__":
    main()
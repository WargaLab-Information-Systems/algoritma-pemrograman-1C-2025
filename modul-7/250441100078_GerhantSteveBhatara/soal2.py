inventory = {}  # Dictionary untuk menyimpan inventaris

def display_menu(): #menu display
    print("\n=== MENU MANAJEMEN INVENTARIS GUDANG ===")
    print("1. Tampilkan semua barang")
    print("2. Cari barang berdasarkan ID")
    print("3. Tambah barang baru")
    print("4. Update stok barang")
    print("5. Hapus barang")
    print("6. Keluar")


def display_all_items(): #menampilkan semua barang
    if not inventory: #cek apakah dictionary kosong
        print("Tidak ada barang yang tersimpan.")
    else: #jika dictionary tidak kosong
        print("\n=== DAFTAR BARANG ===")
        for item_id, details in inventory.items():
            print(f"ID: {item_id}, Nama: {details[0]}, Harga: {details[1]}, Stok: {details[2]}")


def search_item(): #mencari barang berdasarkan ID
    item_id = input("Masukkan ID barang yang dicari: ").strip()
    if item_id in inventory: #cek apakah barang ada
        details = inventory[item_id] #mengambil detail barang berdasarkan ID di inventory
        print(f"ID: {item_id}, Nama: {details[0]}, Harga: {details[1]}, Stok: {details[2]}")
    else:
        print("Barang dengan ID tersebut tidak ditemukan.")


def add_item():  # menambah barang baru
    while True:  # loop untuk validasi ID barang
        item_id = input("Masukkan ID barang: ").strip()
        if item_id.isalnum():  # cek apakah ID barang hanya terdiri dari angka dan huruf
            break  # keluar dari loop jika valid
        else:
            print("ID barang hanya boleh berisi angka dan huruf. Silakan coba lagi.")  # pesan error jika invalid
    
    if item_id in inventory:  # cek apakah barang sudah ada
        print("Barang dengan ID tersebut sudah ada.")
    else:
        while True:  # loop untuk validasi nama barang
            name = input("Masukkan nama barang: ").strip()
            if name.isalpha():  # cek apakah nama barang hanya terdiri dari huruf
                break  # keluar dari loop jika valid
            else:
                print("Nama barang hanya boleh berisi huruf. Silakan coba lagi.")  # pesan error jika invalid
        
        try:
            price = float(input("Masukkan harga barang: ").strip())
            stock = int(input("Masukkan stok barang: ").strip())
            if stock < 1:
                print("Stok tidak boleh negatif.")
            else:
                inventory[item_id] = [name, price, stock]
                print("Barang berhasil ditambahkan.")
        except ValueError:
            print("Input harga atau stok tidak valid. Harus berupa angka.")



def update_stock(): #mengupdate stok barang
    item_id = input("Masukkan ID barang yang ingin diupdate stok-nya: ").strip()
    if item_id in inventory: #cek apakah barang ada
        try:
            new_stock = int(input("Masukkan stok baru: ").strip())
            if new_stock < 0:
                print("Stok tidak boleh negatif.")
            else:
                inventory[item_id][2] = new_stock
                print("Stok barang berhasil diupdate.")
        except ValueError: #menangani kesalahan jika input stok bukan angka bulat
            print("Input stok tidak valid. Harus berupa angka bulat.")
    else:
        print("Barang dengan ID tersebut tidak ditemukan.")


def delete_item(): #menghapus barang
    item_id = input("Masukkan ID barang yang ingin dihapus: ").strip()
    if item_id in inventory: #cek apakah barang ada
        del inventory[item_id]
        print("Barang berhasil dihapus.")
    else:
        print("Barang dengan ID tersebut tidak ditemukan.")


# Loop utama program
while True:
    display_menu() #menampilkan menu
    choice = input("Pilih opsi (1-6): ").strip()
    
    if choice == "1":
        display_all_items()
    elif choice == "2":
        search_item()
    elif choice == "3":
        add_item()
    elif choice == "4":
        update_stock()
    elif choice == "5":
        delete_item()
    elif choice == "6":
        print("Terima kasih telah menggunakan Manajemen Inventaris Gudang!")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")

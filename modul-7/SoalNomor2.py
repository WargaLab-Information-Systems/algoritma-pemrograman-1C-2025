# program manajemen inventaris gudang dengan fitur CRUD (Create,Read, Update, Delete)
inventaris = {}
#read
def tampilkan_semua_barang():
    if not inventaris:
        print("Inventaris kosong.")
    else:
        print("\nDaftar Barang:")
        for id_barang, data in inventaris.items(): #Melakukan iterasi pada setiap item
            print(f"ID: {id_barang}, Nama: {data[0]}, Harga: {data[1]}, Stok: {data[2]}")

def cari_barang():
    id_barang = input("Masukkan ID barang yang ingin dicari: ")
    if id_barang in inventaris:
        data = inventaris[id_barang] #mengambil data sesuai ID
        print(f"ID: {id_barang}, Nama: {data[0]}, Harga: {data[1]}, Stok: {data[2]}")
    else:
        print("Barang tidak ditemukan.")

#create
def tambah_barang():
    id_barang = input("Masukkan ID barang baru: ")
    if id_barang in inventaris:
        print("ID sudah digunakan. Gunakan ID lain.")
        return #menghentikan fungsi jika ID sudah ada
    nama = input("Masukkan nama barang: ")
    try: #Memulai blok coba untuk menangani input harga dan stok.
        harga = float(input("Masukkan harga barang: "))
        stok = int(input("Masukkan jumlah stok: "))
        if stok < 0:
            print("Stok tidak boleh negatif.")
            return #menghentikan fungsi jika stok negatif
        
        #create
        inventaris[id_barang] = [nama, harga, stok]
        print("Barang berhasil ditambahkan.")
    
    except ValueError:
        print("Input harga atau stok tidak valid.")
#update
def perbarui_stok():
    id_barang = input("Masukkan ID barang yang ingin diperbarui: ")
    if id_barang in inventaris:
        try: #Memulai blok penanganan error untuk input stok baru
            stok_baru = int(input("Masukkan jumlah stok baru: "))
            if stok_baru < 0:
                print("Stok tidak boleh negatif.")
                return #Menghentikan fungsi jika stok negatif
            
            #update
            inventaris[id_barang][2] = stok_baru
            print("Stok berhasil diperbarui.")
        except ValueError: #Menangkap error jika input stok baru tidak valid
            print("Input stok tidak valid.")
    else:
        print("Barang tidak ditemukan.")
#dalate
# fungsi untuk menghapus barang dari inventaris.
def hapus_barang():
    id_barang = input("Masukkan ID barang yang ingin dihapus: ")
    if id_barang in inventaris:
        del inventaris[id_barang] #Menghapus barang dari dictionary inventaris
        print("Barang berhasil dihapus.")
    else: #jika id tidak di temukan
        print("Barang tidak ditemukan.")

def menu():
    while True:
        print("\n=== Menu Manajemen Inventaris ===")
        print("1. Tampilkan semua barang")
        print("2. Cari barang berdasarkan ID")
        print("3. Tambah barang baru")
        print("4. Perbarui stok barang")
        print("5. Hapus barang")
        print("6. Keluar")

        pilihan = input("Pilih menu (1-6): ")

        # 1 sampai 5, menjalankan fungsi3
        
        if pilihan == '1':
            tampilkan_semua_barang()
        elif pilihan == '2':
            cari_barang()
        elif pilihan == '3':
            tambah_barang()
        elif pilihan == '4':
            perbarui_stok()
        elif pilihan == '5':
            hapus_barang()
        elif pilihan == '6':
            print("Terima kasih telah menggunakan program ini.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Menjalankan program
menu()

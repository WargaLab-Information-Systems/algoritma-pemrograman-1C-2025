inventaris = {}

def input_id(prompt):
    while True:
        id_barang = input(prompt).strip()

        if id_barang.isdigit() and int(id_barang) > 0:
            return id_barang 
        else:
            print("Silahkan masukkan angka!")

def cek_kosong():
    if not inventaris:
        print("\nBelum ada data barang yang dimasukkan!")
        return True
    return False

def tampilkan_semua():
    if cek_kosong():
        return
    print("\n=== DAFTAR INVENTARIS GUDANG ===")
    for id_barang, data in inventaris.items():
        print(f"ID Barang : {id_barang}")
        print(f"Nama      : {data[0]}")
        print(f"Harga     : {data[1]}")
        print(f"Stok      : {data[2]}")
        print("-------------------------------")

def cari_barang():
    if cek_kosong():
        return
    
    id_barang = input_id("\nMasukkan ID barang yang dicari: ")

    if id_barang in inventaris:
        data = inventaris[id_barang]
        print("\nBarang ditemukan:")
        print(f"ID Barang : {id_barang}")
        print(f"Nama      : {data[0]}")
        print(f"Harga     : {data[1]}")
        print(f"Stok      : {data[2]}")
    else:
        print("\nBarang tidak ditemukan!")

def tambah_barang():
    id_barang = input_id("\nMasukkan ID barang baru: ")

    if id_barang in inventaris:
        print("\nID barang sudah terdaftar!")
        return

    nama = input("Masukkan nama barang: ")

    while True:
        try:
            harga = float(input("Masukkan harga barang: "))
            if harga < 0:
                print("Harga tidak boleh negatif!")
            else:
                break
        except ValueError:
            print("Input harga harus berupa angka!")

    while True:
        try:
            stok = int(input("Masukkan stok barang: "))
            if stok < 0:
                print("Stok tidak boleh negatif!")
            else:
                break
        except ValueError:
            print("Input stok harus berupa angka!")

    inventaris[id_barang] = [nama, harga, stok]
    print("\nBarang berhasil ditambahkan!")

def update_barang():
    if cek_kosong():
        return

    id_barang = input_id("\nMasukkan ID barang yang akan di-update: ")

    if id_barang not in inventaris:
        print("\nBarang tidak ditemukan!")
        return

    nama_lama, harga_lama, stok_lama = inventaris[id_barang]

    print("\n=== UPDATE DATA BARANG ===")
    print(f"Data lama -> Nama: {nama_lama}, Harga: {harga_lama}, Stok: {stok_lama}")

    nama_baru = input("\nMasukkan nama baru (kosongkan jika tidak diganti): ").strip()
    if nama_baru == "":
        nama_baru = nama_lama

    while True:
        harga_input = input("Masukkan harga baru (kosongkan jika tidak diganti): ").strip()
        if harga_input == "":
            harga_baru = harga_lama
            break
        try:
            harga_baru = float(harga_input)
            if harga_baru < 0:
                print("Harga tidak boleh negatif!")
            else:
                break
        except ValueError:
            print("Input harga harus angka!")

    while True:
        stok_input = input("Masukkan perubahan stok (menambah (+), mengurangi (-), kosongkan jika tidak diganti): ").strip()
        if stok_input == "":
            stok_baru = stok_lama
            break
        try:
            stok_baru = stok_lama + int(stok_input)
            if stok_baru < 0:
                print("Stok tidak boleh negatif!")
            else:
                break
        except ValueError:
            print("Input stok harus berupa angka!")

    inventaris[id_barang] = [nama_baru, harga_baru, stok_baru]
    print("\nData barang berhasil diperbarui!")

def hapus_barang():
    if cek_kosong():
        return

    id_barang = input_id("\nMasukkan ID barang yang akan dihapus: ")

    if id_barang in inventaris:
        del inventaris[id_barang]
        print("\nBarang berhasil dihapus!")
    else:
        print("\nBarang tidak ditemukan!")


while True:
    print("\n=== SISTEM MANAJEMEN INVENTARIS GUDANG ===")
    print("1. Tampilkan semua barang")
    print("2. Cari barang berdasarkan ID")
    print("3. Tambah barang baru")
    print("4. Update data barang (nama, harga, stok)")
    print("5. Hapus barang")
    print("6. Keluar")

    pilihan = input("Pilih menu (1-6): ")

    if pilihan == "1":
        tampilkan_semua()
    elif pilihan == "2":
        cari_barang()
    elif pilihan == "3":
        tambah_barang()
    elif pilihan == "4":
        update_barang()
    elif pilihan == "5":
        hapus_barang()
    elif pilihan == "6":
        print("\nProgram selesai.")
        break
    else:
        print("\nPilihan tidak valid!")

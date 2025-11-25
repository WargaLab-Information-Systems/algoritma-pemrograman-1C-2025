inventaris = {}
counter_id = 1   # Mulai dari A1

def generate_id():
    global counter_id
    id_barang = f"A{counter_id}"
    counter_id += 1
    return id_barang


def tampilkan_semua():
    if not inventaris:
        print("\nTidak ada data barang di gudang.")
    else:
        print("\nDAFTAR BARANG:")
        for id_barang, data in inventaris.items():
            print(f"ID: {id_barang} | Nama: {data[0]} | Harga: Rp{data[1]} | Stok: {data[2]}")


def cari_barang():
    id_barang = input("Masukkan ID barang yang dicari: ").upper()
    if id_barang in inventaris:
        data = inventaris[id_barang]
        print(f"Barang ditemukan → Nama: {data[0]}, Harga: Rp{data[1]}, Stok: {data[2]}")
    else:
        print("Barang dengan ID tersebut tidak ditemukan.")

def tambah_barang():
    id_barang = generate_id()
    print(f"ID Barang otomatis: {id_barang}")

    nama = input("Masukkan nama barang: ")
    harga = int(input("Masukkan harga barang: "))
    stok = int(input("Masukkan stok barang: "))

    inventaris[id_barang] = [nama, harga, stok]
    print("Barang berhasil ditambahkan!")


def update_stok():
    id_barang = input("Masukkan ID barang yang akan diperbarui: ").upper()
    if id_barang in inventaris:
        perubahan = int(input("Masukkan penambahan/pengurangan stok (contoh: 5 atau -3): "))
        if inventaris[id_barang][2] + perubahan < 0:
            print("Perubahan stok ditolak! Stok tidak boleh negatif.")
        else:
            inventaris[id_barang][2] += perubahan
            print("Stok berhasil diperbarui!")
    else:
        print("Barang dengan ID tersebut tidak ditemukan.")


def hapus_barang():
    id_barang = input("Masukkan ID barang yang akan dihapus: ").upper()
    if id_barang in inventaris:
        del inventaris[id_barang]
        print("Barang berhasil dihapus.")
    else:
        print("Barang dengan ID tersebut tidak ditemukan.")


while True:
    print("\n=== PROGRAM INVENTARIS GUDANG ===")
    print("1. Tampilkan semua barang")
    print("2. Cari barang berdasarkan ID")
    print("3. Tambah barang baru")
    print("4. Perbarui stok barang")
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
        update_stok()
    elif pilihan == "5":
        hapus_barang()
    elif pilihan == "6":
        print("Program selesai. Terima kasih!")
        break
    else:
        print("Pilihan tidak valid, silakan coba lagi.")
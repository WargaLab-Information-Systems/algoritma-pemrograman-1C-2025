data_kunjungan = []
id_antrian = 1

def tambah_data():
    global id_antrian
    nama_pengunjung = input("Masukkan nama pengunjung: ")
    nama_santri = input("Masukkan nama santri yang dijenguk: ")
    daerah = input("Masukkan daerah asal (Sumatra/Kalimantan/Jawa): ").capitalize()
    data_kunjungan.append([id_antrian, nama_pengunjung, nama_santri, daerah])
    id_antrian += 1
    print("Data berhasil ditambahkan!\n")

def tampilkan_data():
    print("\n=== DAFTAR KUNJUNGAN SANTRI ===")
    urutan = ["Sumatra", "Kalimantan", "Jawa"]
    for daerah in urutan:
        print(f"\n--- Pengunjung dari {daerah} ---")
        for data in data_kunjungan:
            if data[3] == daerah:
                print(f"ID: {data[0]} | Pengunjung: {data[1]} | Santri: {data[2]}")

def hapus_data():
    id_hapus = int(input("Masukkan ID antrian yang ingin dihapus: "))
    for data in data_kunjungan:
        if data[0] == id_hapus:
            data_kunjungan.remove(data)
            print("Data berhasil dihapus!\n")
            return
    print("ID tidak ditemukan.\n")

# Menu utama
while True:
    print("\n1. Tambah Data")
    print("2. Tampilkan Data")
    print("3. Hapus Data")
    print("4. Keluar")
    pilih = input("Pilih menu: ")

    if pilih == "1":
        tambah_data()
    elif pilih == "2":
        tampilkan_data()
    elif pilih == "3":
        hapus_data()
    elif pilih == "4":
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid.")
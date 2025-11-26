data_kunjungan = []
id_counter = 1

def tambah_kunjungan():
    global id_counter
    print("=== Tambah Data Kunjungan ===")
    nama_pengunjung = input("Masukkan nama pengunjung       : ")
    nama_santri = input("Masukkan nama santri yang dijenguk : ")
    
    while True:
        daerah = input("Masukkan daerah asal (Sumatra/Kalimantan/Jawa): ").capitalize()
        if daerah in ["Sumatra", "Kalimantan", "Jawa"]:
            break
        else:
            print("Daerah tidak valid! Harap masukkan: Sumatra, Kalimantan, atau Jawa.")
    
    data_kunjungan.append([id_counter, nama_pengunjung, nama_santri, daerah])
    print(f"Data berhasil ditambahkan! ID Antrian Anda: {id_counter}")
    id_counter += 1


def tampilkan_kunjungan():
    print("=== Daftar Kunjungan Santri Berdasarkan Daerah ===")
    if not data_kunjungan:
        print("Belum ada data kunjungan.")
        return
    
    urutan_daerah = ["Sumatra", "Kalimantan", "Jawa"]
    for daerah in urutan_daerah:
        print(f"Pengunjung dari {daerah}")
        ada_data = False
        for data in data_kunjungan:
            if data[3] == daerah:
                ada_data = True
                print(f"ID: {data[0]} | Pengunjung: {data[1]} | Santri: {data[2]}")
        if not ada_data:
            print("(Tidak ada pengunjung dari daerah ini.)")


def hapus_kunjungan():
    print("=== Hapus Data Kunjungan ===")
    if not data_kunjungan:
        print("Belum ada data untuk dihapus.")
        return
    
    try:
        id_hapus = int(input("Masukkan ID Antrian yang ingin dihapus: "))
    except ValueError:
        print("ID harus berupa angka!")
        return
    
    for data in data_kunjungan:
        if data[0] == id_hapus:
            data_kunjungan.remove(data)
            print(f"Data dengan ID {id_hapus} berhasil dihapus.")
            return
    print(f"Data dengan ID {id_hapus} tidak ditemukan.")

while True:
    print("\n========== KUNJUNGAN SANTRI ==========")
    print("1. Tambah Data Kunjungan")
    print("2. Tampilkan Semua Kunjungan")
    print("3. Hapus Data Kunjungan")
    print("4. Keluar")
    
    pilihan = input("Pilih menu (1-4): ")
    
    if pilihan == "1":
        tambah_kunjungan()
    elif pilihan == "2":
        tampilkan_kunjungan()
    elif pilihan == "3":
        hapus_kunjungan()
    elif pilihan == "4":
        print("Terima kasih telah berkunjung.")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih menu 1-4.")

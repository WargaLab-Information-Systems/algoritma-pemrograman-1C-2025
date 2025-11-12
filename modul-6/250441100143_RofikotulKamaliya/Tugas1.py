def tambah_kunjungan(data_kunjungan, id_antrian):
    print("\n=== Tambah Data Kunjungan ===")
    nama_pengunjung = input("Masukkan nama pengunjung: ")
    nama_santri = input("Masukkan nama santri yang dijenguk: ")
    while True:
        daerah = input("Masukkan daerah asal (Sumatra/Kalimantan/Jawa): ").capitalize()
        if daerah in ["Sumatra", "Kalimantan", "Jawa"]:
            break
        else:
            print("Daerah tidak valid! Pilih antara Sumatra, Kalimantan, atau Jawa.")
    data_kunjungan.append([id_antrian, nama_pengunjung, nama_santri, daerah])
    print(f"Data berhasil ditambahkan dengan ID antrian {id_antrian}")
    return id_antrian + 1

def tampilkan_kunjungan(data_kunjungan):
    print("\n=== Daftar Kunjungan Berdasarkan Daerah ===")
    if not data_kunjungan:
        print("Belum ada data kunjungan.")
        return
    daerah_urut = ["Sumatra", "Kalimantan", "Jawa"]
    for daerah in daerah_urut:
        print(f"\n--- Pengunjung dari {daerah} ---")
        ada_data = False
        for data in data_kunjungan:
            if data[3] == daerah:
                ada_data = True
                print(f"ID: {data[0]} | Pengunjung: {data[1]} | Santri: {data[2]}")
        if not ada_data:
            print("Tidak ada pengunjung dari daerah ini.")

def hapus_kunjungan(data_kunjungan):
    print("\n=== Hapus Data Kunjungan ===")
    if not data_kunjungan:
        print("Belum ada data untuk dihapus.")
        return
    try:
        id_hapus = int(input("Masukkan ID antrian yang ingin dihapus: "))
        for data in data_kunjungan:
            if data[0] == id_hapus:
                data_kunjungan.remove(data)
                print(f"Data dengan ID {id_hapus} berhasil dihapus.")
                return
        print("ID tidak ditemukan.")
    except ValueError:
        print("Masukkan angka ID yang valid!")

def main():
    data_kunjungan = []
    id_antrian = 1
    while True:
        print("\n=== Sistem Kunjungan Santri ===")
        print("1. Tambah Data Kunjungan")
        print("2. Tampilkan Daftar Kunjungan")
        print("3. Hapus Data Kunjungan")
        print("4. Keluar")
        pilihan = input("Pilih menu (1-4): ")

        if pilihan == "1":
            id_antrian = tambah_kunjungan(data_kunjungan, id_antrian)
        elif pilihan == "2":
            tampilkan_kunjungan(data_kunjungan)
        elif pilihan == "3":
            hapus_kunjungan(data_kunjungan)
        elif pilihan == "4":
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")
main()
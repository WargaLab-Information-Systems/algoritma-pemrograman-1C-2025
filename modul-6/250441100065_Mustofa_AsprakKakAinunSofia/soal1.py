# Program Sistem Kunjungan Santri
data_kunjungan = []
id_antrian = 1

def tambah_kunjungan():
    global id_antrian
    print("\n=== Tambah Data Kunjungan ===")
    nama_pengunjung = input("Masukkan nama pengunjung: ")
    nama_santri = input("Masukkan nama santri yang dijenguk: ")
    daerah = input("Masukkan daerah asal (sumatra/kalimantan/jawa): ").lower()

    if daerah not in ["sumatra", "kalimantan", "jawa"]:
        print("Daerah tidak valid! Gunakan: sumatra / kalimantan / jawa.")
        return

    data_kunjungan.append([id_antrian, nama_pengunjung, nama_santri, daerah])
    print(f"Data berhasil ditambahkan! ID Antrian: {id_antrian}")
    id_antrian += 1


def tampilkan_kunjungan():
    if not data_kunjungan:
        print("\nBelum ada data kunjungan.")
        return

    print("\n=== Daftar Kunjungan Santri Berdasarkan Daerah ===")
    urutan_daerah = ["sumatra", "kalimantan", "jawa"]
    for daerah in urutan_daerah:
        print(f"\n--- Pengunjung dari {daerah} ---")
        ada_data = False
        for data in data_kunjungan:
            if data[3] == daerah:
                print(f"ID: {data[0]} | Pengunjung: {data[1]} | Santri: {data[2]}")
                ada_data = True
        if not ada_data:
            print("Tidak ada pengunjung dari daerah ini.")


def hapus_kunjungan():
    if not data_kunjungan:
        print("Belum ada data untuk dihapus.")
        return

    try:
        id_hapus = int(input("Masukkan ID antrian yang ingin dihapus: "))
    except ValueError:
        print("ID harus berupa angka!")
        return

    for data in data_kunjungan:
        if data[0] == id_hapus:
            data_kunjungan.remove(data)
            print("Data berhasil dihapus.")
            return

    print("ID tidak ditemukan.")


while True:
    print("\n=== SISTEM KUNJUNGAN SANTRI ===")
    print("1. Tambah Data Pengunjung")
    print("2. Tampilkan Data Kunjungan")
    print("3. Hapus Data Pengunjung")
    print("4. Keluar")
    pilih = input("Pilih menu: ")

    if pilih == "1":
        tambah_kunjungan()
    elif pilih == "2":
        tampilkan_kunjungan()
    elif pilih == "3":
        hapus_kunjungan()
    elif pilih == "4":
        print("Terima kasih! Program selesai.")
        break
    else:
        print("Pilihan tidak valid! Silakan coba lagi.")
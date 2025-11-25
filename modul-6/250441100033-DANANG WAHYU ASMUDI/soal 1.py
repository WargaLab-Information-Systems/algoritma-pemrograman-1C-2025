# List utama untuk menyimpan semua data kunjungan
kunjungan = []
no_antrian = 1   # nomor antrian otomatis dimulai dari 1

def tambah_kunjungan():
    global no_antrian

    print("\n=== Tambah Data Kunjungan ===")
    nama_pengunjung = input("Masukkan nama pengunjung        : ")
    nama_santri = input("Masukkan nama santri yang dijenguk : ")

    # Validasi input daerah
    while True:
        daerah = input("Masukkan daerah asal (Sumatra/Kalimantan/Jawa): ").capitalize()
        if daerah in ["Sumatra", "Kalimantan", "Jawa"]:
            break
        else:
            print("Daerah tidak valid! Coba lagi.")

    # Menambahkan data ke list utama
    kunjungan.append([no_antrian, nama_pengunjung, nama_santri, daerah])
    print(f"Data berhasil ditambahkan dengan no_antrian: {no_antrian}")

    no_antrian += 1  # men nomor antrian


def tampilkan_kunjungan():
    print("\n=== Daftar Kunjungan Terurut Berdasarkan Daerah ===")

    urutan_daerah = ["Sumatra", "Kalimantan", "Jawa"]

    for d in urutan_daerah:
        print(f"\n=== Pengunjung dari {d}:")
        ada = False
        for data in kunjungan:
            if data[3] == d:
                print(f"No {data[0]} | {data[1]} menjenguk {data[2]}")
                ada = True
        if not ada:
            print("Tidak ada data.")


def hapus_kunjungan():
    print("\n=== Hapus Data Kunjungan ===")

    id_hapus = int(input("Masukkan no_antrian yang ingin dihapus: "))

    for data in kunjungan:
        if data[0] == id_hapus:
            kunjungan.remove(data)
            print("Data berhasil dihapus!")
            return

    print("Nomor antrian tidak ditemukan!")


# ================== MENU UTAMA ===================

while True:
    print("\n===== SISTEM KUNJUNGAN SANTRI =====")
    print("1. Tambah Data Kunjungan")
    print("2. Tampilkan Semua Data")
    print("3. Hapus Data Pengunjung")
    print("4. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tambah_kunjungan()
    elif pilihan == "2":
        tampilkan_kunjungan()
    elif pilihan == "3":
        hapus_kunjungan()
    elif pilihan == "4":
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid! Coba lagi.")
kunjungan = []

def tambah_kunjungan():
    nama_pengunjung = input("Nama pengunjung: ")
    nama_santri = input("Nama santri yang dijenguk: ")
    daerah_asal = input("Daerah asal (Sumatra/Kalimantan/Jawa): ").capitalize()
    while daerah_asal not in ["Sumatra", "Kalimantan", "Jawa"]:
        daerah_asal = input("Daerah asal (Sumatra/Kalimantan/Jawa): ").capitalize()
    id_antrian = len(kunjungan) + 1  # ID antrian auto-increment berdasarkan panjang list
    kunjungan.append([id_antrian, nama_pengunjung, nama_santri, daerah_asal])
    print(f"Data kunjungan berhasil ditambahkan dengan ID Antrian: {id_antrian}")

def tampilkan_kunjungan():
    if not kunjungan:
        print("Tidak ada data kunjungan.")
        return
    daerah_urutan = ["Sumatra", "Kalimantan", "Jawa"]
    for daerah in daerah_urutan:
        print(f"\nPengunjung dari {daerah}:")
        filtered = [k for k in kunjungan if k[3] == daerah]
        if not filtered:
            print("  Tidak ada pengunjung dari daerah ini.")
        else:
            for k in filtered:
                print(f"  ID Antrian: {k[0]}, Nama Pengunjung: {k[1]}, Nama Santri: {k[2]}")

def hapus_kunjungan():
    id_hapus = int(input("Masukkan ID Antrian yang ingin dihapus: "))
    for i, k in enumerate(kunjungan):
        if k[0] == id_hapus:
            del kunjungan[i]
            print(f"Data kunjungan dengan ID Antrian {id_hapus} berhasil dihapus.")
            return
    print("ID Antrian tidak ditemukan.")

# Menu utama program
while True:
    print("\nMenu Sistem Kunjungan Santri:")
    print("1. Tambah Data Kunjungan")
    print("2. Tampilkan Seluruh Data Kunjungan")
    print("3. Hapus Data Kunjungan berdasarkan ID Antrian")
    print("4. Keluar")
    pilihan = input("Pilih menu (1-4): ")
    if pilihan == "1":
        tambah_kunjungan()
    elif pilihan == "2":
        tampilkan_kunjungan()
    elif pilihan == "3":
        hapus_kunjungan()
    elif pilihan == "4":
        print("Terima kasih telah menggunakan sistem kunjungan santri.")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih 1-4.")
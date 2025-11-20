print("=== SISTEM KUNJUNGAN SANTRI ===")

data_kunjungan = []
id_terakhir = 0

def panjang(data):
    hitung = 0
    for _ in data:
        hitung = hitung + 1
    return hitung

def tambah_data():
    global id_terakhir, data_kunjungan
    print("\n--- TAMBAH DATA PENGUNJUNG ---")
    nama_pengunjung = input("Masukkan nama pengunjung: ")
    nama_santri = input("Masukkan nama santri yang dijenguk: ")

    while True:
        daerah = input("Masukkan daerah asal (Sumatra/Kalimantan/Jawa): ")
        if daerah.lower() in ["sumatra", "kalimantan", "jawa"]:
            break
        print("Daerah tidak valid! Coba lagi.")

    id_terakhir = id_terakhir + 1
    id_antrian = id_terakhir

    baru = []
    for d in data_kunjungan:
        baru = baru + [d]
    baru = baru + [[id_antrian, nama_pengunjung, nama_santri, daerah.capitalize()]]
    data_kunjungan = baru
    print("Data pengunjung berhasil ditambahkan dengan ID:", id_antrian)

def tampilkan_data():
    print("\n--- DAFTAR PENGUNJUNG ---")
    if panjang(data_kunjungan) == 0:
        print("Belum ada data kunjungan.")
        return

    urutan_daerah = ["Sumatra", "Kalimantan", "Jawa"]
    for daerah in urutan_daerah:
        print("\n--Daerah", daerah)
        ada = False
        for data in data_kunjungan:
            if data[3] == daerah:
                ada = True
                print("ID:", data[0])
                print("  Nama Pengunjung:", data[1])
                print("  Nama Santri    :", data[2])
                print("  Asal Daerah    :", data[3])
        if not ada:
            print("(Tidak ada pengunjung dari daerah ini)")

def hapus_data():
    global data_kunjungan
    print("\n--- HAPUS DATA PENGUNJUNG ---")
    if panjang(data_kunjungan) == 0:
        print("Belum ada data untuk dihapus.")
        return

    teks = input("Masukkan ID antrian yang ingin dihapus: ")
    id_hapus = 0
    for t in teks:
        id_hapus = id_hapus * 10 + (ord(t) - ord("0"))

    baru = []
    i = 0
    ditemukan = False
    for data in data_kunjungan:
        if data[0] != id_hapus:
            baru = baru + [data]
        else:
            ditemukan = True
        i = i + 1

    if ditemukan:
        data_kunjungan = baru
        print("Data dengan ID", id_hapus, "berhasil dihapus.")
    else:
        print("ID tidak ditemukan!")

while True:
    print("\nMENU SISTEM KUNJUNGAN SANTRI")
    print("1. Tambah Data")
    print("2. Tampilkan Data")
    print("3. Hapus Data")
    print("4. Keluar")

    pilih = input("Pilih menu (1-4): ")

    if pilih == "1":
        tambah_data()
    elif pilih == "2":
        tampilkan_data()
    elif pilih == "3":
        hapus_data()
    elif pilih == "4":
        print("program selesai.")
        break
    else:
        print("Pilihan tidak valid!")

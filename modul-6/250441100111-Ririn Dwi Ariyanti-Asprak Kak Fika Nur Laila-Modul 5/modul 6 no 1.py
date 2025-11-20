# === SISTEM KUNJUNGAN SANTRI ===
data_kunjungan = []
id_counter = 1

while True:
    print("\n=== SISTEM KUNJUNGAN SANTRI ===")
    print("1. Tambah Pengunjung")
    print("2. Tampilkan Data")
    print("3. Hapus Pengunjung")
    print("4. Keluar")

    pilihan = input("Pilih menu (1-4): ")

    if pilihan == "1":
        nama_pengunjung = input("Masukkan nama pengunjung: ")
        nama_santri = input("Masukkan nama santri yang dijenguk: ")
        daerah = input("Masukkan daerah asal (Sumatra/Kalimantan/Jawa): ").capitalize()

        data_kunjungan.append([id_counter, nama_pengunjung, nama_santri, daerah])
        id_counter += 1
        print(" Data berhasil ditambahkan!")

    elif pilihan == "2":
        if len(data_kunjungan) == 0:
            print("\nBelum ada data pengunjung.")
        else:
            print("\n=== DAFTAR PENGUNJUNG ===")
            urutan = ["Sumatra", "Kalimantan", "Jawa"]
            for d in urutan:
                print(f"\n-- Pengunjung dari {d} --")
                ada = False
                for data in data_kunjungan:
                    if data[3] == d:
                        print("ID:", data[0], "| Nama:", data[1], "| Santri:", data[2])
                        ada = True
                if not ada:
                    print("(Tidak ada pengunjung dari daerah ini)")

    elif pilihan == "3":
        hapus_id = int(input("Masukkan ID yang ingin dihapus: "))
        index_hapus = -1
        for i in range(len(data_kunjungan)):
            if data_kunjungan[i][0] == hapus_id:
                index_hapus = i
                break
        if index_hapus != -1:
            data_kunjungan.pop(index_hapus)
            print("Data berhasil dihapus!")
        else:
            print(" ID tidak ditemukan!")

    elif pilihan == "4":
        print("Program selesai. Terima kasih!")
        break
    else:
        print("Pilihan tidak valid!")

daftar_kunjungan = []
id_antrian = 1

while True:
    print("SISTEM KUNJUNGAN SANTRI")
    print("1. Tambah Data Pengunjung")
    print("2. Tampilkan Daftar Pengunjung")
    print("3. Hapus Data Pengunjung")
    print("4. Keluar")

    pilihan = input("pilih menu (1-4): ")

    if pilihan == "1":
        print("tambah data pengunjung")
        nama_pengunjung = input("masukkan nama pengunjung: ")
        nama_santri = input("masukkan nama santri dijenguk: ")
        daerah_asal = input("masukkan asal daerah (Sumatra/Kalimantan/Jawa): ")

        if daerah_asal == "Sumatra" or daerah_asal == "Kalimantan" or daerah_asal == "Jawa":
            data = [id_antrian, nama_pengunjung, nama_santri, daerah_asal]
            daftar_kunjungan.append(data)
            print("data berhasil ditambahkan dengan ID antrian:", id_antrian)
            id_antrian = id_antrian + 1
        else:
            print("daerah asal tidak valid!")

    elif pilihan == "2":
        print("daftar pengunjung berdasarkan daerah asal")
        if len(daftar_kunjungan) == 0:
            print("belum ada data kunjungan.")
        else:
            urutan_daerah = ["Sumatra", "Kalimantan", "Jawa"]
            for daerah in urutan_daerah:
                print("--- pengunjung dari", daerah, "---")
                ada = False
                for data in daftar_kunjungan:
                    if data[3] == daerah:
                        ada = True
                        print("ID:", data[0], "pengunjung:", data[1], "santri:", data[2])
                if not ada:
                    print("tidak ada pengunjung dari daerah ini.")

    elif pilihan == "3":
        print("hapus data pengunjung")
        if len(daftar_kunjungan) == 0:
            print("belum ada data yang bisa dihapus.")
        else:
            id_hapus = int(input("masukkan ID antrian yang akan dihapus: "))
            ditemukan = False
            for data in daftar_kunjungan:
                if data[0] == id_hapus:
                    daftar_kunjungan.remove(data)
                    print("data dengan ID", id_hapus, "berhasil dihapus.")
                    ditemukan = True
                    break
            if not ditemukan:
                print("ID tidak ditemukan.")

    elif pilihan == "4":
        print("program selesai.")
        break

    else:
        print("pilihan tidak valid.")
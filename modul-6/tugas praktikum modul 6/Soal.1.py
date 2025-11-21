data_kunjungan = []
id_terakhir = 0

while True:
    print("\n=== SISTEM KUNJUNGAN SANTRI ===")
    print("1. tambah data pengunjung")
    print("2. tampilkan daftar pengunjung")
    print("3. hapus data pengunjung berdasarkan ID antrian")
    print("4. keluar")
    pilihan = input("Pilih menu (1-4): ")

    if pilihan == "1":
        
        id_terakhir += 1
        nama_pengunjung = input("nama pengunjung: ")
        nama_santri = input("nama santri yang dijenguk: ")
        daerah_asal = input("daerah asal (sumatra/kalimantan/jawa): ")

        data = [id_terakhir, nama_pengunjung, nama_santri, daerah_asal]
        data_kunjungan.append(data)
        print("data berhasil ditambahkan dengan ID:", id_terakhir)

    elif pilihan == "2":
        
        if len(data_kunjungan) == 0:
            print("Belum ada data pengunjung.")
        else:
            print("\n=== DAFTAR PENGUNJUNG SANTRI ===")

            urutan_daerah = ["sumatra", "kalimantan", "jawa"]
            for daerah in urutan_daerah:
                print(f"\n-- Pengunjung dari {daerah} --")
                for data in data_kunjungan:
                    if data[3] == daerah:
                        print(f"ID: {data[0]} | Pengunjung: {data[1]} | Santri: {data[2]} | Daerah: {data[3]}")

    elif pilihan == "3":
        if len(data_kunjungan) == 0:
            print("Belum ada data untuk dihapus.")
        else:
            id_hapus = int(input("Masukkan ID antrian yang ingin dihapus: "))
            ditemukan = False
            for data in data_kunjungan:
                if data[0] == id_hapus:
                    data_kunjungan.remove(data)
                    print("Data berhasil dihapus.")
                    ditemukan = True
                    break
            if not ditemukan:
                print("ID tidak ditemukan.")

    elif pilihan == "4":
        print("Terima kasih! Program selesai.")
        break

    else:
        print("Pilihan tidak valid. Coba lagi.")
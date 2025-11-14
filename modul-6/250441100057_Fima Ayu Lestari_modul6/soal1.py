data_kunjungan = []
id_antrian = 1

def tambah_data():
    global id_antrian
    print("\nTambah Data Kunjungan")
    nama_pengunjung = input("Nama pengunjung: ")
    nama_santri = input("Nama santri yang dijenguk: ")
    daerah = input("Daerah asal (sumatra/kalimantan/jawa): ").lower()

    if daerah in ["sumatra", "kalimantan", "jawa"]:
        data_kunjungan.append([id_antrian, nama_pengunjung, nama_santri, daerah])
        print(f"Data berhasil ditambahkan dengan ID {id_antrian}")
        id_antrian += 1
    else:
        print("Daerah tidak valid!")

def tampil_data():
    print("\nDaftar Kunjungan Berdasarkan Daerah:")
    if not data_kunjungan:
        print("Belum ada data.")
    else:
        for daerah in ["sumatra", "kalimantan", "jawa"]:
            print(f"\nPengunjung dari {daerah}:")
            ada = False
            for d in data_kunjungan:
                if d[3] == daerah:
                    print(f"ID:{d[0]} | Pengunjung:{d[1]} | Santri:{d[2]}")
                    ada = True
            if not ada:
                print("Tidak ada pengunjung dari daerah ini.")

def hapus_data():
    if not data_kunjungan:
        print("\nBelum ada data yang bisa dihapus.")
    else:
        try:
            id_hapus = int(input("\nMasukkan ID yang ingin dihapus: "))
            for d in data_kunjungan:
                if d[0] == id_hapus:
                    data_kunjungan.remove(d)
                    print(f"Data ID {id_hapus} berhasil dihapus.")
                    return
            print("ID tidak ditemukan.")
        except:
            print("Input harus angka!")

def menu():
    while True:
        print("\n=== SISTEM KUNJUNGAN SANTRI ===")
        print("1. Tambah Kunjungan\n2. Tampilkan Kunjungan\n3. Hapus Kunjungan\n4. Keluar")
        pilih = input("Pilih menu (1-4): ")
        if pilih == "1":
            tambah_data()
        elif pilih == "2":
            tampil_data()
        elif pilih == "3":
            hapus_data()
        elif pilih == "4":
            print("Program selesai, terima kasih.")
            break
        else:
            print("Pilihan tidak valid!")

menu()

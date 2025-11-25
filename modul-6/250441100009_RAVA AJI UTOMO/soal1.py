daftar_kunjungan = []
id_antrian = 1
while True:
    print("\nMenu:")
    print("1. Tambah pengunjung")
    print("2. Lihat daftar pengunjung")
    print("3. Hapus pengunjung")
    print("4. Keluar")
    menu = input("Pilih menu: ")
    #tambah data
    if menu == "1":
        print("\nTambah data pengunjung")
        nama_pengunjung = input("Nama pengunjung: ")
        nama_santri = input("Nama santri yang dijenguk: ")
        daerah = input("Daerah asal (Sumatra/Kalimantan/Jawa): ")
        #biar tampilana rapi
        if daerah.lower() == "sumatra":
            daerah = "Sumatra"
        elif daerah.lower() == "kalimantan":
            daerah = "Kalimantan"
        elif daerah.lower() == "jawa":
            daerah = "Jawa"
        data = [id_antrian, nama_pengunjung, nama_santri, daerah]
        daftar_kunjungan.append(data)
        print("Data pengunjung berhasil ditambah dengan id", id_antrian)
        id_antrian = id_antrian + 1
    #lihat data
    elif menu == "2":
        if len(daftar_kunjungan) == 0:
            print("\nbelum ada pengunjung")
        else:
            print("\nDaftar Pengunjung:")
            print("ID | Nama Pengunjung | Nama Santri | Daerah Asal")
            for daerah_urut in ["Sumatra", "Kalimantan", "Jawa"]:
                for data in daftar_kunjungan:
                    if data[3].lower() == daerah_urut.lower():
                        print(data[0], "|", data[1], "|", data[2], "|", data[3])
    #hapus data
    elif menu == "3":
        print("Hapus data pengunjung")
        hapus = int(input("Masukkan id antrian: "))
        ketemu = False
        for data in daftar_kunjungan:
            if data[0] == hapus:
                daftar_kunjungan.remove(data)
                ketemu = True
                print("Data id", hapus, "berhasil dihapus")
                break
        if ketemu == False:
            print("Data dengan id tersebut tidak ditemukan")
    #keluarnya 
    elif menu == "4":
        print("\nTerima kasih, program selesai.")
        break
    else:
        print("\nPilihan tidak valid, coba lagi.")
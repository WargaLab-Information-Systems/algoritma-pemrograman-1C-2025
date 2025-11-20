#Membuat sistem kunjungan santri
kunjungan = [] #List untuk menyimpan data pengunjung
id_antrian = 1 #ID antrian awal

while True: #Mulai perulangan sampai berenti manual
    #Tampilkan menu u/ user
    print("\n=== SISTEM KUNJUNGAN SANTRI ===")
    print("1. Tambah Pengunjung")
    print("2. Tampilkan Daftar Pengunjung")
    print("3. Hapus Pengunjung")
    print("4. Keluar")

    pilihan = input("Pilih menu (1/2/3/4): ")

    if pilihan == "1": #jika pilih 1 
        print("\n--- Tambah Pengunjung ---")
        nama_pengunjung = input("Nama Pengunjung : ")
        nama_santri = input("Nama Santri     : ")

        print("Daerah Asal:")
        print("1. Sumatra")
        print("2. Kalimantan")
        print("3. Jawa")
        asal = input("Pilih (1/2/3): ")

        if asal == "1":
            daerah = "Sumatra"
        elif asal == "2":
            daerah = "Kalimantan"
        elif asal == "3":
            daerah = "Jawa"
        else:
            print("Pilihan daerah tidak valid!")
            continue

        kunjungan.append([id_antrian, nama_pengunjung, nama_santri, daerah]) #Menambahkan data tadi ke list kunjungan
        print(f"Data berhasil ditambahkan! ID Antrian = {id_antrian}")
        id_antrian += 1 #penambahan

    elif pilihan == "2":
        print("\n--- Daftar Pengunjung Berdasarkan Daerah ---")
        urutan_daerah = ["Sumatra", "Kalimantan", "Jawa"] #Urutan daerah untuk ditampilkan

        for d in urutan_daerah:
            print(f"\nPengunjung dari {d}:")
            ada = False 
            for data in kunjungan:
                if data[3] == d: #mengecek daerah apakah sesuai
                    print(f"ID {data[0]} | {data[1]} menjenguk {data[2]}") 
                    ada = True #menandai ada pengunjung dari daerah tersebut
            if ada == False: #jika tidak ada pengunjung dari daerah tersebut
                print("Tidak ada pengunjung dari daerah ini.")

    elif pilihan == "3":
        print("\n--- Hapus Data Pengunjung ---")
        id_hapus = input("Masukkan ID Antrian: ")

        id_hapus = int(id_hapus)

        ditemukan = False
        for data in kunjungan:
            if data[0] == id_hapus:
                kunjungan.remove(data) #menghapus data dari kunjungan
                print("Data berhasil dihapus!")
                ditemukan = True #menandai data ditemukan
                break

        if ditemukan == False:
            print("ID tidak ditemukan!")

    elif pilihan == "4": #keluar
        print("Program selesai. Terima kasih.")
        break

    else:
        print("Pilihan tidak valid!")
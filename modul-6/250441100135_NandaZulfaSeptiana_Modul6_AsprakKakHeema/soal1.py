daftar_kunjungan = []
id_antrian = 1

def tambah_pengunjung():
    global id_antrian
    print("\n--- Tambah Data Pengunjung ---")
    nama_pengunjung = input("Masukkan Nama Pengunjung: ")
    nama_santri = input("Masukkan Nama Santri yang Dijenguk: ")
    
    while True:
        daerah_asal = input("Masukkan Daerah Asal (Sumatra/Kalimantan/Jawa): ")
        if daerah_asal in ["Sumatra", "Kalimantan", "Jawa"]:
            break
        else:
            print("Daerah asal tidak valid. Harap masukkan Sumatra, Kalimantan, atau Jawa.")
            
    data_pengunjung = [id_antrian, nama_pengunjung, nama_santri, daerah_asal]
    daftar_kunjungan.append(data_pengunjung)
    
    print(f"Data Pengunjung berhasil ditambahkan dengan ID Antrian: {id_antrian}")
    id_antrian += 1

def tampilkan_daftar_pengunjung():
    if not daftar_kunjungan:
        print("\n--- Daftar Kunjungan Kosong ---")
        return

    print("\n--- Daftar Kunjungan Berdasarkan Daerah Asal ---")

    sumatra = [data for data in daftar_kunjungan if data[3] == "Sumatra"]
    kalimantan = [data for data in daftar_kunjungan if data[3] == "Kalimantan"]
    jawa = [data for data in daftar_kunjungan if data[3] == "Jawa"]
    
    daftar_urut = sumatra + kalimantan + jawa

    print("-" * 60)
    print(f"{'ID':<5} | {'Nama Pengunjung':<20} | {'Nama Santri':<15} | {'Daerah Asal':<10}")
    print("-" * 60)
    
    for data in daftar_urut:
        id_antrian, nama_pengunjung, nama_santri, daerah_asal = data
        print(f"{id_antrian:<5} | {nama_pengunjung:<20} | {nama_santri:<15} | {daerah_asal:<10}")
    print("-" * 60)

def hapus_pengunjung():
    tampilkan_daftar_pengunjung() 
    if not daftar_kunjungan:
        return
        
    print("\n--- Hapus Data Pengunjung ---")
    try:
        id_hapus = int(input("Masukkan ID Antrian yang ingin dihapus: "))
    except ValueError:
        print("Input ID harus berupa angka.")
        return

    hapus_id = -1
    for i, data in enumerate(daftar_kunjungan):
        if data[0] == id_hapus:
            hapus_id = i
            break
            
    if hapus_id != -1:
        hapus_data = daftar_kunjungan.pop(hapus_id)
        print(f"Data dengan ID Antrian {id_hapus} ({hapus_data[1]}) berhasil dihapus.")
    else:
        print(f"ID Antrian {id_hapus} tidak ditemukan.")

def menu_kunjungan():
    while True:
        print("\n===== SISTEM KUNJUNGAN SANTRI =====")
        print("1. Tambah Data Pengunjung")
        print("2. Tampilkan Daftar Pengunjung")
        print("3. Hapus Data Pengunjung")
        print("4. Keluar dari Program Kunjungan")
        
        pilihan = input("Masukkan pilihan Anda (1-4): ")
        
        if pilihan == '1':
            tambah_pengunjung()
        elif pilihan == '2':
            tampilkan_daftar_pengunjung()
        elif pilihan == '3':
            hapus_pengunjung()
        elif pilihan == '4':
            print("Keluar dari program kunjungan. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

menu_kunjungan()


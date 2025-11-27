# Program Sistem Kunjungan Santri
data_kunjungan = []
id_counter = 1

def tambah_pengunjung():
    global id_counter
    print("\n=== TAMBAH PENGUNJUNG ===")
    nama_pengunjung = input("nama pengunjung: ")
    nama_santri = input("nama santri yang dijenguk: ")
    
    # input daerah asal
    while True:
        daerah = input("asal daerah (sumatra/kalimantan/jawa): ")
        if daerah in ["sumatra", "kalimantan", "jawa"]:
            break
        else:
            print("daerah harus Sumatra, kalimantan, atau jawa!")
    
    # tambah data ke list utama
    data_kunjungan.append([id_counter, nama_pengunjung, nama_santri, daerah])
    print(f"berhasil ditambah! ID antrian kamu: {id_counter}")
    id_counter += 1

def tampilkan_pengunjung():
    print("\n=== DAFTAR PENGUNJUNG ===")
    
    if not data_kunjungan:
        print("maaf, saat ini belum ada data pengunjung.")
        return
    
    # pisahkan data berdasarkan daerah
    sumatra = []
    kalimantan = []
    jawa = []
    
    for data in data_kunjungan:
        if data[3] == "sumatra":
            sumatra.append(data)
        elif data[3] == "kalimantan":
            kalimantan.append(data)
        elif data[3] == "jawa":
            jawa.append(data)
    
    # Tampilkan data berurutan: Sumatra -> Kalimantan -> Jawa
    for data in sumatra:
        print(f"ID: {data[0]} | pengunjung: {data[1]} | santri: {data[2]} | daerah: {data[3]}")
    
    for data in kalimantan:
        print(f"ID: {data[0]} | pengunjung: {data[1]} | santri: {data[2]} | daerah: {data[3]}")
    
    for data in jawa:
        print(f"ID: {data[0]} | pengunjung: {data[1]} | santri: {data[2]} | daerah: {data[3]}")

def hapus_pengunjung():
    print("\n=== HAPUS PENGUNJUNG ===")
    if not data_kunjungan:
        print("maaf, saat ini belum ada data pengunjung.")
        return
    
    id_hapus = input("masukkan ID antrian yang akan dihapus: ")
    
    # Cek apakah input adalah angka
    if not id_hapus.isdigit():
        print("ID harus berupa angka!")
        return
    
    id_hapus = int(id_hapus)
    
    # Cari data berdasarkan ID
    for i, data in enumerate(data_kunjungan):
        if data[0] == id_hapus:
            data_kunjungan .pop(i)
            print(f"data dengan ID {id_hapus} berhasil dihapus!")
            return
    
    print(f"data dengan ID {id_hapus} tidak ditemukan!") 

while True:
    print("\n=== SISTEM KUNJUNGAN SANTRI ===")
    print("1. tambah pengunjung")
    print("2. tampilkan semua pengunjung") 
    print("3. hapus pengunjung")
    print("4. keluar")
    
    pilihan = input("pilih menu (1-4): ")
    
    if pilihan == "1":
        tambah_pengunjung()
    elif pilihan == "2":
        tampilkan_pengunjung()
    elif pilihan == "3":
        hapus_pengunjung()
    elif pilihan == "4":
        print("terima kasih.")
        break
    else:
        print("pilihan tidak valid! Silakan pilih 1-4.")
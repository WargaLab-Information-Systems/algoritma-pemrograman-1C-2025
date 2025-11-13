kunjungan = []

def tambah_Pengunjung():
    nama_pengunjung = input("masukkan nama pengunjung: ")
    nama_santri = input("masukkan nama santri: ")
    daerah = input("masukkan daerah asal (sumatera/kalimantan/jawa): ")
    if daerah != daerah.strip() :
        print("inputan tidak valid")
        return
    if daerah not in["sumatera", "kalimantan", "jawa"]:
        print("daerah tidak valid")
        return
    id_antrian = len(kunjungan) + 1
    kunjungan.append([nama_pengunjung, nama_santri, daerah, id_antrian])
    print(f"id antrian: {id_antrian}")
    

def tampilkan_pengunjung():
    if not kunjungan:
        print("tidak ada data")
        return
    print("\nsumatera: ")
    for data in kunjungan:
        if data[2] == "sumatera":
            print(f"id: {data[3]}, pengunjung: {data[0]}, santri: {data[1]}")
    print("\nkalimantan: ")
    for data in kunjungan:
        if data[2] == "kalimantan":
            print(f"id: {data[3]}, pengunjung: {data[0]}, santri: {data[1]}")
    print("\njawa: ")
    for data in kunjungan:
        if data [2] == "jawa":
            print(f"id: {data[3]}, pengunjung: {data[0]}, santri {data[1]}")

def hapus_pengunjung():
    try:
        id_hapus = int(input("id antrian: "))
    except ValueError:
        print("id harus angka")
        return
    for i in range(len(kunjungan)):
        if kunjungan[i][3] == id_hapus:
            del kunjungan[i]
            print("dihapus")
            return
    print("id tidak ditemukan")

while True:
    print("\nmenu sistem kunjungan santri: ")
    print("1. tambah pengunjung")
    print("2. tampilkan daftar pengunjung")
    print("3. hapus pengunjung")
    print("4. keluar")

    pilih = input("pilih menu (1-4): ")

    if pilih == "1":
         tambah_Pengunjung()
    elif pilih == "2":
        tampilkan_pengunjung()
    elif pilih == "3":
        hapus_pengunjung()
    elif pilih == "4":
        print("terimakasih.")
        break
    else:
        print("pilihan tidak valid")

            




        
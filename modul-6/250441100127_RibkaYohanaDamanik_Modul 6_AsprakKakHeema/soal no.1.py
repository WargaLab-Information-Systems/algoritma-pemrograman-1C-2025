# Program Sistem Kunjungan Santri

# List utama untuk menyimpan semua data kunjungan
data_kunjungan = []
id_counter = 1  # Untuk memberi ID antrian otomatis

while True:
    print("\n=== SISTEM KUNJUNGAN SANTRI ===")
    print("1. Tambah Pengunjung")
    print("2. Tampilkan Daftar Pengunjung")
    print("3. Hapus Pengunjung berdasarkan ID")
    print("4. Keluar")
    menu = input("Pilih menu (1-4): ")

    if menu == "1":
        # Input data pengunjung
        while True:
            print("\n--- Tambah Data Pengunjung ---")
            nama_pengunjung = input("Nama pengunjung (ketik 'selesai' untuk berhenti): ")
            if nama_pengunjung.lower() == "selesai":
                break

            nama_santri = input("Nama santri yang dijenguk: ")

            daerah = input("Daerah asal (Sumatra/Kalimantan/Jawa): ").capitalize()
            if daerah not in ["Sumatra", "Kalimantan", "Jawa"]:
                print("Daerah tidak valid! Hanya bisa Sumatra, Kalimantan, atau Jawa.")
                continue

            # Simpan data ke list utama
            data_kunjungan.append([id_counter, nama_pengunjung, nama_santri, daerah])
            print(f"Data berhasil ditambahkan dengan ID {id_counter}")
            id_counter += 1

    elif menu == "2":
        print("\n--- DAFTAR PENGUNJUNG (Diurutkan Berdasarkan Daerah) ---")

        if not data_kunjungan:
            print("Belum ada data pengunjung.")
        else:
            # Pisahkan data berdasarkan daerah (tanpa sorted)
            sumatra = []
            kalimantan = []
            jawa = []

            for d in data_kunjungan:
                if d[3] == "Sumatra":
                    sumatra.append(d)
                elif d[3] == "Kalimantan":
                    kalimantan.append(d)
                elif d[3] == "Jawa":
                    jawa.append(d)

            # Gabungkan manual sesuai urutan daerah
            data_urut = sumatra + kalimantan + jawa

            # Tampilkan hasil
            for d in data_urut:
                print(f"ID: {d[0]} | Pengunjung: {d[1]} | Santri: {d[2]} | Daerah: {d[3]}")

    elif menu == "3":
        print("\n--- HAPUS DATA PENGUNJUNG ---")
        if not data_kunjungan:
            print("Belum ada data untuk dihapus.")
        else:
            try:
                hapus_id = int(input("Masukkan ID yang ingin dihapus: "))
                for d in data_kunjungan:
                    if d[0] == hapus_id:
                        data_kunjungan.remove(d)
                        print(f"Data dengan ID {hapus_id} berhasil dihapus.")
                        break
                else:
                    print("ID tidak ditemukan.")
            except ValueError:
                print("Input ID harus berupa angka!")

    elif menu == "4":
        print("\nProgram dihentikan. Terima kasih!")
        break

    else:
        print("Pilihan menu tidak valid!")

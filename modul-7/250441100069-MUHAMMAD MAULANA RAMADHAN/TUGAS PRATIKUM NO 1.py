kontak = {}

def cek_kosong():
    if not kontak:
        print("\nBelum ada data yang dimasukkan!")
        return True
    return False

def tampilkan_kontak():
    if not kontak:
        print("\nTidak ada kontak yang tersimpan.")
    else:
        print("\n=== Daftar Kontak ===")
        for nama, info in kontak.items():
            print(f"Nama : {nama}")
            print(f"Telepon : {info[0]}")
            print(f"Email : {info[1]}")
            print("-------------------")

def cari_kontak():
    if cek_kosong():
        return
    
    nama = input("\nMasukkan nama kontak yang dicari: ").lower()

    if nama in kontak:
        print("\nKontak ditemukan:")
        print(f"Nama : {nama}")
        print(f"Telepon : {kontak[nama][0]}")
        print(f"Email : {kontak[nama][1]}")
    else:
        print("\nKontak tidak ditemukan!")

def validasi_nomor():
    while True:
        nomor = input("Masukkan nomor telepon: ").strip()

        if nomor.isdigit() and 11 <= len(nomor) <= 12:
            return nomor
        else:
            print("Nomor telepon harus angka dan berjumlah 11–12 digit!")

def tambah_kontak():
    nama = input("\nMasukkan nama kontak baru: ").lower()

    if nama in kontak:
        print("\nKontak sudah ada!")
        return

    telepon = validasi_nomor()
    email = input("Masukkan email: ")

    kontak[nama] = [telepon, email]
    print("\nKontak berhasil ditambahkan!")

def update_kontak():
    if cek_kosong():
        return

    nama = input("\nMasukkan nama kontak yang akan di-update: ").lower()

    if nama not in kontak:
        print("\nKontak tidak ditemukan!")
        return

    print("\n=== Update Kontak ===")
    nama_baru = input("Masukkan nama baru (kosongkan jika tidak diganti): ").lower()

    telepon_baru = validasi_nomor()

    email_baru = input("Masukkan email baru: ")

    if nama_baru and nama_baru != nama:
        kontak[nama_baru] = [telepon_baru, email_baru]
        del kontak[nama]
    else:
        kontak[nama] = [telepon_baru, email_baru]

    print("\nData kontak berhasil diperbarui!")

def hapus_kontak():
    if cek_kosong():
        return

    nama = input("\nMasukkan nama kontak yang akan dihapus: ").lower()

    if nama in kontak:
        del kontak[nama]
        print("\nKontak berhasil dihapus!")
    else:
        print("\nKontak tidak ditemukan!")

while True:
    print("\n=== BUKU KONTAK CRUD ===")
    print("1. Tampilkan semua kontak")
    print("2. Cari kontak")
    print("3. Tambah kontak")
    print("4. Update kontak (nama, telepon, email)")
    print("5. Hapus kontak")
    print("6. Keluar")

    pilihan = input("Pilih menu (1-6): ")

    if pilihan == "1":
        tampilkan_kontak()
    elif pilihan == "2":
        cari_kontak()
    elif pilihan == "3":
        tambah_kontak()
    elif pilihan == "4":
        update_kontak()
    elif pilihan == "5":
        hapus_kontak()
    elif pilihan == "6":
        print("\nProgram selesai")
        break
    else:
        print("\nPilihan tidak valid!")

kontak = {}

def tampilkan_kontak():
    if not kontak:
        print("\nDaftar kontak masih kosong!")
        return

    print("\n=== DAFTAR KONTAK ===")
    for nama, info in kontak.items(): #BMENGEMBALIKAN DATA DARI DICTIONARY
        print(f"Nama  : {nama}")
        print(f"Nomor : {info[0]}")
        print(f"Email : {info[1]}")
        print("------------------------")   


def cari_kontak():
    nama = input("Masukkan nama kontak yang dicari: ")

    if nama in kontak:
        print("\nKontak ditemukan:")
        print(f"Nama  : {nama}")
        print(f"Nomor : {kontak[nama][0]}")
        print(f"Email : {kontak[nama][1]}")
    else:
        print("\nKontak tidak ditemukan!")


def tambah_kontak():
    nama = input("Masukkan nama kontak baru: ")

    if nama in kontak:
        print("Kontak sudah ada!")
        return

    nomor = input("Masukkan nomor telepon: ")
    email = input("Masukkan email: ")

    kontak[nama] = [nomor, email]
    print("\nKontak berhasil ditambahkan!")


def update_email():
    nama = input("Masukkan nama kontak yang ingin diperbarui: ")

    if nama not in kontak:
        print("Kontak tidak ditemukan!")
        return

    email_baru = input("Masukkan email baru: ")
    kontak[nama][1] = email_baru
    print("\nEmail berhasil diperbarui!")


def hapus_kontak():
    nama = input("Masukkan nama kontak yang ingin dihapus: ")

    if nama in kontak:
        del kontak[nama]
        print("Kontak berhasil dihapus!")
    else:
        print("Kontak tidak ditemukan!")


# ===== PROGRAM UTAMA =====
while True:
    print("\n===== CONTACT BOOK =====")
    print("1. Tampilkan Semua Kontak")
    print("2. Cari Kontak")
    print("3. Tambah Kontak")
    print("4. Update Email Kontak")
    print("5. Hapus Kontak")
    print("6. Keluar")

    pilihan = input("Pilih menu (1-6): ")

    if pilihan == "1":
        tampilkan_kontak()
    elif pilihan == "2":
        cari_kontak()
    elif pilihan == "3":
        tambah_kontak()
    elif pilihan == "4":
        update_email()
    elif pilihan == "5":
        hapus_kontak()
    elif pilihan == "6":
        print("Program selesai. Terima kasih!")
        break
    else:
        print("Pilihan tidak valid!")
 
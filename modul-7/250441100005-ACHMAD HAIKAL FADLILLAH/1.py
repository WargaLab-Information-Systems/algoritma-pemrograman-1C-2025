contact_book = {}

def tampilkan_semua():
    print("\n=== DAFTAR SEMUA KONTAK ===")
    if not contact_book:
        print("Tidak ada kontak yang tersimpan.")
    else:
        for nama, info in contact_book.items():
            print(f"Nama : {nama}")
            print(f"Telepon : {info[0]}")
            print(f"Email : {info[1]}\n")

def cari_kontak():
    print("\n=== CARI KONTAK ===")
    nama = input("Masukkan nama kontak: ").capitalize()
    
    if nama in contact_book:
        print(f"Nama : {nama}")
        print(f"Telepon : {contact_book[nama][0]}")
        print(f"Email : {contact_book[nama][1]}")
    else:
        print("Kontak tidak ditemukan!")

def tambah_kontak():
    print("\n=== TAMBAH KONTAK BARU ===")
    nama = input("Masukkan nama: ").capitalize()

    if nama in contact_book:
        print("Kontak sudah ada!")
        return

    telepon = input("Masukkan nomor telepon: ")
    email = input("Masukkan email: ")

    contact_book[nama] = [telepon, email]
    print("Kontak berhasil ditambahkan!")

def update_email():
    print("\n=== UPDATE EMAIL KONTAK ===")
    nama = input("Masukkan nama kontak: ").capitalize()

    if nama not in contact_book:
        print("Kontak tidak ditemukan!")
        return

    email_baru = input("Masukkan email baru: ")
    contact_book[nama][1] = email_baru
    print("Email berhasil diperbarui!")

def hapus_kontak():
    print("\n=== HAPUS KONTAK ===")
    nama = input("Masukkan nama kontak yang ingin dihapus: ").capitalize()

    if nama not in contact_book:
        print("Kontak tidak ditemukan!")
        return

    del contact_book[nama]
    print("Kontak berhasil dihapus!")


while True:
    print("\n=== CONTACT BOOK ===")
    print("1. Tampilkan Semua Kontak")
    print("2. Cari Kontak")
    print("3. Tambah Kontak")
    print("4. Update Email Kontak")
    print("5. Hapus Kontak")
    print("6. Keluar")

    pilihan = input("Pilih menu (1-6): ")

    if pilihan == "1":
        tampilkan_semua()
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

contacts = {}

def tampilkan_semua():
    if not contacts:
        print("Belum ada kontak yang tersimpan.")
    else:
        print("Daftar Kontak:")
        for nama in contacts:
            print("Nama:", nama)
            print("Telepon:", contacts[nama][0])
            print("Email:", contacts[nama][1])
    print()

def cari_kontak():
    nama = input("Masukkan nama kontak yang dicari: ").lower()
    if nama in contacts:
        print("Kontak ditemukan:")
        print("Nama:", nama)
        print("Telepon:", contacts[nama][0])
        print("Email:", contacts[nama][1])
    else:
        print("Kontak tidak ditemukan.")
    print()

def tambah_kontak():
    nama = input("Masukkan nama kontak baru: ").lower()
    if not nama.isalpha():
        print("Nama hanya boleh huruf.")
        print()
        return

    if nama in contacts:
        print("Kontak sudah ada.")
        print()
        return

    telepon = input("Masukkan nomor telepon: ")

    if not telepon.isdigit():
        print("Nomor telepon hanya boleh angka.")
        print()
        return

    if len(telepon) < 5 or len(telepon) > 12:
        print("Nomor telepon harus 5 - 12 digit.")
        print()
        return

    email = input("Masukkan email: ")

    if "@" not in email or "." not in email:
        print("Format email tidak valid.")
        print()
        return
    if email.startswith("@") or email.endswith("@") or email.endswith("."):
        print("Format email tidak valid.")
        print()
        return

    contacts[nama] = [telepon, email]
    print("Kontak berhasil ditambahkan.")
    print()

def update_email():
    nama = input("Masukkan nama kontak yang ingin diperbarui emailnya: ").lower()
    if nama in contacts:
        email_baru = input("Masukkan email baru: ")
        if "@" not in email_baru or "." not in email_baru:
            print("Format email tidak valid.")
            print()
            return
        if email_baru.startswith("@") or email_baru.endswith("@") or email_baru.endswith("."):
            print("Format email tidak valid.")
            print()
            return

        contacts[nama][1] = email_baru
        print("Email berhasil diperbarui.")
    else:
        print("Kontak tidak ditemukan.")
    print()

def hapus_kontak():
    nama = input("Masukkan nama kontak yang ingin dihapus: ").lower()
    if nama in contacts:
        del contacts[nama]
        print("Kontak berhasil dihapus.")
    else:
        print("Kontak tidak ditemukan.")
    print()

while True:
    print("MENU CONTACT BOOK")
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
        print("Terima Kasih.")
        break
    else:
        print("Pilihan tidak valid.")
contacts = {}

# === Fungsi Validasi ===

def valid_nama(nama):
    return nama.replace(" ", "").isalpha()

def valid_telepon(telp):
    # Maksimal 13 digit, boleh kurang
    return telp.isdigit() and len(telp) <= 13

def valid_email(email):
    return (
        "@" in email and 
        email.endswith(("gmail.com", "yahoo.com", "outlook.com", "hotmail.com"))
    )

# === Program Utama ===
while True:
    print("\n=== CONTACT BOOK ===")
    print("1. Tampilkan semua kontak")
    print("2. Cari kontak")
    print("3. Tambah kontak")
    print("4. Update email kontak")
    print("5. Hapus kontak")
    print("6. Keluar")

    pilihan = input("Pilih menu: ")

    # 1. Tampilkan semua kontak
    if pilihan == "1":
        if not contacts:
            print("Tidak ada kontak.")
        else:
            for nama, info in contacts.items():
                print(f"Nama: {nama}, Telepon: {info[0]}, Email: {info[1]}")

    # 2. Cari kontak
    elif pilihan == "2":
        nama = input("Masukkan nama kontak: ")
        if nama in contacts:
            print(f"Telepon: {contacts[nama][0]}, Email: {contacts[nama][1]}")
        else:
            print("Kontak tidak ditemukan.")

    # 3. Tambah kontak
    elif pilihan == "3":
        while True:
            nama = input("Nama: ")
            if valid_nama(nama):
                break
            print("Nama hanya boleh huruf!")

        while True:
            telepon = input("Telepon (maksimal 13 digit): ")
            if valid_telepon(telepon):
                break
            print("Telepon harus angka dan TIDAK boleh lebih dari 13 digit!")

        while True:
            email = input("Email: ")
            if valid_email(email):
                break
            print("Email tidak valid!")

        contacts[nama] = [telepon, email]
        print("Kontak berhasil ditambahkan.")

    # 4. Update email
    elif pilihan == "4":
        nama = input("Masukkan nama kontak: ")
        if nama in contacts:
            while True:
                email_baru = input("Email baru: ")
                if valid_email(email_baru):
                    contacts[nama][1] = email_baru
                    print("Email berhasil diperbarui.")
                    break
                print("Email tidak valid!")
        else:
            print("Kontak tidak ditemukan.")

    # 5. Hapus kontak
    elif pilihan == "5":
        nama = input("Nama kontak yang ingin dihapus: ")
        if nama in contacts:
            del contacts[nama]
            print("Kontak berhasil dihapus.")
        else:
            print("Kontak tidak ditemukan.")

    # 6. Keluar
    elif pilihan == "6":
        print("Keluar...")
        break

    else:
        print("Menu tidak valid.")

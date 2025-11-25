data_kontak = {}

# validasi nama (tanpa strip)
def valid_nama(nama):
    # cek kosong atau spasi semua
    if nama == "" or set(nama) == {" "}:
        return False

    # cek per huruf
    for huruf in nama:
        if not (huruf.isalpha() or huruf == " "):
            return False
    return True

# validasi nomor
def valid_nomor(nomor):
    if not nomor.isdigit():
        return False
    return 12 <= len(nomor) <= 13

# validasi email
def valid_email(email):
    if "@" not in email:
        return False

    posisi = -1
    for i in range(len(email)):
        if email[i] == "@":
            posisi = i
            break

    if posisi <= 0 or posisi == len(email) - 1:
        return False

    bagian_user = email[:posisi]
    bagian_domain = email[posisi + 1:]

    if bagian_user == "":
        return False

    domain_valid = ["gmail.com", "yahoo.com", "outlook.com"]
    return bagian_domain in domain_valid

# tambah kontak
def tambah():
    print("\n---Tambah Kontak---")

    # input nama
    while True:
        nama = input("Nama: ")
        if not valid_nama(nama):
            print("Nama hanya boleh huruf dan spasi.")
            continue
        if nama in data_kontak:
            print("Nama sudah ada.")
            continue
        break

    # input nomor
    while True:
        nomor = input("Nomor (12-13 digit): ")
        if not valid_nomor(nomor):
            print("Nomor tidak valid.")
            continue
        break

    # input email
    while True:
        email = input("Email: ")
        if not valid_email(email):
            print("Email tidak valid.")
            continue
        break
    data_kontak[nama] = {"nomor": nomor, "email": email}
    print("Kontak ditambahkan.")

# tampil kontak
def tampil():
    print("\n---Semua Kontak---")
    if not data_kontak:
        print("Belum ada kontak.")
        return
    for nama, info in data_kontak.items():
        print("-", nama, "| Nomor:", info["nomor"], "| Email:", info["email"])

# cari kontak
def cari():
    print("\n=== Cari Kontak ===")
    nama = input("Nama: ")
    if nama in data_kontak:
        info = data_kontak[nama]
        print("Nama :", nama)
        print("Nomor:", info["nomor"])
        print("Email:", info["email"])
    else:
        print("Tidak ditemukan.")

# update email
def update():
    print("\n---Update Email---")
    nama = input("Nama kontak: ")
    if nama not in data_kontak:
        print("Tidak ditemukan.")
        return
    email_baru = input("Email baru: ")
    if not valid_email(email_baru):
        print("Email tidak valid.")
        return
    data_kontak[nama]["email"] = email_baru
    print("Email diperbarui.")

# hapus kontak
def hapus():
    print("\n=== Hapus Kontak ===")
    nama = input("Nama: ")
    if nama in data_kontak:
        del data_kontak[nama]
        print("Kontak dihapus.")
    else:
        print("Tidak ditemukan.")

# menu utama
while True:
    print("\n---CONTACT BOOK---")
    print("1. Tambah Kontak")
    print("2. Tampilkan Semua Kontak")
    print("3. Cari Kontak")
    print("4. Update Email")
    print("5. Hapus Kontak")
    print("0. Keluar")
    pilih = input("Pilih menu: ")

    if pilih == "1":
        tambah()
    elif pilih == "2":
        tampil()
    elif pilih == "3":
        cari()
    elif pilih == "4":
        update()
    elif pilih == "5":
        hapus()
    elif pilih == "0":
        print("Keluar...")
        break
    else:
        print("Pilihan tidak valid.")

kontak = {}

def validasi_telp(telepon):
    return telepon.isdigit() and len(telepon) == 12

def semua_kontak():
    if not kontak:
        print("\nTidak ada kontak.\n")
        return

    print("\n=== Semua Kontak ===")
    for nama, (telepon, email) in kontak.items():
        print(f"Nama    : {nama}")
        print(f"Telepon : {telepon}")
        print(f"Email   : {email}")
        print("--------------------")
    print()

def cari_kontak():
    nama = input("Nama kontak: ")

    if nama in kontak:
        telepon, email = kontak[nama]
        print(f"\nNama    : {nama}")
        print(f"Telepon : {telepon}")
        print(f"Email   : {email}\n")
    else:
        print("\nKontak tidak ditemukan!\n")

def tambah_kontak():
    nama = input("Nama baru: ")

    if nama in kontak:
        print("\nKontak sudah ada!\n")
        return

    while True:
        telepon = input("Telepon (12 digit): ")
        if validasi_telp(telepon):
            break
        print("Nomor telepon harus 12 digit!\n")

    email = input("Email: ")

    kontak[nama] = (telepon, email)
    print("\nKontak berhasil ditambahkan!\n")

def update_email():
    nama = input("Nama kontak: ")

    if nama not in kontak:
        print("\nKontak tidak ditemukan!\n")
        return

    email_baru = input("Email baru: ")
    telepon, _ = kontak[nama]
    kontak[nama] = (telepon, email_baru)

    print("\nEmail berhasil diperbarui!\n")

def hapus_kontak():
    nama = input("Nama kontak: ")

    if nama in kontak:
        del kontak[nama]
        print("\nKontak dihapus!\n")
    else:
        print("\nKontak tidak ditemukan!\n")

def menu():
    while True:
        print("===== PILIH SALAH SATU =====")
        print("1. Lihat semua kontak")
        print("2. Cari kontak")
        print("3. Tambah kontak")
        print("4. Update email")
        print("5. Hapus kontak")
        print("6. Keluar")

        pilih = input("Pilih (1-6): ")

        if pilih == "1": 
            semua_kontak()
        elif pilih == "2": 
            cari_kontak()
        elif pilih == "3": 
            tambah_kontak()
        elif pilih == "4": 
            update_email()
        elif pilih == "5": 
            hapus_kontak()
        elif pilih == "6":
            print("\nTerima kasih!\n")
            break
        else:
            print("\nPilihan tidak valid!\n")

menu()

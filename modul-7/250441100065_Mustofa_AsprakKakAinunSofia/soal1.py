kontak = {}

def tampilkan_kontak():
    if not kontak:
        print("Belum ada data kontak.\n")
        return
    print("\n--- Daftar Kontak ---")
    for nama, info in kontak.items():
        print(f"Nama    : {nama}")
        print(f"Telepon : {info[0]}")
        print(f"Email   : {info[1]}\n")

def cari_kontak():
    nama = input("Masukkan nama kontak yang dicari: ").lower()
    if nama in kontak:
        print("\nData ditemukan:")
        print(f"Nama    : {nama}")
        print(f"Telepon : {kontak[nama][0]}")
        print(f"Email   : {kontak[nama][1]}\n")
    else:
        print("Kontak tidak ditemukan.\n")

def tambah_kontak():
    nama = input("Masukkan nama: ").lower()
    if nama in kontak:
        print("Kontak sudah ada!\n")
        return

    while True:
        telepon = input("Masukkan nomor telepon (11-12 digit): ")

        if not telepon.isdigit():
            print("Nomor telepon harus berupa angka!\n")
        elif len(telepon) < 11 or len(telepon) > 12:
            print("Nomor telepon harus 11 atau 12 digit!\n")
        else:
            break

    email = input("Masukkan email: ")

    kontak[nama] = [telepon, email]
    print("Kontak berhasil ditambahkan.\n")


def update_kontak():
    nama = input("Masukkan nama kontak yang akan diperbarui: ").lower()

    if nama in kontak:
        while True:
            telepon_baru = input("Masukkan telepon baru (Enter jika tidak ingin mengubah): ")

            if telepon_baru == "":
                break

            if not telepon_baru.isdigit():
                print("Nomor telepon harus berupa angka!\n")
            elif len(telepon_baru) < 11 or len(telepon_baru) > 12:
                print("Nomor telepon harus 11 atau 12 digit!\n")
            else:
                kontak[nama][0] = telepon_baru
                break

        email_baru = input("Masukkan email baru (Enter jika tidak ingin mengubah): ")
        if email_baru != "":
            kontak[nama][1] = email_baru

        print("Data kontak berhasil diperbarui.\n")

    else:
        print("Kontak tidak ditemukan.\n")

def hapus_kontak():
    nama = input("Masukkan nama kontak yang akan dihapus: ").lower()
    if nama in kontak:
        del kontak[nama]
        print("Kontak berhasil dihapus.\n")
    else:
        print("Kontak tidak ditemukan.\n")

while True:
    print("""
=== MENU CONTACT BOOK ===
1. Tampilkan Semua Kontak
2. Cari Kontak
3. Tambah Kontak
4. Perbarui Email Kontak
5. Hapus Kontak
6. Keluar
""")

    pilih = input("Pilih menu: ")

    if pilih == "1":
        tampilkan_kontak()
    elif pilih == "2":
        cari_kontak()
    elif pilih == "3":
        tambah_kontak()
    elif pilih == "4":
        update_kontak()
    elif pilih == "5":
        hapus_kontak()
    elif pilih == "6":
        break
    else:
        print("Pilihan tidak valid.\n")

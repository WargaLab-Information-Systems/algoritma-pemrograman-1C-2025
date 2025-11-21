def lihat(kontak):
    if not kontak:
        print("Belum ada data kontak.")
    else:
        for nama, data in kontak.items():
            print(nama, "-", data[0], "-", data[1])


def cari(kontak):
    nama = input("Nama yang dicari: ")
    if nama in kontak:
        print("Telp:", kontak[nama][0], " | Email:", kontak[nama][1])
    else:
        print("Kontak tidak ditemukan.")


def tambah(kontak):
    nama = input("Nama: ")

    telp = input("No telp: ")
    if not telp.isdigit():
        print("Nomor telepon harus angka!")
        return
    if len(telp) != 12:
        print("Nomor telepon harus 12 digit!")
        return

    email = input("Email: ")
    if "@gmail.com" not in email:
        print("Email harus menggunakan @gmail.com")
        return

    kontak[nama] = [telp, email]
    print("Kontak berhasil ditambah.")


def update_email(kontak):
    nama = input("Nama: ")
    if nama in kontak:

        telp_baru = input("Nomor baru (Enter untuk skip): ")
        email_baru = input("Email baru (Enter untuk skip): ")

        if telp_baru:
            if not telp_baru.isdigit():
                print("Nomor baru harus angka!")
                return
            if len(telp_baru) != 12:
                print("Nomor baru harus 12 digit!")
                return
            kontak[nama][0] = telp_baru

        if email_baru:
            if "@gmail.com" not in email_baru:
                print("Email harus menggunakan @gmail.com!")
                return
            kontak[nama][1] = email_baru

        print("Kontak berhasil diperbarui.")
    else:
        print("Nama tidak ditemukan.")


def hapus(kontak):
    nama = input("Nama: ")
    if nama in kontak:
        del kontak[nama]
        print("Kontak dihapus.")
    else:
        print("Nama tidak ada.")


kontak = {}

while True:
    print("\n1. Lihat kontak")
    print("2. Cari kontak")
    print("3. Tambah kontak")
    print("4. Ganti email & nomor")
    print("5. Hapus kontak")
    print("6. Keluar")

    pilih = input("Pilih: ")

    if pilih == "1":
        lihat(kontak)
    elif pilih == "2":
        cari(kontak)
    elif pilih == "3":
        tambah(kontak)
    elif pilih == "4":
        update_email(kontak)
    elif pilih == "5":
        hapus(kontak)
    elif pilih == "6":
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak ada.")

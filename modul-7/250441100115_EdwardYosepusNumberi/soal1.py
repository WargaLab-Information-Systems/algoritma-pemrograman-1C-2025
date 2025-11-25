kontak = {}

def tampil():
    if not kontak:
        print("Tidak ada kontak")
    else:
        for n, (t, e) in kontak.items():
            print(f"{n}: {t}, {e}")

def cari():
    n = input("Nama: ")
    if n in kontak:
        t, e = kontak[n]
        print(f"{n}: {t}, {e}")
    else:
        print("Kontak tidak ditemukan.")

def tambah():
    n = input("Nama: ")
    if n in kontak:
        print("Sudah ada.")
        return
    
    telp = input("Telp: ")

    # Validasi nomor telepon
    if not telp.isdigit() or not (10 <= len(telp) <= 13):
        print("Nomor telepon tidak valid (harus angka 10–13 digit).")
        

    email = input("Email: ")

    # Validasi email sederhana
    if "@" not in email or "." not in email:
        print("Email tidak valid.")
        return

    kontak[n] = [telp, email]
    print("Kontak ditambahkan.")

def update_email():
    n = input("Nama: ")
    if n in kontak:
        email_baru = input("Email baru: ")

        # Validasi email
        if "@" not in email_baru or "." not in email_baru:
            print("Email tidak valid.")
            return

        kontak[n][1] = email_baru
        print("Email diperbarui.")
    else:
        print("Kontak tidak ditemukan.")

def hapus():
    n = input("Nama: ")
    if kontak.pop(n, None):
        print("Kontak dihapus.")
    else:
        print("Kontak tidak ditemukan.")

def main():
    while True:
        print("\n1.Tampil  2.Cari  3.Tambah  4.Update Email  5.Hapus  6.Keluar")
        pilih = input("Pilih: ")

        if pilih == "1":
            tampil()
        elif pilih == "2":
            cari()
        elif pilih == "3":
            tambah()
        elif pilih == "4":
            update_email()
        elif pilih == "5":
            hapus()
        elif pilih == "6":
            print("Keluar.")
            break
        else:
            print("Pilihan salah.")

main()

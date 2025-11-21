buku_kontak = {}

def membuat_kontak(nama, telepon, email):
    if nama in buku_kontak:
        print(f"Kontak dengan nama '{nama}' sudah ada.")
    else:
        buku_kontak[nama] = [telepon, email]
        print(f"Kontak '{nama}' berhasil ditambahkan.")
        
def membaca_kontak():
    if not buku_kontak:
        print("Buku kontak kosong.")
    else:
        print("Daftar Kontak:")
        for nama, details in buku_kontak.items():
            print(f"Nama: {nama}, Telepon: {details[0]}, Email: {details[1]}")

def pencarian_kontak(nama):
    if nama in buku_kontak:
        details = buku_kontak[nama]
        print(f"Ditemukan - Nama: {nama}, Telepon: {details[0]}, Email: {details[1]}")
    else:
        print(f"Kontak dengan nama '{nama}' tidak ditemukan.")

def memperbarui_kontak_email(nama, email_baru):
    if nama in buku_kontak:
        buku_kontak[nama][1] = email_baru
        print(f"Email kontak '{nama}' berhasil diperbarui.")
    else:
        print(f"Kontak dengan nama '{nama}' tidak ditemukan.")

def hapus_kontak(nama):
    if nama in buku_kontak:
        del buku_kontak[nama]
        print(f"Kontak '{nama}' berhasil dihapus.")
    else:
        print(f"Kontak dengan nama '{nama}' tidak ditemukan.")

def menu():
    while True:
        print("\n=== Menu Buku Kontak ===")
        print("1. Tampilkan semua kontak")
        print("2. Cari kontak berdasarkan nama")
        print("3. Tambah kontak baru")
        print("4. Perbarui email kontak")
        print("5. Hapus kontak")
        print("6. Keluar")
        pilihan = input("Masukkan pilihan Anda: ")

        if pilihan == '1':
            membaca_kontak()
        elif pilihan == '2':
            nama = input("Masukkan nama kontak yang dicari: ")
            pencarian_kontak(nama)
        elif pilihan == '3':
            nama = input("Masukkan nama: ")
            while True:
                telepon_str = input("masukkan nomor telepon (harus 12 digit): ")
                if len(telepon_str) == 12 and telepon_str.isdigit():
                    telepon = int(telepon_str)
                    break
                else:
                    print("input tidak valid pastikan nomor telepon terdiri dari 12 digit dan hanya angka.")
            email = input("Masukkan email: ")
            membuat_kontak(nama, telepon, email)
        elif pilihan == '4':
            nama = input("Masukkan nama kontak yang emailnya akan diperbarui: ")
            email_baru = input("Masukkan email baru: ")
            memperbarui_kontak_email(nama, email_baru)
        elif pilihan == '5':
            nama = input("Masukkan nama kontak yang akan dihapus: ")
            hapus_kontak(nama)
        elif pilihan == '6':
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

menu()
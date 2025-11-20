def tampilkan_kontak(contacts):
    if not contacts:
        print("\nTidak ada kontak yang tersimpan.\n")
    else:
        print("\n=== Daftar Kontak ===")
        for nama, data in contacts.items():
            print(f"Nama : {nama}")
            print(f"Telepon : {data[0]}")
            print(f"Email : {data[1]}\n")

def cari_kontak(contacts):
    nama = input("Masukkan nama kontak yang dicari: ")
    if nama in contacts:
        print("\nKontak ditemukan:")
        print(f"Nama   : {nama}")
        print(f"Telepon: {contacts[nama][0]}")
        print(f"Email  : {contacts[nama][1]}\n")
    else:
        print("\nKontak tidak ditemukan.\n")

def tambah_kontak(contacts):
    nama = input("Masukkan nama kontak baru: ")

    if nama in contacts:
        print("Kontak sudah ada. Gunakan menu update untuk mengubah data.\n")
        return

    telepon = input("Masukkan nomor telepon: ")
    email = input("Masukkan email: ")

    contacts[nama] = [telepon, email]
    print("Kontak berhasil ditambahkan!\n")

def update_email(contacts):
    nama = input("Masukkan nama kontak yang emailnya ingin diperbarui: ")

    if nama not in contacts:
        print("Kontak tidak ditemukan.\n")
        return

    telepon_baru = input("Masukkan nomor telepon baru (tekan Enter jika tidak ingin diubah): ")
    if telepon_baru != "":
        contacts[nama][0] = telepon_baru
        print ("Nomor berhasil di perbarui")
    else:
        contacts[nama][0]

    email_baru = input("Masukkan email baru: ")
    if email_baru != "":
        contacts[nama][1] = email_baru
        print("Email berhasil diperbarui!\n")
    else:
        contacts[nama][1]
        
def hapus_kontak(contacts):
    nama = input("Masukkan nama kontak yang ingin dihapus: ")

    if nama not in contacts:
        print("Kontak tidak ditemukan.\n")
        return

    del contacts[nama]
    print("Kontak berhasil dihapus!\n")

def main():

    contacts = {}

    while True:
        print("=== MENU CONTACT BOOK ===")
        print("1. Tampilkan Semua Kontak")
        print("2. Cari Kontak")
        print("3. Tambah Kontak Baru")
        print("4. Update Email Kontak")
        print("5. Hapus Kontak")
        print("6. Keluar")

        pilihan = input("Pilih menu (1-6): ")

        if pilihan == '1':
            tampilkan_kontak(contacts)
        elif pilihan == '2':
            cari_kontak(contacts)
        elif pilihan == '3':
            tambah_kontak(contacts)
        elif pilihan == '4':
            update_email(contacts)
        elif pilihan == '5':
            hapus_kontak(contacts)
        elif pilihan == '6':
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Coba lagi.\n")


main()

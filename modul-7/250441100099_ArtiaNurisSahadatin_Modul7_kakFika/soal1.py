#program contact book dengan fitur CRUD (Create, Read, Update,delate)

#read
#Ini fungsi buat nampilin semua kontak yang ada
def tampilkan_semua_kontak(kontak):
    if not kontak:
        print("Daftar kontak kosong.")
    else:
        print("Daftar Kontak:")
        for nama, info in kontak.items():#buat ngambil data dari dictionary
            print(f"Nama: {nama}, Telepon: {info[0]}, Email: {info[1]}")

#fungsi buat cari kontak berdasarkan nama
def cari_kontak(kontak):
    nama = input("Masukkan nama kontak yang dicari: ")
    if nama in kontak:
        telepon, email = kontak[nama] #kontak[nama] artinya kamu mau ngambil list 
        print(f"Kontak ditemukan - Nama: {nama}, Telepon: {telepon}, Email: {email}")
    else:
        print("Kontak tidak ditemukan.")
#create
#fungsi untuk nambah kontak
def tambah_kontak(kontak):
    nama = input("Masukkan nama kontak baru: ")
    if nama in kontak:
        print("Kontak sudah ada.")
    else:
        telepon = input("Masukkan nomor telepon: ")
        email = input("Masukkan email: ")
        kontak[nama] = [telepon, email]
        print("Kontak berhasil ditambahkan.")
#update
#memperbarui email kontak tertentu
def perbarui_email(kontak):
    nama = input("Masukkan nama kontak yang ingin diperbarui emailnya: ")
    if nama in kontak:
        email_baru = input("Masukkan email baru: ")
        kontak[nama][1] = email_baru
        print("Email berhasil diperbarui.")
    else:
        print("Kontak tidak ditemukan.")
#delate
#fungsi buat hapus kontak
def hapus_kontak(kontak):
    nama = input("Masukkan nama kontak yang ingin dihapus: ")
    if nama in kontak:
        del kontak[nama]
        print("Kontak berhasil dihapus.")
    else:
        print("Kontak tidak ditemukan.")

def menu():
    kontak = {}
    while True:
        print("\nMenu Contact Book")
        print("1. Tampilkan semua kontak")
        print("2. Cari kontak berdasarkan nama")
        print("3. Tambah kontak baru")
        print("4. Perbarui email kontak")
        print("5. Hapus kontak")
        print("6. Keluar")

        pilihan = input("Pilih menu (1-6): ")
        
#menu yang ngecek apa pilihan yang dimasukkan pengguna
        if pilihan == '1':
            tampilkan_semua_kontak(kontak)
        elif pilihan == '2':
            cari_kontak(kontak)
        elif pilihan == '3':
            tambah_kontak(kontak)
        elif pilihan == '4':
            perbarui_email(kontak)
        elif pilihan == '5':
            hapus_kontak(kontak)
        elif pilihan == '6':
            print("Terima kasih telah menggunakan Contact Book.")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

if __name__ == "__main__":
    menu()

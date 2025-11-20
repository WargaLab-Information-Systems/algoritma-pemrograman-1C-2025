contacts = {}  # Dictionary untuk menyimpan kontak

def menu_tampilan(): #menampilkan menu display
    print("\n=== MENU CONTACT BOOK ===")
    print("1. Tampilkan semua kontak")
    print("2. Cari kontak berdasarkan nama")
    print("3. Tambah kontak baru")
    print("4. Update email kontak")
    print("5. Hapus kontak")
    print("6. Keluar")


def display_all_contacts(): #menampilkan semua kontak
    if not contacts: #jika bukan kontak
        print("Tidak ada kontak yang tersimpan.")
    else:
        print("\n=== DAFTAR KONTAK ===")
        for name, details in contacts.items(): #mengambil nama dan detail dari kontak
            print(f"Nama: {name}, Nomor Telepon: {details[0]}, Email: {details[1]}")


def search_contact(): #mencari kontak berdasarkan nama
    name = input("Masukkan nama kontak yang dicari: ").strip() #mengambil input nama dan menghapus spasi kiri kanan 
    if name in contacts: #cek apakah kontak ada
        details = contacts[name] #mengambil detail kontak berdasarkan nama
        print(f"Nama: {name}, Nomor Telepon: {details[0]}, Email: {details[1]}")
    else:
        print("Kontak dengan nama tersebut tidak ditemukan.")


def add_contact():  # menambah kontak baru
    while True:  # loop untuk validasi nama
        name = input("Masukkan nama kontak: ").strip()  # mengambil input nama dan menghapus spasi kiri kanan
        if name.isalnum():  # cek apakah nama hanya terdiri dari huruf dan angka
            break  # keluar dari loop jika valid
        else:
            print("Nama kontak hanya boleh berisi huruf dan angka. Silakan coba lagi.")  # pesan error jika invalid
    
    if name in contacts:  # cek apakah nama sudah ada di kontak
        print("Kontak dengan nama tersebut sudah ada.")
    else:
        while True:  # loop untuk validasi nomor telepon
            phone = input("Masukkan nomor telepon: ").strip()  # mengambil input nomor telepon dan menghapus spasi kiri kanan
            if phone.isdigit() and len(phone) == 11:  # cek apakah input berupa angka dan tepat 11 digit
                break  # keluar dari loop jika valid
            else:
                print("Nomor telepon harus berupa angka dan tepat 11 digit. Silakan coba lagi.")  # pesan error jika invalid
        
        while True:  # loop untuk validasi email
            email = input("Masukkan email: ").strip()  # mengambil input email dan menghapus spasi kiri kanan
            if email.endswith('@gmail.com'):  # cek apakah email berakhir dengan '@gmail.com'
                break  # keluar dari loop jika valid
            else:
                print("Email harus berakhir dengan '@gmail.com'. Silakan coba lagi.")  # pesan error jika invalid
        
        contacts[name] = [phone, email]  # menyimpan kontak baru ke dictionary
        print("Kontak berhasil ditambahkan.")



def update_email(): #mengupdate email kontak
    name = input("Masukkan nama kontak yang ingin diupdate email-nya: ").strip()
    if name in contacts: #cek apakah kontak ada
        new_email = input("Masukkan email baru: ").strip()
        contacts[name][1] = new_email #mengupdate email di index ke-1
        print("Email kontak berhasil diupdate.")
    else:
        print("Kontak dengan nama tersebut tidak ditemukan.")


def delete_contact(): #menghapus kontak
    name = input("Masukkan nama kontak yang ingin dihapus: ").strip()
    if name in contacts: #cek apakah kontak ada
        del contacts[name] #menghapus kontak dari dictionary
        print("Kontak berhasil dihapus.")
    else:
        print("Kontak dengan nama tersebut tidak ditemukan.")


# Loop utama program
while True:
    menu_tampilan()
    choice = input("Pilih opsi (1-6): ").strip()
    
    if choice == "1":
        display_all_contacts()
    elif choice == "2":
        search_contact()
    elif choice == "3":
        add_contact()
    elif choice == "4":
        update_email()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        print("Terima kasih telah menggunakan Contact Book!")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
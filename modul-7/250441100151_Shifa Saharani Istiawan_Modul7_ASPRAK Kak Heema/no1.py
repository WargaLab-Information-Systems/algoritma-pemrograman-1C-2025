import json #nyimpandata
import os #ngecek apa ada kontak atau tidak
import re #memvalidasi no tlp dan email

CONTACTS_FILE = "contacts.json"

# Fungsi untuk memuat kontak dari file
def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'r') as f:
            return json.load(f)
    return {}

# Fungsi untuk menyimpan kontak ke file
def save_contacts():
    with open(CONTACTS_FILE, 'w') as f:
        json.dump(contacts, f, indent=4)

# Dictionary untuk menyimpan kontak (data lama akan otomatis)
contacts = load_contacts()

def tampilkan_kontak():
    if not contacts:
        print("Tidak ada kontak yang tersimpan.")
    else:
        print("\nDaftar Kontak:")
        for nama, info in contacts.items():
            print(f"- {nama} | Telp: {info['telp']} | Email: {info['email']}")
    print()

def cari_kontak():
    nama = input("Masukkan nama kontak yang ingin dicari: ").strip().lower()
    for key in contacts:
        if key.lower() == nama:
            print(f"Ditemukan: {key} | Telp: {contacts[key]['telp']} | Email: {contacts[key]['email']}")
            print()
            return
    print("Kontak tidak ditemukan.\n")

def tambah_kontak():
    nama = input("Masukkan nama: ").strip()
    if not nama:
        print("Nama tidak boleh kosong!")
        return

    if nama.lower() in [k.lower() for k in contacts]:
        print("Kontak sudah ada!")
        return

    telp = input("Masukkan nomor telepon: ").strip()

    # Validasi nomor telepon
    if not re.match(r'^\d+$', telp):
        print("Nomor telepon harus berupa angka!")
        return
    if len(telp) < 11:
        print("Nomor telepon harus minimal 11 digit!")
        return

    email = input("Masukkan email: ").strip()

    # Validasi email wajib @gmail.com
    if not re.match(r'^[^@]+@gmail\.com$', email):
        print("Email harus menggunakan domain @gmail.com!")
        return

    contacts[nama] = {'telp': telp, 'email': email}
    save_contacts()
    print("Kontak berhasil ditambahkan!\n")

def update_email():
    nama = input("Masukkan nama kontak yang ingin diperbarui emailnya: ").strip().lower()
    for key in contacts:
        if key.lower() == nama:
            email_baru = input("Masukkan email baru: ").strip()

            # Validasi email baru
            if not re.match(r'^[^@]+@gmail\.com$', email_baru):
                print("Email harus menggunakan domain @gmail.com!")
                return

            contacts[key]['email'] = email_baru
            save_contacts()
            print("Email berhasil diperbarui!\n")
            return

    print("Kontak tidak ditemukan.\n")

def hapus_kontak():
    nama = input("Masukkan nama kontak yang ingin dihapus: ").strip().lower()
    for key in list(contacts.keys()):
        if key.lower() == nama:
            del contacts[key]
            save_contacts()
            print("Kontak berhasil dihapus!\n")
            return
    print("Kontak tidak ditemukan.\n")

# Menu utama
while True:
    print("=== CONTACT BOOK ===")
    print("1. Tampilkan semua kontak")
    print("2. Cari kontak")
    print("3. Tambah kontak")
    print("4. Update email kontak")
    print("5. Hapus kontak")
    print("6. Keluar")

    pilihan = input("Pilih menu (1-6): ").strip()

    if pilihan == "1":
        tampilkan_kontak()
    elif pilihan == "2":
        cari_kontak()
    elif pilihan == "3":
        tambah_kontak()
    elif pilihan == "4":
        update_email()
    elif pilihan == "5":
        hapus_kontak()
    elif pilihan == "6":
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid!\n")
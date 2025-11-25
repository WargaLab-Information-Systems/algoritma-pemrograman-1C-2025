# PROGRAM BUKU KONTAK DENGAN CRUD

buku_kontak = {}   # dictionary untuk menyimpan data kontak (key = nama, value = [telepon, email])

# Fungsi untuk menampilkan semua kontak yang ada di dalam buku kontak
def tampilkan_semua():
    if not buku_kontak:
        print("\n== Tidak ada kontak tersimpan ==")
    else:
        print("\n== Daftar Semua Kontak ==")
        for nama, info in buku_kontak.items():
            print(f"Nama : {nama}")
            print(f"Telepon : {info[0]}")
            print(f"Email   : {info[1]}\n")

# Fungsi untuk mencari kontak berdasarkan nama
def cari_kontak():
    nama = input("Masukkan nama kontak yang ingin dicari : ")
    if nama in buku_kontak:
        print("\n== Kontak Ditemukan ==")
        print(f"Nama : {nama}")
        print(f"Telepon : {buku_kontak[nama][0]}")
        print(f"Email   : {buku_kontak[nama][1]}")
    else:
        print("\n!! Kontak tidak ditemukan !!")

# Fungsi untuk menambahkan kontak baru ke dalam buku kontak
def tambah_kontak():
    # Meminta input nama kontak baru
    nama = input("Masukkan nama kontak baru : ")

    # Mengecek apakah nama sudah ada di dalam buku_kontak
    if nama in buku_kontak:
        print("\n!! Kontak sudah ada. Gunakan menu update untuk mengubah kontak !!")
    else:
        # Validasi nomor telepon minimal 10 digit dan maksimal 12 digit
        while True:
            telepon = input("Masukkan nomor telepon (10-12 digit) : ")

            # cek hanya angka dan panjang harus 10–12 digit
            if telepon.isdigit() and 10 <= len(telepon) <= 12:
                break
            else:
                print(">> Nomor telepon harus 10–12 digit dan hanya berisi angka! Silakan input lagi.")

        # Input username email saja (tanpa @gmail.com)
        username = input("Masukkan username email (tanpa @gmail.com) : ")

        # Menggabungkan username dengan domain @gmail.com
        email = username + "@gmail.com"

        # Menyimpan kontak baru dalam list [telepon, email]
        buku_kontak[nama] = [telepon, email]
        print("\n== Kontak berhasil ditambahkan ==")


def update_email():
    # Meminta nama kontak yang ingin diperbarui emailnya
    nama = input("Masukkan nama kontak yang ingin diperbarui emailnya : ")

    # Mengecek apakah kontak ditemukan
    if nama in buku_kontak:

        # Input username email baru (tanpa @gmail.com)
        username_baru = input("Masukkan username email baru (tanpa @gmail.com) : ")

        # Menggabungkan username baru dengan domain @gmail.com
        email_baru = username_baru + "@gmail.com"

        # Menyimpan email baru pada indeks ke-1 karena posisi ke-2 dalam list adalah email
        buku_kontak[nama][1] = email_baru

        print("\n== Email berhasil diperbarui ==")
    else:
        # Jika nama kontak tidak ada di buku_kontak
        print("\n!! Kontak tidak ditemukan !!")



# Fungsi untuk menghapus kontak dari buku kontak
def hapus_kontak():
    nama = input("Masukkan nama kontak yang ingin dihapus : ")
    if nama in buku_kontak:
        del buku_kontak[nama]   # hapus data berdasarkan key nama
        print("\n== Kontak berhasil dihapus ==")
    else:
        print("\n!! Kontak tidak ditemukan !!")



# ===== MENU UTAMA =====
while True:
    print("\n===== BUKU KONTAK =====")
    print("1. Tampilkan Semua Kontak")
    print("2. Cari Kontak")
    print("3. Tambah Kontak")
    print("4. Update Email Kontak")
    print("5. Hapus Kontak")
    print("6. Keluar")

    pilihan = input("Pilih menu (1-6): ")

    if pilihan == '1':
        tampilkan_semua()
    elif pilihan == '2':
        cari_kontak()
    elif pilihan == '3':
        tambah_kontak()
    elif pilihan == '4':
        update_email()
    elif pilihan == '5':
        hapus_kontak()
    elif pilihan == '6':
        print("Terima kasih telah menggunakan Buku Kontak.")
        break
    else:
        print("\n!! Pilihan tidak valid, coba lagi !!")
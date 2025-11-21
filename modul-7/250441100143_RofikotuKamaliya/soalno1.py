contact = {}
while True:
    print("\n=== CONTACT BOOK ===")
    print("1. Tambah Kontak")
    print("2. Perbarui Email Kontak")
    print("3. Cari Kontak")
    print("4. Tampilkan Semua Kontak")
    print("5. Hapus Kontak")
    print("6. Keluar")
    pilihan = input("Pilih menu: ")
    if pilihan == "1":
        while True:
            print("\n=== TAMBAH KONTAK ===")
            nama = input("Masukkan nama: ")
            if nama in contact:
                print("Nama sudah ada! Gunakan nama lain.")
                continue
            while True:
                nomor = input("Masukkan nomor telepon: ")
                if not nomor.isdigit():
                    print("Nomor telepon harus berupa angka.")
                elif len(nomor) > 13:
                    print("Nomor telepon harus kurang dari 13 digit!!")
                else:
                    break
            while True:
                email = input("Masukkan email: ")
                if "@" not in email or "." not in email:
                    print("Format email tidak valid.")
                else:
                    break
            contact[nama] = [nomor, email]
            print("Kontak berhasil ditambahkan!")
            lanjut = input("Tambah kontak lagi? (y/n): ")
            if lanjut != "y":
                break
    elif pilihan == "2":
        update = input("Masukkan nama: ")
        if update not in contact:
            print("Kontak tidak ditemukan.")
        else:
            print(f"Email saat ini: {contact[update][1]}")
            while True:
                email_baru = input("Masukkan email baru: ")
                if "@" not in email_baru or "." not in email_baru:
                    print("Format email tidak valid.")
                else:
                    break
            contact[update][1] = email_baru
            print("Email berhasil diperbarui!")
    elif pilihan == "3":
        nama_cari = input("Masukkan nama: ")
        if nama_cari in contact:
            nomor, email = contact[nama_cari]
            print("\nKontak ditemukan!")
            print(f"Nama : {nama_cari}")
            print(f"Telepon: {nomor}")
            print(f"Email: {email}")
        else:
            print("Kontak tidak ditemukan.")
    elif pilihan == "4":
        if not contact:
            print("Kontak masih kosong.")
        else:
            print("\n=== DAFTAR KONTAK ===")
            for nama, data in contact.items():
                print(f"Nama   : {nama}")
                print(f"Telepon: {data[0]}")
                print(f"Email  : {data[1]}")
                print("-----------------------")
    elif pilihan == "5":
        nama_hapus = input("Masukkan nama: ")
        if nama_hapus in contact:
            del contact[nama_hapus]
            print("Kontak berhasil dihapus.")
        else:
            print("Kontak tidak ditemukan.")
    elif pilihan == "6":
        print("Program selesai. Terimakasih!")
        break
    else:
        print("Pilihan tidak valid.")
# ##Tugas Praktikum
# ##Soal 1
# print("Soal 1")
# print("SOAL: ")
# print("====================")

Kontak = {}

def NamaValid(n):
    return n.replace(" ", "").isalpha()

def NomerValid(no):
    return no.isdigit() and len(no) >= 10 <= len(no) <= 12

def EmailValid(e):
    return "@" in e and "." in e and e.count("@") == 1

while True:
    print("=== CONTACT BOOK ===")
    print("1. Tampilkan Semua Kontak")
    print("2. Cari Kontak")
    print("3. Tambah Kontak")
    print("4. Perbarui Email Kontak")
    print("5. Hapus Kontak")
    print("6. Keluar")

    pilih = input("Pilih menu (1–6): ")
    if pilih not in ["1","2","3","4","5","6"]:
        print("Pilihan tidak valid!\n")
        continue

##read
    if pilih == "1":
        print("\n--- Semua Kontak ---")
        if not Kontak:
            print("Belum ada kontak.\n")
        else:
            for nama in Kontak:
                print(f"Nama: {nama} | Nomor: {Kontak[nama][0]} | Email: {Kontak[nama][1]}")
            print()

##search
    elif pilih == "2":
        nama = input("Masukkan nama yang dicari: ").lower()
        ditemukan = False

        for key in Kontak:
            if key.lower() == nama:
                print(f"Nama: {key} | Nomor: {Kontak[key][0]} | Email: {Kontak[key][1]}\n")
                ditemukan = True
                break
        if not ditemukan:
            print("Kontak tidak ditemukan.\n")

##create
    elif pilih == "3":
        while True:
            nama = input("Masukkan nama kontak: ").strip()
            if NamaValid(nama):
                break
            print("Nama tidak valid!")

        while True:
            nomor = input("Masukkan nomor telepon: ")
            if NomerValid(nomor):
                break
            print("Nomor telepon tidak valid!")

        while True:
            email = input("Masukkan email: ")
            if EmailValid(email):
                break
            print("Email tidak valid!")

        Kontak[nama] = [nomor, email]
        print("Kontak berhasil ditambahkan!\n")

##update
    elif pilih == "4":
        nama = input("Masukkan nama kontak: ").strip()

        if nama not in Kontak:
            print("Kontak tidak ditemukan.\n")
        else:
            while True:
                email = input("Masukkan email baru: ")
                if EmailValid(email):
                    break
                print("Email tidak valid!")

            Kontak[nama][1] = email
            print("Email berhasil diperbarui!\n")

##delate
    elif pilih == "5":
        nama = input("Masukkan nama kontak: ")
        if nama in Kontak:
            del Kontak[nama]
            print("Kontak berhasil dihapus!\n")
        else:
            print("Kontak tidak ditemukan.\n")

    else:
        print("Program selesai.")
        break
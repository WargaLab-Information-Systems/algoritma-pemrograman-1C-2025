biodata = {
    "nama": "",
    "umur": 0,
    "hobi": "",
    "alamat": ""
}
print("=== INPUT BIODATA ===")
while True:
    nama = input("Masukkan nama: ")
    if nama == "":
        print("Nama tidak boleh kosong!")
    else:
        biodata["nama"] = nama
        break
while True:
    umur = input("Masukkan umur: ")
    if umur == "":
        print("Umur tidak boleh kosong!")
    elif not umur.isdigit():
        print("Umur tidak valid! harus berupa angka dan lebih dari 0.")
    else:
        biodata["umur"] = int(umur)
        break
while True:
    hobi = input("Masukkan hobi: ")
    if hobi == "":
        print("Hobi tidak boleh kosong!")
    else:
        biodata["hobi"] = hobi
        break
while True:
    alamat = input("Masukkan alamat: ")
    if alamat == "":
        print("Alamat tidak boleh kosong!")
    else:
        biodata["alamat"] = alamat
        break
while True:
    print("\n=== MENU BIODATA ===")
    print("1. Perbarui Biodata")
    print("2. Tampilkan Biodata")
    print("3. Keluar")
    pilihan = input("Pilih menu: ")
    if pilihan == "1":
        print("\n--- PERBARUI BIODATA ---")
        print("a. Nama")
        print("b. Umur")
        print("c. Hobi")
        print("d. Alamat")
        print("e. Kembali")
        pilih_update = input("Pilih data yang ingin diperbarui: ")
        if pilih_update == "a":
            while True:
                nama_baru = input("Masukkan nama baru: ")
                if nama_baru == "":
                    print("Nama tidak boleh kosong!")
                else:
                    biodata["nama"] = nama_baru
                    print("Nama berhasil diperbarui!")
                    break
        elif pilih_update == "b":
            while True:
                umur_baru = input("Masukkan umur baru: ")
                if umur_baru == "":
                    print("Umur tidak boleh kosong!")
                elif not umur_baru.isdigit():
                    print("Umur tidak valid! harus berupa angka dan lebih dari 0.")
                else:
                    biodata["umur"] = int(umur_baru)
                    print("Umur berhasil diperbarui!")
                    break
        elif pilih_update == "c":
            while True:
                hobi_baru = input("Masukkan hobi baru: ")
                if hobi_baru == "":
                    print("Hobi tidak boleh kosong!")
                else:
                    biodata["hobi"] = hobi_baru
                    print("Hobi berhasil diperbarui!")
                    break
        elif pilih_update == "d":
            while True:
                alamat_baru = input("Masukkan alamat baru: ")
                if alamat_baru == "":
                    print("Alamat tidak boleh kosong!")
                else:
                    biodata["alamat"] = alamat_baru
                    print("Alamat berhasil diperbarui!")
                    break
        elif pilih_update == "e":
            continue
        else:
            print("Pilihan tidak valid!")
    elif pilihan == "2":
        print("\n=== DATA BIODATA ===")
        print(f"Nama   : {biodata['nama']}")
        print(f"Umur   : {biodata['umur']}")
        print(f"Hobi   : {biodata['hobi']}")
        print(f"Alamat : {biodata['alamat']}")
    elif pilihan == "3":
        print("Program selesai. Terima kasih!")
        break
    else:
        print("Pilihan tidak valid!")
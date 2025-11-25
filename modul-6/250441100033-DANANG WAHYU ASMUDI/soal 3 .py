# List utama untuk menyimpan angka
daftar_angka = []

def tambah_angka():
    print("\n=== Tambah Angka ===")
    nilai = int(input("Masukkan angka: "))
    daftar_angka.append(nilai)
    print("Angka berhasil ditambahkan!")

def tampilkan_angka():
    print("\n=== Daftar Angka ===")
    if len(daftar_angka) == 0:
        print("List masih kosong.")
    else:
        print(daftar_angka)

def ubah_angka():
    print("\n=== Ubah Angka ===")
    tampilkan_angka()
    if len(daftar_angka) == 0:
        return

    indeks = int(input("Masukkan indeks yang ingin diubah: "))
    if 0 <= indeks < len(daftar_angka):
        nilai_baru = int(input("Masukkan nilai baru: "))
        daftar_angka[indeks] = nilai_baru
        print("Data berhasil diubah!")
    else:
        print("Indeks tidak valid!")

def hapus_angka():
    print("\n=== Hapus Angka ===")
    tampilkan_angka()
    if len(daftar_angka) == 0:
        return

    indeks = int(input("Masukkan indeks yang ingin dihapus: "))
    if 0 <= indeks < len(daftar_angka):
        daftar_angka.pop(indeks)
        print("Data berhasil dihapus!")
    else:
        print("Indeks tidak valid!")

def cek_pembagian_dua_bagian():
    print("\n=== Cek Pembagian Dua Bagian Sama ===")
    if len(daftar_angka) % 2 != 0:
        print("False (jumlah elemen ganjil, tidak bisa dibagi dua sama besar)")
        return

    tengah = len(daftar_angka) // 2
    bagian_pertama = daftar_angka[:tengah]
    bagian_kedua = daftar_angka[tengah:]

    print("Bagian pertama :", bagian_pertama)
    print("Bagian kedua   :", bagian_kedua)

    if sum(bagian_pertama) == sum(bagian_kedua):
        print("True (jumlah kedua bagian sama)")
    else:
        print("False (jumlah tidak sama)")


# ====================== MENU UTAMA ======================

while True:
    print("\n===== PROGRAM PEMERIKSA DERET ANGKA =====")
    print("1. Tambah Angka (Create)")
    print("2. Tampilkan Angka (Read)")
    print("3. Ubah Angka (Update)")
    print("4. Hapus Angka (Delete)")
    print("5. Cek Pembagian Dua Bagian Sama")
    print("6. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tambah_angka()
    elif pilihan == "2":
        tampilkan_angka()
    elif pilihan == "3":
        ubah_angka()
    elif pilihan == "4":
        hapus_angka()
    elif pilihan == "5":
        cek_pembagian_dua_bagian()
    elif pilihan == "6":
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid! Coba lagi.")
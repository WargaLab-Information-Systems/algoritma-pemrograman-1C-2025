data_angka = []

def tambah_angka():
    try:
        masukan = input("Masukkan angka baru (pisahkan dengan spasi): ")
        angka_baru = [int(x) for x in masukan.split()]
        data_angka.extend(angka_baru)
        print(f"{len(angka_baru)} angka berhasil ditambahkan.")
    except ValueError:
        print("Input tidak valid! Pastikan semua input berupa angka.")

def tampilkan_angka():
    if not data_angka:
        print("Belum ada data.")
    else:
        print("Data saat ini:", data_angka)

def ubah_angka():
    tampilkan_angka()
    if not data_angka:
        return
    try:
        index = int(input("Masukkan indeks yang ingin diubah: "))
        if 0 <= index < len(data_angka):
            nilai_baru = int(input("Masukkan nilai baru: "))
            data_angka[index] = nilai_baru
            print("Data berhasil diubah.")
        else:
            print("Indeks tidak ditemukan.")
    except ValueError:
        print("Input harus berupa angka!")

def hapus_angka():
    tampilkan_angka()
    if not data_angka:
        return
    try:
        index = int(input("Masukkan indeks yang ingin dihapus: "))
        if 0 <= index < len(data_angka):
            del data_angka[index]
            print("Data berhasil dihapus.")
        else:
            print("Indeks tidak ditemukan.")
    except ValueError:
        print("Input harus berupa angka!")

def cek_keseimbangan():
    if not data_angka:
        print("Tidak ada data untuk dicek.")
        return
    
    total = sum(data_angka)
    if total % 2 != 0:
        print("False (jumlah total ganjil, tidak bisa dibagi dua sama besar)")
        return
    
    setengah = total // 2
    jumlah = 0
    for angka in data_angka:
        jumlah += angka
        if jumlah == setengah:
            print("True (bisa dibagi dua bagian sama besar)")
            return
    print("False (tidak bisa dibagi dua bagian sama besar)")

while True:
    print("\n=== PROGRAM CRUD ===")
    print("1. Tambah Angka (bisa banyak sekaligus)")
    print("2. Tampilkan Angka")
    print("3. Ubah Angka")
    print("4. Hapus Angka")
    print("5. Cek Keseimbangan")
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
        cek_keseimbangan()
    elif pilihan == "6":
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid.")
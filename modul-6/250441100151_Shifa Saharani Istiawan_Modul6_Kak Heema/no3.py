data = []  #def untuk membuat sebuah fungsi list kosong 

def tambah():
    angka = int(input("Masukkan angka: "))
    data.append(angka)
    print("Data berhasil ditambahkan!\n")

def tampil():
    print("Daftar angka:", data)

def ubah():
    tampil()
    index = int(input("Masukkan indeks data yang ingin diubah: "))
    if 0 <= index < len(data):
        data[index] = int(input("Masukkan nilai baru: "))
        print("Data berhasil diubah!\n")
    else:
        print("Indeks tidak ditemukan.\n")

def hapus():
    tampil()
    index = int(input("Masukkan indeks data yang ingin dihapus: "))
    if 0 <= index < len(data):
        del data[index]
        print("Data berhasil dihapus!\n")
    else:
        print("Indeks tidak valid.\n")

def cek_pembagian():
    total = sum(data)
    kiri = 0
    for i in range(len(data)):
        kiri += data[i]
        kanan = total - kiri
        if kiri == kanan:
            return True
    return False

while True:
    print("\n1. Tambah Data")
    print("2. Tampilkan Data")
    print("3. Ubah Data")
    print("4. Hapus Data")
    print("5. Cek Pembagian Sama")
    print("6. Keluar")

    pilih = input("Pilih menu: ")
    if pilih == "1":
        tambah()
    elif pilih == "2":
        tampil()
    elif pilih == "3":
        ubah()
    elif pilih == "4":
        hapus()
    elif pilih == "5":
        print("Hasil:", cek_pembagian())
    elif pilih == "6":
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid.")
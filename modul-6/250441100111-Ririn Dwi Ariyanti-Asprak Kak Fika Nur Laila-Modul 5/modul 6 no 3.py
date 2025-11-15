angka_list = [] 

def tampilkan_data(): 
    if len(angka_list) == 0:
        print("Belum ada data angka.")
    else:
        print("Daftar angka sekarang:", angka_list)

def tambah_data():
    angka = int(input("Masukkan angka baru: "))
    angka_list.append(angka)
    print("Angka berhasil ditambahkan!")

def hapus_data():
    tampilkan_data()
    if len(angka_list) > 0:
        angka = int(input("Masukkan angka yang ingin dihapus: "))
        if angka in angka_list:
            angka_list.remove(angka)
            print("Angka berhasil dihapus!")
        else:
            print("Angka tidak ditemukan!")

def ubah_data():
    tampilkan_data()
    if len(angka_list) > 0:
        posisi = int(input("Masukkan posisi (mulai dari 0) yang ingin diubah: "))
        if 0 <= posisi < len(angka_list):
            angka_baru = int(input("Masukkan angka baru: "))
            angka_list[posisi] = angka_baru
            print("Data berhasil diubah!")
        else:
            print("Posisi tidak valid!")


def hitung_jumlah(data):
    total = 0
    for i in data:
        total += i
    return total

def cek_sama_besar():
    if len(angka_list) % 2 != 0:
        print("Jumlah data harus genap agar bisa dibagi dua.")
        return
    
    tengah = len(angka_list) // 2
    bagian1 = angka_list[:tengah]
    bagian2 = angka_list[tengah:]
    
    print("Bagian 1:", bagian1)
    print("Bagian 2:", bagian2)
    
    total1 = hitung_jumlah(bagian1)
    total2 = hitung_jumlah(bagian2)
    
    if total1 == total2:
        print("Jumlah kedua bagian sama! Hasil: True")
    else:
        print("Jumlah kedua bagian tidak sama. Hasil: False")

while True:
    print("\n=== MENU CRUD DAFTAR ANGKA ===")
    print("1. Tambah angka")
    print("2. Hapus angka")
    print("3. Lihat semua angka")
    print("4. Ubah angka")
    print("5. Cek apakah bisa dibagi dua sama besar")
    print("6. Keluar")

    pilihan = input("Pilih menu (1-6): ")

    if pilihan == "1":
        tambah_data()
    elif pilihan == "2":
        hapus_data()
    elif pilihan == "3":
        tampilkan_data()
    elif pilihan == "4":
        ubah_data()
    elif pilihan == "5":
        cek_sama_besar()
    elif pilihan == "6":
        print("Terima kasih! Program selesai.")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")

data_angka = []

def tambah_angka():
    angka = int(input("masukkan angka: "))
    data_angka.append(angka)
    print("angka berhasil ditambahkan.")

def tampilkan_angka():
    print("daftar angka:", data_angka)

def ubah_angka():
    tampilkan_angka()
    indeks = int(input("masukkan indeks yang ingin diubah: "))
    if 0 <= indeks < len(data_angka):
        angka_baru = int(input("masukkan angka baru: "))
        data_angka[indeks] = angka_baru
        print("data berhasil diubah.")
    else:
        print("indeks tidak valid.")

def hapus_angka():
    tampilkan_angka()
    indeks = int(input("masukkan indeks yang ingin dihapus: "))
    if 0 <= indeks < len(data_angka):
        del data_angka[indeks]
        print("data berhasil dihapus.")
    else:
        print("indeks tidak valid.")

def cek_pembagian_sama():
    total = sum(data_angka)
    if total % 2 != 0:
        print("False (total ganjil, tidak bisa dibagi dua sama besar)")
        return
    setengah = total // 2
    temp = 0
    for i in range(len(data_angka)):
        temp += data_angka[i]
        if temp == setengah:
            print("True (bisa dibagi menjadi dua bagian dengan jumlah sama)")
            return
    print("False (tidak bisa dibagi dua bagian sama)")

while True:
    print("MENU PROGRAM DOMINIC")
    print("1. Tambah angka")
    print("2. Tampilkan angka")
    print("3. Ubah angka")
    print("4. Hapus angka")
    print("5. Cek pembagian dua bagian sama besar")
    print("6. Keluar")

    pilih = input("pilih menu (1-6): ")

    if pilih == '1':
        tambah_angka()
    elif pilih == '2':
        tampilkan_angka()
    elif pilih == '3':
        ubah_angka()
    elif pilih == '4':
        hapus_angka()
    elif pilih == '5':
        cek_pembagian_sama()
    elif pilih == '6':
        print("program selesai.")
        break
    else:
        print("pilihan tidak valid.")
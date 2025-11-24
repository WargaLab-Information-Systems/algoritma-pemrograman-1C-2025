#soal3
angka_list = []
def cek_sama(daftar):
    if len(daftar) % 2 != 0:
        return False
    tengah = len(daftar) // 2
    kiri = daftar[:tengah]
    kanan = daftar[tengah:]
    total_kiri = 0
    total_kanan = 0

    for i in kiri:
        total_kiri = total_kiri + i
    for j in kanan:
        total_kanan = total_kanan + j

    if total_kiri == total_kanan:
        return True
    else:
        return False
while True:
    print("\nMenu:")
    print("1. Tambah angka")
    print("2. Tampilkan angka")
    print("3. Ubah angka")
    print("4. Hapus angka")
    print("5. Cek apakah bisa dibagi dua bagian sama besar")
    print("6. Keluar")

    pilihan = input("Pilih menu: ")
    if pilihan == "1":
        angka = int(input("Masukkan angka: "))
        angka_list.append(angka)
        print("Angka berhasil ditambahkan.")

    elif pilihan == "2":
        if len(angka_list) == 0:
            print("Belum ada data.")
        else:
            print("Daftar angka:", angka_list)

    elif pilihan == "3":
        if len(angka_list) == 0:
            print("Belum ada data.")
        else:
            print("Data sekarang:", angka_list)
            posisi = int(input("Masukkan indeks yang ingin diubah: "))
            if posisi >= 0 and posisi < len(angka_list):
                angka_baru = int(input("Masukkan angka baru: "))
                angka_list[posisi] = angka_baru
                print("Data berhasil diubah.")
            else:
                print("Indeks tidak ditemukan.")

    elif pilihan == "4":
        if len(angka_list) == 0:
            print("Belum ada data.")
        else:
            print("Data sekarang:", angka_list)
            posisi = int(input("Masukkan indeks yang ingin dihapus: "))
            if posisi >= 0 and posisi < len(angka_list):
                angka_list.pop(posisi)
                print("Data berhasil dihapus.")
            else:
                print("Indeks tidak ditemukan.")

    elif pilihan == "5":
        if len(angka_list) == 0:
            print("Belum ada data.")
        else:
            hasil = cek_sama(angka_list)
            print("Hasil pengecekan:", hasil)

    elif pilihan == "6":
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid.")



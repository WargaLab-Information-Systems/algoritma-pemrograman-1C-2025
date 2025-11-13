def deretan_angka(daftar):
    total = sum(daftar)
    if total % 2 != 0:
        return False
    setengah = total // 2
    sementara = 0
    for angka in daftar:
        sementara = sementara + angka
        if sementara == setengah:
            return True
    return False

daftar_angka = []
while True:
    print("\n=== PROGRAM DERETAN ANGKA ===")
    print("1. Tambah angka")
    print("2. Tampilkan angka")
    print("3. Ubah angka")
    print("4. Hapus angka")
    print("5. Cek apakah bisa dibagi dua sama besar")
    print("6. Keluar")
    pilih = input("Pilih menu (1-6): ")
    if pilih == '1':
        try:
            data = input("Masukkan angka (pisahkan dengan spasi): ")
            angka_baru = list(map(int, data.split()))
            daftar_angka.extend(angka_baru)
            print("Data berhasil ditambahkan.")
        except ValueError:
            print("Pastikan semua input berupa angka!")
    elif pilih == '2':
        print("Daftar angka:", daftar_angka if daftar_angka else "Kosong")
    elif pilih == '3':
        if not daftar_angka:
            print("Daftar masih kosong.")
        else:
            try:
                indeks = int(input("Masukkan indeks yang ingin diubah: "))
                if 0 <= indeks < len(daftar_angka):
                    angka_baru = int(input("Masukkan angka baru: "))
                    daftar_angka[indeks] = angka_baru
                    print("Data berhasil diubah.")
                else:
                    print("Indeks tidak ditemukan.")
            except ValueError:
                print("Input tidak valid.")
    elif pilih == '4':
        if not daftar_angka:
            print("Daftar masih kosong.")
        else:
            try:
                indeks = int(input("Masukkan indeks yang ingin dihapus: "))
                if 0 <= indeks < len(daftar_angka):
                    daftar_angka.pop(indeks)
                    print("Data berhasil dihapus.")
                else:
                    print("Indeks tidak ditemukan.")
            except ValueError:
                print("Input tidak valid.")
    elif pilih == '5':
        if not daftar_angka:
            print("Daftar kosong, tidak bisa diperiksa.")
        else:
            hasil = deretan_angka(daftar_angka)
            print("Hasil:", hasil)
    elif pilih == '6':
        print("Program selesai. Terima kasih!")
        break
    else:
        print("Pilihan tidak valid, silakan coba lagi.")
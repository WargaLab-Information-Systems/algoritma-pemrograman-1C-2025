# Program CRUD untuk Mengecek Daftar Angka Berjumlah Sama

angka_list = []

def cek_sama_besar():
    total = sum(angka_list)
    if total % 2 != 0:
        return False  # Jika jumlah total ganjil, pasti tidak bisa dibagi dua sama besar

    half = total // 2
    jumlah_sementara = 0

    for angka in angka_list:
        jumlah_sementara += angka
        if jumlah_sementara == half:
            return True
    return False

while True:
    print("\n=== PROGRAM CRUD DAFTAR ANGKA ===")
    print("1. Tambah Angka")
    print("2. Tampilkan Angka")
    print("3. Ubah Angka")
    print("4. Hapus Angka")
    print("5. Cek Apakah Bisa Dibagi Dua Sama Besar")
    print("6. Keluar")

    pilih = input("Pilih menu (1-6): ")

    if pilih == "1":
        try:
            nilai = int(input("Masukkan angka baru: "))
            angka_list.append(nilai)
            print("Angka berhasil ditambahkan.")
        except ValueError:
            print("I  nput harus berupa angka!")

    elif pilih == "2":
        print("Daftar angka:", angka_list if angka_list else "Masih kosong.")

    elif pilih == "3":
        try:
            idx = int(input("Masukkan indeks yang ingin diubah: "))
            if 0 <= idx < len(angka_list):
                nilai_baru = int(input("Masukkan nilai baru: "))
                angka_list[idx] = nilai_baru
                print("Data berhasil diubah.")
            else:
                print("Indeks tidak ditemukan.")
        except ValueError:
            print("Input harus berupa angka!")

    elif pilih == "4":
        try:
            idx = int(input("Masukkan indeks yang ingin dihapus: "))
            if 0 <= idx < len(angka_list):
                del angka_list[idx]
                print("Data berhasil dihapus.")
            else:
                print("Indeks tidak ditemukan.")
        except ValueError:
            print("Input harus berupa angka!")

    elif pilih == "5":
        if len(angka_list) < 2:
            print("Data terlalu sedikit untuk diperiksa.")
        else:
            hasil = cek_sama_besar()
            print("Hasil pemeriksaan:", hasil)

    elif pilih == "6":
        print("Program dihentikan.")
        break

    else:
        print("Pilihan tidak valid!")

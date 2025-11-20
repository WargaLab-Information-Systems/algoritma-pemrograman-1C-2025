# List untuk menyimpan angka
angka_list = []

# Fungsi Create (Tambah data)
def tambah_angka():
    try:
        angka = int(input("Masukkan angka: "))
        angka_list.append(angka)
        print(f"{angka} berhasil ditambahkan.")
    except ValueError:
        print("Harap masukkan angka valid.")

# Fungsi Read (Tampilkan data)
def tampilkan_angka():
    if angka_list:
        print("Daftar angka:", angka_list)
    else:
        print("Daftar kosong.")

# Fungsi Update (Ubah data)
def ubah_angka():
    if not angka_list:
        print("Daftar kosong.")
        return
    tampilkan_angka()
    try:
        index = int(input("Masukkan indeks angka yang ingin diubah: "))
        if index < 0 or index >= len(angka_list):
            print("Indeks tidak valid.")
            return
        angka_baru = int(input("Masukkan angka baru: "))
        angka_list[index] = angka_baru
        print("Data berhasil diperbarui.")
    except ValueError:
        print("Harap masukkan angka valid.")

# Fungsi Delete (Hapus data)
def hapus_angka():
    if not angka_list:
        print("Daftar kosong.")
        return
    tampilkan_angka()
    try:
        index = int(input("Masukkan indeks angka yang ingin dihapus: "))
        if index < 0 or index >= len(angka_list):
            print("Indeks tidak valid.")
            return
        angka_terhapus = angka_list.pop(index)
        print(f"{angka_terhapus} berhasil dihapus.")
    except ValueError:
        print("Harap masukkan angka valid.")

# Fungsi untuk cek apakah list bisa dibagi menjadi dua bagian dengan jumlah sama
def cek_bagian_sama_sederhana():
    if not angka_list:
        print("Daftar kosong.")
        return

    total = 0
    for num in angka_list:
        total += num

    if total % 2 != 0:
        print("False (tidak bisa dibagi menjadi dua bagian sama besar)")
        return

    target = total // 2

    # Fungsi rekursif untuk cek subset
    def cek_subset(index, sisa_target):
        if sisa_target == 0:
            return True
        if index >= len(angka_list):
            return False
        # Pilih elemen index atau lewati elemen index
        return cek_subset(index + 1, sisa_target - angka_list[index]) or cek_subset(index + 1, sisa_target)

    if cek_subset(0, target):
        print("True (bisa dibagi menjadi dua bagian sama besar)")
    else:
        print("False (tidak bisa dibagi menjadi dua bagian sama besar)")


# Menu utama
while True:
    print("\n=== MENU ===")
    print("1. Tambah angka")
    print("2. Tampilkan angka")
    print("3. Ubah angka")
    print("4. Hapus angka")
    print("5. Cek dua bagian sama")
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
        cek_bagian_sama_sederhana()
    elif pilihan == "6":
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid.")

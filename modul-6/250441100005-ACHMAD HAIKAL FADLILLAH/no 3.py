angka_list = []

def create_data():
    print("=== TAMBAH ANGKA DALAM DERET ===")
    try:
        angka = int(input("Masukkan angka baru: "))
        angka_list.append(angka)
        print("Angka berhasil ditambahkan!")
    except ValueError:
        print("Input tidak valid! Masukkan angka bulat (integer).")

def read_data():
    print("=== DAFTAR ANGKA ===")
    if not angka_list:
        print("Belum ada data angka.")
    else:
        print("Data saat ini:", angka_list)

def update_data():
    print("=== UBAH ANGKA ===")
    if not angka_list:
        print("Belum ada data untuk diubah.")
        return
    try:
        index = int(input("Masukkan indeks angka yang ingin diubah (mulai dari 0): "))
        if 0 <= index < len(angka_list):
            angka_baru = int(input("Masukkan angka baru: "))
            angka_list[index] = angka_baru
            print("Data berhasil diperbarui!")
        else:
            print("Indeks tidak valid!")
    except ValueError:
        print("Input harus berupa angka!")

def delete_data():
    print("=== HAPUS ANGKA ===")
    if not angka_list:
        print("Belum ada data untuk dihapus.")
        return
    try:
        index = int(input("Masukkan indeks angka yang ingin dihapus (mulai dari 0): "))
        if 0 <= index < len(angka_list):
            angka_terhapus = angka_list.pop(index)
            print(f"Angka {angka_terhapus} berhasil dihapus!")
        else:
            print("Indeks tidak valid!")
    except ValueError:
        print("Input harus berupa angka!")

def cek_pembagian_sama():
    print("=== CEK PEMBAGIAN DUA BAGIAN ===")
    if not angka_list:
        print("Belum ada data angka untuk diperiksa.")
        return
    
    total = 0
    for angka in angka_list:
        total += angka

    if total % 2 != 0:
        print("Total ganjil, tidak bisa dibagi dua bagian sama besar.")
        print("Hasil: False")
        return
    
    setengah = total // 2
    akumulasi = 0

    for i in range(len(angka_list)):
        akumulasi += angka_list[i]
        if akumulasi == setengah:
            bagian1 = angka_list[:i+1]
            bagian2 = angka_list[i+1:]
            print("Dapat dibagi menjadi dua bagian dengan jumlah sama!")
            print("Bagian 1:", bagian1)
            print("Bagian 2:", bagian2)
            print("Hasil: True")
            return
    
    print("Tidak dapat dibagi menjadi dua bagian dengan jumlah sama.")
    print("Hasil: False")

while True:
    print("\n========= PILIHAN MENU =========")
    print("1. Tambah Angka (Create)")
    print("2. Tampilkan Angka (Read)")
    print("3. Ubah Angka (Update)")
    print("4. Hapus Angka (Delete)")
    print("5. Cek Pembagian Dua Bagian Sama (Check)")
    print("6. Keluar")
    
    pilihan = input("Pilih menu (1-6): ")
    
    if pilihan == "1":
        create_data()
    elif pilihan == "2":
        read_data()
    elif pilihan == "3":
        update_data()
    elif pilihan == "4":
        delete_data()
    elif pilihan == "5":
        cek_pembagian_sama()
    elif pilihan == "6":
        print("Terima kasih! Program selesai.")
        break
    else:
        print("Pilihan tidak valid, coba lagi.")

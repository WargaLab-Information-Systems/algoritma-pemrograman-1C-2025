def tampilkan_menu():
    print("\n=== PROGRAM CRUD DERET ANGKA ===")
    print("1. Tambah Angka (Create)")
    print("2. Tampilkan Angka (Read)")
    print("3. Ubah Angka (Update)")
    print("4. Hapus Angka (Delete)")
    print("5. Periksa Pembagian Dua Bagian")
    print("6. Keluar")

def tambah_angka(data):
    try:
        deret = input("Masukkan angka (pisahkan dengan koma, contoh: 1,2,3,4): ")
        for x in deret.split(','):
            data.append(int(x))
        print("Angka berhasil ditambahkan!")
    except ValueError:
        print("Input tidak valid! Pastikan hanya angka yang dipisahkan dengan koma.")

def tampilkan_data(data):
    if not data:
        print("Daftar masih kosong.")
    else:
        print("Daftar angka saat ini:", data)

def ubah_data(data):
    if not data:
        print("Daftar masih kosong, tidak ada data yang bisa diubah.")
        return
    tampilkan_data(data)
    try:
        index = int(input("Masukkan indeks data yang ingin diubah (mulai dari 0): "))
        if 0 <= index < len(data):
            nilai_baru = int(input("Masukkan nilai baru: "))
            data[index] = nilai_baru
            print("Data berhasil diubah!")
        else:
            print("Indeks tidak valid.")
    except ValueError:
        print("Input harus berupa angka!")

def hapus_data(data):
    if not data:
        print("Daftar masih kosong, tidak ada data yang bisa dihapus.")
        return
    tampilkan_data(data)
    try:
        index = int(input("Masukkan indeks data yang ingin dihapus (mulai dari 0): "))
        if 0 <= index < len(data):
            data.pop(index)
            print("Data berhasil dihapus!")
        else:
            print("Indeks tidak valid.")
    except ValueError:
        print("Input harus berupa angka!")

def cek_pembagian_sama(data):
    if not data:
        print("Daftar masih kosong.")
        return
    
    total = 0
    for i in data:
        total += i
    
    if total % 2 != 0:
        print("Hasil: False (Total ganjil, tidak bisa dibagi dua sama besar)")
        return
    
    setengah = total // 2
    sementara = 0
    for i in range(len(data)):
        sementara += data[i]
        if sementara == setengah:
            print(f"Bagian kiri : {data[:i+1]}")
            print(f"Bagian kanan: {data[i+1:]}")
            print("Hasil: True (Dapat dibagi menjadi dua bagian sama besar)")
            return
    print("Hasil: False (Tidak dapat dibagi menjadi dua bagian sama besar)")

data = []

while True:
    tampilkan_menu()
    pilihan = input("Pilih menu (1-6): ")

    if pilihan == "1":
        tambah_angka(data)
    elif pilihan == "2":
        tampilkan_data(data)
    elif pilihan == "3":
        ubah_data(data)
    elif pilihan == "4":
        hapus_data(data)
    elif pilihan == "5":
        cek_pembagian_sama(data)
    elif pilihan == "6":
        print("Program selesai. Terima kasih!")
        break
    else:
        print("Pilihan tidak valid, coba lagi.")

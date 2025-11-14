data = []
def create(data):
    try:
        angka = int(input("Masukkan angka baru: "))
        data.append(angka)
        print("Angka berhasil ditambahkan!")
    except ValueError:
        print("Input harus berupa angka!")

def read(data):
    if len(data) == 0:
        print("List masih kosong.")
    else:
        print("Data saat ini:", data)

def update(data):
    if len(data) == 0:
        print("List kosong, tidak ada yang diubah.")
        return
    try:
        index = int(input("Masukkan indeks yang ingin diubah: "))
        if index >= 0 and index < len(data):
            nilai_baru = int(input("Masukkan nilai baru: "))
            data[index] = nilai_baru
            print("Data berhasil diperbarui!")
        else:
            print("Indeks tidak valid.")
    except ValueError:
        print("Input harus berupa angka!")

def delete(data):
    if len(data) == 0:
        print("List kosong, tidak ada yang dihapus.")
        return
    try:
        index = int(input("Masukkan indeks yang ingin dihapus: "))
        if index >= 0 and index < len(data):
            data.pop(index)
            print("Data berhasil dihapus!")
        else:
            print("Indeks tidak valid.")
    except ValueError:
        print("Input harus berupa angka!")

def cek_pembagian_sama(data):
    total = 0
    for i in data:
        total += i

    if total % 2 != 0:
        return False 

    separuh = total // 2
    jumlah = 0

    for i in range(len(data)):
        jumlah += data[i]
        if jumlah == separuh:
            return True
    return False

while True:
    print("\n=== MENU CRUD LIST ANGKA ===")
    print("1. Tambah data (Create)")
    print("2. Tampilkan data (Read)")
    print("3. Ubah data (Update)")
    print("4. Hapus data (Delete)")
    print("5. Cek apakah bisa dibagi dua bagian dengan jumlah sama")
    print("6. Keluar")

    pilihan = input("Pilih menu (1-6): ")
    if pilihan == "1":
        create(data)
    elif pilihan == "2":
        read(data)
    elif pilihan == "3":
        update(data)
    elif pilihan == "4":
        delete(data)
    elif pilihan == "5":
        hasil = cek_pembagian_sama(data)
        print("Hasil:", hasil)
    elif pilihan == "6":
        print("Program selesai. Terima kasih!")
        break
    else:
        print("Pilihan tidak valid, coba lagi.")
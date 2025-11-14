def create(data):
    angka = input("Masukkan angka: ")
    if not angka.isdigit():
        print("Input harus angka!")
        return
    data.append(int(angka))
    print("Angka berhasil ditambahkan")

def read(data):
    if not data:
        print("Data masih kosong")
    else:
        print("Daftar angka:", data)

def update(data):
    read(data)
    if data:
        index = input("Masukkan indeks yang mau diubah: ")
        if not index.isdigit():
            print("Input harus angka!")
            return
        index = int(index)
        if 0 <= index < len(data):
            baru = input("Masukkan angka baru: ")
            if not baru.isdigit():
                print("Input harus angka!")
                return
            data[index] = int(baru)
            print("Data berhasil diubah")
        else:
            print("Indeks tidak ditemukan")

def delete(data):
    read(data)
    if data:
        index = input("Masukkan indeks yang mau dihapus: ")
        if not index.isdigit():
            print("Input harus angka!")
            return
        index = int(index)
        if 0 <= index < len(data):
            data.pop(index)
            print("Data berhasil dihapus")
            read(data)
        else:
            print("Indeks tidak valid")

def cek_sama(data):
    if sum(data) % 2 != 0:
        return False
    setengah = sum(data) // 2
    total = 0
    for i in data:
        total += i
        if total == setengah:
            return True
    return False

data = []

while True:
    print("\n1. Tambah")
    print("2. Lihat")
    print("3. Ubah")
    print("4. Hapus")
    print("5. Cek sama")
    print("6. Keluar")

    pilih = input("Pilih menu: ")

    if not pilih.isdigit():
        print("Input harus angka!")
        continue

    if pilih == "1":
        create(data)
    elif pilih == "2":
        read(data)
    elif pilih == "3":
        update(data)
    elif pilih == "4":
        delete(data)
    elif pilih == "5":
        print("Hasil:", cek_sama(data))
    elif pilih == "6":
        print("Program selesai")
        break
    else:
        print("Pilihan salah")

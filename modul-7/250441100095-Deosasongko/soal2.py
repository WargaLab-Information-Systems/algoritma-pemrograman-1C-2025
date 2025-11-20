inventaris = {}

def id_valid(i):
    return i.isalnum()     # hanya huruf dan angka

def nama_valid(n):
    return n.replace(" ", "").isalpha()   # hanya huruf & spasi

def tampil():
    if not inventaris:
        print("Tidak ada barang.\n")
    else:
        for i, (n, h, s) in inventaris.items():
            print(f"ID:{i} | Nama:{n} | Harga:{h} | Stok:{s}")
        print()

def cari():
    i = input("ID barang: ")
    print(inventaris.get(i, "Barang tidak ditemukan.\n"))

def tambah():
    i = input("ID: ").strip()

    if not id_valid(i):
        print("ID hanya boleh huruf atau angka, tidak boleh simbol!\n")
        return

    if i in inventaris:
        print("ID sudah ada!\n")
        return

    n = input("Nama: ").strip()
    if not nama_valid(n):
        print("Nama hanya boleh huruf dan spasi!\n")
        return

    try:
        h = float(input("Harga: "))
        s = int(input("Stok: "))
        if s < 0:
            print("Stok tidak boleh negatif!\n")
            return
    except:
        print("Input harga/stok tidak valid!\n")
        return

    inventaris[i] = [n, h, s]
    print("Barang ditambahkan.\n")

def update():
    i = input("ID barang: ")
    if i not in inventaris:
        print("Barang tidak ditemukan.\n")
        return
    try:
        t = int(input("Perubahan stok (+/-): "))
        if inventaris[i][2] + t < 0:
            print("Stok tidak boleh negatif!\n")
            return
        inventaris[i][2] += t
        print("Stok diperbarui.\n")
    except:
        print("Input harus angka!\n")

def hapus():
    i = input("ID barang: ")
    print("Barang dihapus.\n") if inventaris.pop(i, None) else print("Tidak ditemukan.\n")

while True:
    print("1.Tampil  2.Cari  3.Tambah  4.Update  5.Hapus  6.Keluar")
    p = input("Pilih: ")
    if p == "1": tampil()
    elif p == "2": cari()
    elif p == "3": tambah()
    elif p == "4": update()
    elif p == "5": hapus()
    elif p == "6": break
    else: 
        print("Pilihan salah!\n")
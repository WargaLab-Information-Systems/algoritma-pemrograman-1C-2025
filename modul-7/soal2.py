inv = {}

def tampil():
    if not inv:
        print("Data kosong")
    else:
        for i,d in inv.items():
            print(f"ID:{i} | Nama:{d[0]} | Harga:{d[1]} | Stok:{d[2]}")

def cari():
    i = input("ID: ")
    if i in inv:
        print(inv[i])
    else:
        print("Tidak ditemukan")

def tambah():
    i = input("ID: ")
    if i in inv: 
        return print("ID sudah ada")
    try:
        n = input("Nama: ")
        h = int(input("Harga: "))
        s = int(input("Stok: "))
        if s < 0: 
            return print("Stok tidak boleh negatif")
        inv[i] = [n, h, s]
        print("Ditambah")
    except:
        print("Harga/Stok harus angka")

def update():
    i = input("ID: ")
    if i not in inv: 
        return print("Tidak ditemukan")
    try:
        new_id = input("ID baru (kosong = tidak diganti): ")
        if new_id.strip() != "":
            if new_id in inv:
                return print("ID baru sudah ada")
            inv[new_id] = inv.pop(i)
            i = new_id   

        print("Nama lama:", inv[i][0])
        new_name = input("Nama baru (kosong = tidak diganti): ")
        if new_name.strip() != "":
            inv[i][0] = new_name

        print("Harga lama:", inv[i][1])
        new_price = input("Harga baru (kosong = tidak diganti): ")
        if new_price.strip() != "":
            try:
                inv[i][1] = int(new_price)
            except:
                return print("Harga harus angka")

        u = int(input("Perubahan stok (+/-): "))
        if inv[i][2] + u < 0: 
            return print("Stok tidak boleh negatif")
        inv[i][2] += u
        print("Stok diupdate")

    except:
        print("Harus angka")

def hapus():
    i = input("ID: ")
    print(inv.pop(i, "Tidak ditemukan"))

while True:
    print("\n=== MENU ===")
    print("1. Tampil")
    print("2. Cari")
    print("3. Tambah")
    print("4. Update Stok")
    print("5. Hapus")
    print("0. Keluar")

    p = input("Pilih: ")
    if p=="1": tampil()
    elif p=="2": cari()
    elif p=="3": tambah()
    elif p=="4": update()
    elif p=="5": hapus()
    elif p=="0": break
    else: 
        print("Pilihan salah")

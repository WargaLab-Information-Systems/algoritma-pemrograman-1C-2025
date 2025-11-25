inventaris = {}

def tampil():
    if not inventaris: print("Kosong."); return
    for i, d in inventaris.items():
        print(i, d)

def cari():
    i = input("ID: ").upper()
    print(inventaris.get(i, "Tidak ditemukan")) 

def tambah():
    i = input("ID baru: ").upper()
    if i in inventaris: return print("ID sudah ada")
    n = input("Nama: ")
    h = int(input("Harga: "))
    s = int(input("Stok: "))
    inventaris[i] = [n, h, s]

def update():
    i = input("ID: ").upper()
    if i not in inventaris: return print("Tidak ditemukan") 
    t = int(input("Perubahan stok (+/-): "))
    if inventaris[i][2] + t < 0: return print("Stok tidak boleh negatif")
    inventaris[i][2] += t 

def hapus():
    i = input("ID: ").upper()
    print(inventaris.pop(i, "Tidak ditemukan")) 

def menu():
    while True:
        print("\n1.Tampil 2.Cari 3.Tambah 4.Update 5.Hapus 6.Keluar")
        p = input("Pilih: ")
        if p=="1": tampil()
        elif p=="2": cari()
        elif p=="3": tambah()
        elif p=="4": update()
        elif p=="5": hapus()
        elif p=="6": break
        else: print("Pilihan salah")

menu()
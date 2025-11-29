inventaris={


}

id_awal=int(0)

def tampilkan_data():
    print("=================================daftar inventaris gudang=================================")
    for nama,value in inventaris.items():
        print(f"ID =           [{nama}]")
        print(f"NAMA BARANG  = [{value[0]}]")
        print(f"HARGA BARANG = [Rp.{value[1]:,}]")
        print(f"STOK         = [{value[2]}]")
        print()

def membuat_id():
    global id_awal
    id=id_awal
    inventaris[id]=[]
    id_awal=id_awal+1
    nama_produk=str(input("input nama produk"))
    harga=int(input("input harga porduk"))
    stok=int(input("input stok "))
    inventaris[id]=[nama_produk,harga,stok]

def mencari_produk_lewat_index():
    while True:
        input_id=int(input("input ID yang ingin yang di cari"))
        if inventaris.get(input_id) is not None:
            print(f"barang di temukan ")
            break
        else:
            print("barang tidak di temukan")   

def perbarui_stok():
    while True:
        input_id=int(input("input ID yang ingin yang di perbarui stok nya"))
        if inventaris.get(input_id) is not None:
            inisialisasi_proses=int(input("[TAMBAH stok = 1, KURANGI stok = 2] ="))
            if inisialisasi_proses == 1:
                tambah=int(input("input menambah berapa stok = "))
                inventaris[input_id][2]= inventaris[input_id][2] + tambah
                break
            elif inisialisasi_proses == 2:
                while True:
                    kurang=int(input("input mengurangi berapa stok = "))
                    cek = inventaris[input_id][2] - kurang
                    if cek<0:
                        print("bilangan pengurang terlalu besar dan hasil negatif")
                    elif cek>0:
                        inventaris[input_id][2]= inventaris[input_id][2] -kurang
                        print(f"stok tersisa = {inventaris[input_id][2]}")
                        break
                    elif cek==0:
                        print("stok habis ")
                        inventaris[input_id][2]= inventaris[input_id][2] -kurang
                        break
        else:
            print("barang tidak di temukan")   

def hapus_barang():
    while True:
        input_inisialisasi=int(input("input id yang ingin di hapus"))
        if inventaris.get(input_inisialisasi)is not None:
            del inventaris[input_inisialisasi]
            break
        else:
            print("inputan tidak ada di inventaris ")

def menu():
    while True:
        pilihan=int(input(" [0 = program selesai,1 = menambah jenis barang, 2 = mencari barang berdasarkan id , 3 = menampilkan data inventaris gudang, 4= perbarui stok , 5 = menghapus barang ] = "))
        if pilihan in [0,1,2,3,4,5]:
            return pilihan
        else:
            print("input tidak sesuai kriteria ")

while True:
    pilih=menu()
    if pilih==0:
        print("program selesai")
        break
    elif pilih==1:
        membuat_id()
    elif pilih==2:
        mencari_produk_lewat_index()
    elif pilih==3:
        tampilkan_data()
    elif pilih==4:
        perbarui_stok()
    elif pilih==5:
        hapus_barang()
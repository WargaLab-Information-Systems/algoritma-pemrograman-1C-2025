tampungan_global=[]
global_nama_santri=[]
jawa=[]
sumatra=[]
kalimantan=[]

def proses(nama,daerah,nama_santri):
    tampungan_global.append(nama)
    global_nama_santri.append(nama_santri)
    while True:
        if daerah=="jawa":
            jawa.append(nama)
            break
        elif daerah=="sumatra":
            sumatra.append(nama)
            break
        elif daerah=="kalimantan":
            kalimantan.append(nama)
            break
        else:
             pass

def kalimantan_():
    print("===========daftar kalimantan=========")
    if len(kalimantan)==0 :
         pass
    else:
        for k in kalimantan:
            v_k=tampungan_global.index(k)#index
            print("nama = ",k," id= [",v_k,"] nama santri = ",global_nama_santri[v_k])

def sumatra_():#fungsi mengetahui id pengunjung sumatra dan cetak 
    print("===========daftar sumatra============")
    if len(sumatra)==0 :
         pass
    else:
        for s in sumatra:
            v_s=tampungan_global.index(s)
            print("nama pengunjung id= ",s," = [",v_s,"] nama santri = ",global_nama_santri[v_s])
     
def jawa_():#fungsi menambah antrean
    print("===========daftar jawa===============")
    if len(jawa)==0 :
         pass
    else:
        for i in jawa:
            v_j=tampungan_global.index(i)
            print("nama = ",i," id= [",v_j,"] nama santri = ",global_nama_santri[v_j])


def hapus(angka):# fungsi menghapus data 
    pencarian_nama_index=tampungan_global[angka]
    print(pencarian_nama_index)
    if pencarian_nama_index in jawa:
            jawa.remove(pencarian_nama_index)
    if pencarian_nama_index in kalimantan:
            kalimantan.remove(pencarian_nama_index) 
    if pencarian_nama_index in sumatra:
             sumatra.remove(pencarian_nama_index)
             


def start():
    print("="*5,"INPUT NAMA DAN DAERAH PENGUNJUNG","="*5,"KETIK 'selesai' untuk mengakhiri penambahan pengunjung ")
    while True:
        nama=str(input("input nama pengunjung : "))
        if nama == "selesai":
            print("menampilkan data")
            sumatra_()
            kalimantan_()
            jawa_()
            break
        else:
            while True:
                 daerah=str(input("input daerah : "))
                 if daerah not in ["jawa","kalimantan","sumatra"]:
                      print("tidak masuk kriteria daerah")
                 else:
                      break
            nama_santri=str(input("input nama santri = "))
            proses(nama,daerah,nama_santri)
            pass

def update_hapus():
    while True:
        kualifikasi=(input(f"input nomer yang ingin di hapus, N = tidak =  "))
        if kualifikasi not in ["N","n"]:
            angka=int(kualifikasi)
            hapus(angka)
        else:
            print("MENAMPILKAN DATA")
            sumatra_()
            kalimantan_()
            jawa_()   
            break
    
def menu():
    tabel_pilihan=int(input(f"[TAMBAH DATA PENGUNJUNG = 1] [HAPUS DATA = 2 ][TAMPILKAN DATA PENGUNJUNG = 3 ] [PROGRAM SELESAI = 0]  = "))
    return tabel_pilihan

while True:
    pilihan=menu()
    if pilihan==0:
         print("program selesai")
         break
    elif pilihan==1:
         start()
    elif pilihan==2:
         update_hapus()
    elif pilihan==3:
         sumatra_()
         kalimantan_()
         jawa_()

         


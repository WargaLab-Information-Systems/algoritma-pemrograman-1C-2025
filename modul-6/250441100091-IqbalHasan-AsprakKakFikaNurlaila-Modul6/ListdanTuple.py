# #Percobaan Tugas Pendahuluan
# #Contoh List (menambah)
list = [1,2,3, 'mangga']
list.append('durian') 
print(list)

# #Contoh List (menghapus)
list = [1,2,3, 'mangga']
# #menghapus list menggunakan remove()
list.remove('mangga')
print(list)
# #menghapus list menggunakan del sesuai indeks
del list [0]
print(list)

#Akses nilai dalam tuple
mobil = ('alphart','toyota','L300')
print(mobil)


# #Memperbarui nilai dalam tuple
mobil = ('alphard','toyoya','L300')
mobilanyar = mobil + ('volkswagen')
print(mobil)

# #Menghapus nilai dalam tuple
angkaA = (4,5,6,7)
angka = (1,2,3)
del angka
print(angkaA)

# #Perulangan List & Tuple
# #perulangan list maupun tuple
tup = ('cincin', 'anting', 'gelang')
i = 0
while i < len (tup):
    print(tup[i])
    i=i+1

# #Membuat sebuah kombinasi
# #loop kombinasi
outfit = ('baju', 'celana', 'rok')
for i in outfit:
    for j in outfit:
        for k in outfit:
            print('kombinasi outfit hari ini',i,j,k)

#soal tp no 3
lis = ["beras", "gula", "minyak"]
print(lis)

tupel = (10, 20)
print(tupel)

# #soal tp no 6
daftar_belanja = ["telur", "roti", "susu"]
daftar_belanja.append("keju")
daftar_belanja.remove("roti")
print("Daftar belanja terbaru:", daftar_belanja)













# #Praktikum

# #CRUD (Create/Update)
buah= ["jeruk","apel","mangga","pisang"]
buah.append("durian")
print(buah)

buah.insert(1,"markisa")
print(buah)

buah.extend(["kiwi","nanas"])
print(buah)

# #CRUD (Read)
buah1 = buah.index("apel")
print(buah1)

buah2 = buah.count("durian")
print(buah2)


# #CRUD (Remove)
buah.remove("apel")
print(buah)

buah.pop(3)
print(buah)

# #Untuk mengurutkan sesuai abjad
buah.sort()
print(buah)
buah.reverse()
print(buah)


buah3 = buah.copy()
print(buah3)
buah.clear()
print(buah)



# #Fungsi
# #===List===
angka = [10,20,30,40,50]
pangjang_len = len (angka)
print("Panjang list adalah:", pangjang_len)
# #Menjumlahkan nilai
sum_angka = sum(angka)
print ("Jum;ah total element dalam list adalah:",sum_angka)
# #Nilai terbesar
max_angka = max (angka)
print("Nilai maksimum dalam list adalah:", max_angka)
# #Nilai terkecil
min_angka = min (angka)
print("Nilai manimal dalam list adalah:", max_angka)


# #===Tuple===

# # slicing
## nilai sebelum 2
nilai = (1,2,3,4,5)
satu = nilai[:2] 
print(satu)
##nilai setelah 2
dua = nilai [2:]
print(dua)
##dimuali dari 2 sampai sebelum 4
tiga = nilai [2:4]
print(tiga)
##angka terakhir
empat = nilai[-1]
print(empat)
##loncat 2
lima = nilai [::2]
print(lima)

# #List dalam list
# #Hanya bisa di ubah di bagian list bukan tuple
Tuple1= (1,(1,2),[4,5])
hasil = Tuple1 [2][1]
print(hasil)

# #List compreshention
data = [1,2,3,4,5]
hasil1 = [x**2 for x in data if x % 2 == 0]
print(hasil1)

warna = ["merah","hijau","biru"]
for a in warna:
    for b in warna:
        print(a,b)



































#Tugas 1
print("=== Soal 1 ===")
print("Soal: Buatlah program sistem kunjungan santri yang dapat menginputkan nama pengunjung, nama santri yang dijenguk, daerah asal pengunjung (Sumatra, Kalimantan, atau Jawa), dan mendapat id_antrian di setiap pengunjung. Program harus menggunakan satu list utama yang menyimpan seluruh data kunjungan, di mana setiap elemen di dalam list berisi sub-list beranggotakan tiga data tersebut. Program harus memiliki fitur untuk menambah data pengunjung, menampilkan seluruh daftar pengunjung, dan menghapus data pengunjung berdasarkan id_antrian. Data kunjungan harus dikelompokkan dan ditampilkan berdasarkan daerah asal dengan urutan: ")
print("- Pengunjung daerah Sumatra ditampilkan terlebih dahulu.")
print("- Pengunjung daerah Kalimantan ditampilkan setelah Sumatra.")
print("- Pengunjung daerah Jawa ditampilkan terakhir.")
print("===============")


DataUtamaKunjungan = []
id_antrian = 1

##validasi nama
def NamaValid(s):
    if s == "":
        return False
    for char in s:
        if not ((char >= "A" and char <= "Z") or (char >= "a" and char <= "z") or char == " "):
            return False
    return True

##validasi daerah
def DaerahValid(s):
    if s == "Sumatra" or s == "sumatra":
        return True
    if s == "Kalimantan" or s == "kalimantan":
        return True
    if s == "Jawa" or s == "jawa":
        return True
    return False

##ubah string ke integer
def UbahAngka(teks):
    if teks == "":
        return None
    hasil = 0
    for ch in teks:
        if ch == "0":
            angka = 0
        elif ch == "1":
            angka = 1
        elif ch == "2":
            angka = 2
        elif ch == "3":
            angka = 3
        elif ch == "4":
            angka = 4
        elif ch == "5":
            angka = 5
        elif ch == "6":
            angka = 6
        elif ch == "7":
            angka = 7
        elif ch == "8":
            angka = 8
        elif ch == "9":
            angka = 9
        else:
            return None
        hasil = hasil * 10 + angka
    return hasil

while True:
    print("=== KUNJUNGAN SANTRI ===")
    print("1. Tambah Data Pengunjung")
    print("2. Tampilkan Semua Data")
    print("3. Hapus Data Berdasarkan ID Antrian")
    print("4. Keluar")

##validasi menu utama
    while True:
        pilihan = input("Pilih menu (1/2/3/4): ")
        if pilihan in ["1", "2", "3", "4"]:
            break
        else:
            print("Input tidak valid! Harus pilih 1, 2, 3, atau 4.")

##tambah data
    if pilihan == "1":
        print("--- Tambah Data Pengunjung ---")

##validasi nama pengunjung
        while True:
            NamaPengunjung = input("Masukkan nama pengunjung: ")
            if NamaValid(NamaPengunjung):
                break
            else:
                print("Nama pengunjung tidak valid! (hanya huruf dan spasi). Coba lagi.")

##validasi nama santri
        while True:
            NamaSantri = input("Masukkan nama santri yang dijenguk: ")
            if NamaValid(NamaSantri):
                break
            else:
                print("Nama santri tidak valid! (hanya huruf dan spasi). Coba lagi.")

##validasi daerah
        while True:
            AsalDaerah = input("Masukkan daerah asal (Sumatra/Kalimantan/Jawa): ")
            if DaerahValid(AsalDaerah):
                break
            else:
                print("Input daerah asal tidak valid! (harus Sumatra, Kalimantan, atau Jawa). Coba lagi.")

##simpan data
        data = [id_antrian, NamaPengunjung, NamaSantri, AsalDaerah]
        DataUtamaKunjungan.append(data)
        print("Data berhasil ditambahkan dengan ID antrian:", id_antrian)
        id_antrian = id_antrian + 1

##tampilkan data
    elif pilihan == "2":
        print("--- Daftar Kunjungan Santri ---")
        if len(DataUtamaKunjungan) == 0:
            print("Belum ada data kunjungan.")
        else:
            print("ID  | Nama Pengunjung   | Nama Santri       | Daerah Asal")
            print("-------------------------------------------------------------")

            UrutanDaerah = ["Sumatra", "Kalimantan", "Jawa"]

            for daerah in UrutanDaerah:
                for data in DataUtamaKunjungan:
                    if data[3] == daerah or data[3] == daerah.lower():
##kolom agarr sejajar
                        id_text = str(data[0])
                        NamaPengunjung = data[1]
                        NamaSantri = data[2]
                        AsalDaerah = data[3]

                        while len(id_text) < 3:
                            id_text = id_text + " "
                        while len(NamaPengunjung) < 17:
                            NamaPengunjung = NamaPengunjung + " "
                        while len(NamaSantri) < 17:
                            NamaSantri = NamaSantri + " "
                        while len(AsalDaerah) < 12:
                            AsalDaerah = AsalDaerah + " "

                        print(id_text + "| " + NamaPengunjung + "| " + NamaSantri + "| " + AsalDaerah)

##hapus data
    elif pilihan == "3":
        print("--- Hapus Data Pengunjung ---")

        if len(DataUtamaKunjungan) == 0:
            print("Belum ada data untuk dihapus.")
        else:
            while True:
                hapus_text = input("Masukkan ID Antrian yang ingin dihapus: ")
                if hapus_text == "":
                    print("Input kosong. Masukkan ID angka yang valid.")
                    continue

                hapus_id = UbahAngka(hapus_text)
                if hapus_id is None:
                    print("ID harus angka. Coba lagi.")
                    continue
                else:
                    break

            ditemukan = 0
            for i in range(len(DataUtamaKunjungan)):
                if DataUtamaKunjungan[i][0] == hapus_id:
                    del DataUtamaKunjungan[i]
                    ditemukan = 1
                    print("Data berhasil dihapus.")
                    break

            if ditemukan == 0:
                print("Data dengan ID tersebut tidak ditemukan.")

##keluar dari program
    elif pilihan == "4":
        print("Program selesai. Terima kasih!")
        break





#Tugas 2
print("=== Soal 2 ===")
print("Soal: -")
print("===============")


t1 = (3, 1, 4)
t2 = (1, 5, 9)

print("Tuple pertama :", t1)
print("Tuple kedua   :", t2)

##menggabungkan kedua tuple
gabung = ()
for i in t1:
    gabung = gabung + (i,)
for j in t2:
    gabung = gabung + (j,)

print("Hasil penggabungan tuple (sebelum hapus duplikat):", gabung)

##hapus angka duplikat
sementara = []
for angka in gabung:
    ada = 0
    for x in sementara:
        if angka == x:
            ada = 1
            break
    if ada == 0:
        sementara.append(angka)
print("angka dihapus angka duplikat (dalam list sementara):", sementara)

##urutan menurun
for i in range(len(sementara)):
    for j in range(i + 1, len(sementara)):
        if sementara[i] < sementara[j]:
            temp = sementara[i]
            sementara[i] = sementara[j]
            sementara[j] = temp 

print("Setelah diurutkan menurun (list sementara):", sementara)

##mengubah ke tuple
hasil = ()
for angka in sementara:
    hasil = hasil + (angka,)

print("=== HASIL AKHIR ===")
print("Tuple hasil penggabungan tanpa duplikat dan urut menurun:", hasil)





#Tugas 3
print("=== Soal 3 ===")
print("Soal: Dominic Szoboszlai memiliki deretan angka dan ingin membuat program untuk memeriksa apakah deretan tersebut dapat dibagi menjadi dua bagian Algoritma & Dasar Pemrograman | List & Tuple Modul VI dengan jumlah yang sama. Program ini dibuat berbasis CRUD (Create, Read, Update, Delete), di mana pengguna dapat menambah, menampilkan, mengubah, dan menghapus angka dalam sebuah list Python. Setelah data tersimpan, program harus mampu mengecek apakah daftar angka dapat dipisahkan menjadi dua bagian yang memiliki total nilai sama besar. Sebagai contoh, jika daftar angka adalah [1, 2, 3, 3, 2, 1], maka dapat dibagi menjadi dua bagian [1, 2, 3] dan [3, 2, 1], yang keduanya berjumlah 6. Karena jumlah kedua bagian sama, program akan menampilkan hasil True; jika tidak sama, hasilnya False.")
print("================")


DataUtama = []

def jum_manual(daftar):
    total = 0
    for angka in daftar:
        total = total + angka
    return total

def ubah_angka(teks):
    if teks == "":
        return None
    hasil = 0
    for ch in teks:
        if ch == "0":
            nilai = 0
        elif ch == "1":
            nilai = 1
        elif ch == "2":
            nilai = 2
        elif ch == "3":
            nilai = 3
        elif ch == "4":
            nilai = 4
        elif ch == "5":
            nilai = 5
        elif ch == "6":
            nilai = 6
        elif ch == "7":
            nilai = 7
        elif ch == "8":
            nilai = 8
        elif ch == "9":
            nilai = 9
        else:
            return None
        hasil = hasil * 10 + nilai
    return hasil

while True:
    print("=== LIST ANGKA DOMINIC ===")
    print("1. Tambah Angka")
    print("2. Tampilkan Semua Angka")
    print("3. Ubah Angka")
    print("4. Hapus Angka")
    print("5. Cek Pembagian Dua Bagian Sama")
    print("6. Keluar")

##menu
    while True:
        pilih = input("Pilih menu (1/2/3/4/5/6): ").lower()
        if pilih == "keluar" or pilih == "stop":
            pilih = "6"
            break
        elif pilih in ["1", "2", "3", "4", "5", "6"]:
            break
        else:
            print("Input tidak valid! Pilih antara 1–6.")

##create
    if pilih == "1":
        print("--- Tambah Data Angka ---")
        while True:
            angka_input = input("Masukkan angka (atau ketik 's' untuk berhenti): ").lower()
            if angka_input == "s":
                break
            if angka_input == "":
                print("Input kosong, coba lagi.")
                continue

            angka_baru = ubah_angka(angka_input)
            if angka_baru is None:
                print("Input harus angka! Coba lagi.")
            elif angka_baru == 0:
                print("Angka tidak boleh 0! Coba lagi.")
            else:
                DataUtama.append(angka_baru)
                print("Angka", angka_baru, "berhasil ditambahkan.")

##read
    elif pilih == "2":
        print("--- Daftar Angka Saat Ini ---")
        if len(DataUtama) == 0:
            print("Belum ada data.")
        else:
            print("Index | Nilai")
            print("-----------------")
            for i in range(len(DataUtama)):
                idx_text = str(i)
                nilai_text = str(DataUtama[i])
                while len(idx_text) < 5:
                    idx_text = idx_text + " "
                while len(nilai_text) < 5:
                    nilai_text = nilai_text + " "
                print(idx_text + "| " + nilai_text)

##update
    elif pilih == "3":
        print("--- Ubah Angka ---")
        if len(DataUtama) == 0:
            print("Belum ada data untuk diubah.")
        else:
            print("Daftar Angka Saat Ini:")
            print("Index | Nilai")
            print("-----------------")
            for i in range(len(DataUtama)):
                idx_text = str(i)
                nilai_text = str(DataUtama[i])
                while len(idx_text) < 5:
                    idx_text = idx_text + " "
                while len(nilai_text) < 5:
                    nilai_text = nilai_text + " "
                print(idx_text + "| " + nilai_text)

            while True:
                idx_input = input("Masukkan index data yang ingin diubah: ")
                if idx_input == "":
                    print("Input tidak boleh kosong!")
                    continue
                idx = ubah_angka(idx_input)
                if idx is None:
                    print("Index harus angka.")
                elif idx < 0 or idx >= len(DataUtama):
                    print("Index di luar jangkauan.")
                else:
                    break

            while True:
                angka_input = input("Masukkan nilai baru: ")
                if angka_input == "":
                    print("Input tidak boleh kosong!")
                    continue
                angka_baru = ubah_angka(angka_input)
                if angka_baru is None:
                    print("Input harus angka!")
                elif angka_baru == 0:
                    print("Angka tidak boleh 0! Coba lagi.")
                else:
                    print("Data index", idx, "bernilai", DataUtama[idx], "berhasil diubah menjadi", angka_baru)
                    DataUtama[idx] = angka_baru
                    break

##delate
    elif pilih == "4":
        print("--- Hapus Angka ---")
        if len(DataUtama) == 0:
            print("Belum ada data untuk dihapus.")
        else:
            print("Daftar Angka Saat Ini:")
            print("Index | Nilai")
            print("-----------------")
            for i in range(len(DataUtama)):
                idx_text = str(i)
                nilai_text = str(DataUtama[i])
                while len(idx_text) < 5:
                    idx_text = idx_text + " "
                while len(nilai_text) < 5:
                    nilai_text = nilai_text + " "
                print(idx_text + "| " + nilai_text)

            while True:
                hapus_input = input("Masukkan index data yang ingin dihapus: ")
                if hapus_input == "":
                    print("Input tidak boleh kosong!")
                    continue
                idx = ubah_angka(hapus_input)
                if idx is None:
                    print("Index harus angka.")
                elif idx < 0 or idx >= len(DataUtama):
                    print("Index di luar jangkauan.")
                else:
                    print("Data dengan nilai", DataUtama[idx], "berhasil dihapus.")
                    del DataUtama[idx]
                    break

##pembagian
    elif pilih == "5":
        print("--- Cek Pembagian Dua Bagian Sama ---")
        if len(DataUtama) == 0:
            print("Belum ada data.")
        else:
            total = jum_manual(DataUtama)
            if total % 2 == 1:
                print("Total ganjil, tidak bisa dibagi dua bagian sama. Hasil: False")
            else:
                setengah = total // 2
                jumlah_kiri = 0
                bisa = False
                for i in range(len(DataUtama)):
                    jumlah_kiri = jumlah_kiri + DataUtama[i]
                    if jumlah_kiri == setengah:
                        bisa = True
                        break
                if bisa:
                    print("Daftar angka dapat dibagi menjadi dua bagian sama. Hasil: True")
                else:
                    print("Tidak bisa dibagi menjadi dua bagian sama. Hasil: False")

##keluar
    elif pilih == "6":
        print("Program selesai. Terima kasih!")
        break

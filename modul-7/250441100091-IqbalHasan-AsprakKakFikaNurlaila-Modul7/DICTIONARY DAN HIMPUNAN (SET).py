##Mencoba Modul 7
# #Contoh cara membuat Dictionary pada Python

# dict = {'Name': 'Zara', 'Age' : 7, 'Class': 'First'}
# print("dict['Name']:,dict['Name']")
# print("dict['Age']:, dict['Age']")

# # #Update dictionary python
# dict = {'Nama': 'Zara', 'Age': 7, 'Class': 'First'}
# dict['Age'] = 8            # Mengubah entri yang sudah ada
# dict['School'] = "DPS School"   # Menambah entri baru

# print("dict['Age']: ", dict['Age'])
# print("dict['School']: ", dict['School'])


# ##Contoh cara menghapus pada Dictionary Python
# dict = {'Nama': 'Zara', 'Age': 7, 'Class': 'First'}

# del dict ['Nama']   ##hapus entri dengan key 'Nama'
# dict.clear()        ##hapus semua entri di dict
# del dict            ##hapus dictionary yang sudah ada

# print("dict['Age']: ", dict['Age'])
# print("dict['School']: ", dict['School'])


# set1 = set() # deklarasi set kosong
# set1.add(1) # menambahkan isi set1

# #>>> A = {1, 2, 3, 4, 5} >>> B = {4, 5, 6, 7, 8}
# # use union function
# >>> A.union(B)
# {1, 2, 3, 4, 5, 6, 7, 8}
# # use union function on B
# >>> B.union(A)
# {1, 2, 3, 4, 5, 6, 7, 8}

# # use intersection function on A
# >>> A.intersection(B)
# {4, 5}
# # use intersection function on B
# >>> B.intersection(A)
# {4, 5}


# # use difference function on A
# >>> A.difference(B)
# {1, 2, 3}
# # use - operator on B
# >>> B - A
# {8, 6, 7}
# # use difference function on B
# >>> B.difference(A)
# {8, 6, 7}

# # use symmetric_difference function on A
# >>> A.symmetric_difference(B)
# {1, 2, 3, 6, 7, 8}
# # use symmetric_difference function on B
# >>> B.symmetric_difference(A)
# {1, 2, 3, 6, 7, 8}


# ##Soal Tp No 2
# nilai = {'Ani':85,'Budi':90,'Citra':78,'Doni':88}
# tertinggi = max(nilai, key=nilai.get)
# print("Tertinggi:", tertinggi, nilai[tertinggi])
# rata = sum(nilai.values())/len(nilai)
# print("Rata-rata:", rata)


# # #Soal Tp No 3
# basket={'Ani','Budi','Citra'}
# futsal={'Budi','Doni','Eka'}
# print(basket|futsal)
# print(basket&futsal)
# print(basket-futsal)

# ##Soal Tp No 6 (contoh salah)
# {[1,2]:'data'}






















# ##praktikum modul 7 
# ##Contoh set
# himpunan = {1,2,5,5}
# print(himpunan)

# ##Elemen dari set tidak dapat duplikat
# himpunan = {1,1,1,2,2,2}
# print(himpunan)


# ##penggabungan sementara (jangan terfokus ke union)
# himpunan_1 = {1,True}
# print(himpunan_1)
# himpunan_2 = {0,False}
# print(himpunan_2)

# himpunan_3 = himpunan_1.union(himpunan_2)
# print(himpunan_3)

# ##Menambah dan menghapus elemen ke dalam set
# himpunan ={2,1,4}
# himpunan.add(5)
# print(f"Setelah di tambah: {himpunan}")


# ##remove
# himpunan.remove(2) ###menghapus angka 2
# print(f"Setelah di hapus: {himpunan}")

# ##Operasi Himpunan Union (Gabungan)
# himpunan_1 = {1,3,5}
# himpunan_2 = {5,6,10}
# irisan = himpunan_1.intersection(himpunan_2)
# print(irisan)

# ##Operasi himpunan differance (perbedaan)
# himpunan_1 = {1,3,5}
# himpunan_2 = {5,6,10}
# perbedaan_himpunan_1 = himpunan_1.difference(himpunan_2)
# perbedaan_himpunan_2 = himpunan_2.difference(himpunan_1)
# print (perbedaan_himpunan_1)
# print(perbedaan_himpunan_2)

# ##Operasi himpunan symmetric difference (perbedaan simetris)
# himpunan_1 = {1,3,5}
# himpunan_2 = {5,6,10}
# perbedaan_simetris_1 = himpunan_1.symmetric_difference(himpunan_2)
# perbedaan_simetris_2 = himpunan_2.symmetric_difference(himpunan_1)

# print (perbedaan_simetris_1)
# print(perbedaan_simetris_2)


# ##contoh dictionary
# biodata = {
#     "nama": "anton",
#     "hobi": "Lari Maraton"
# }
# print(biodata)


# ##(Read) mengakses elemen dictionary
# biodata = {
#     "nama": "anton",
#     "hobi": "Lari Maraton"
# }
# print(f"Nama anda adalah : {biodata["nama"]}")
# print(f"Hobi anda adalah : {biodata["hobi"]}")


# ##(Update) 
# biodata = {
#     "nama": "anton",
#     "hobi": "Lari Maraton"
# }

# ##tampilkan kondisi aawal
# print(biodata)

# ##edit value dari key nama
# biodata["nama"] = "Adit"

# ##Tampilkan konndisi akhir
# print(biodata)

# ##menambah elemen baru key yang belum terdefinisi
# biodata["alamat"] = "Sidoarjo"
# print(biodata)

# ##jika sudah ada, maka update
# biodata["alamat"] = "kediri"
# ##tampilkan 
# print(biodata)

# ##Delate) menghapus elemen dari dictionary
# biodata = {
#     "nama": "anton",
#     "alamat": "kediri",
#     "hobi": "Lari Maraton"
# }

# ##menampilkan kondisi awal
# print(biodata)

# ##menghapus hobi dengan pop
# yang_dihapus = biodata.pop("hobi")
# print(biodata)
# print(f"/nYang dihapus: {yang_dihapus}/n")

# ##menghapus alamat dengan del
# del biodata["alamat"]

# ##menampilkan kondisi akhir
# print(biodata)


# ##  
# daftar_mahasiswa = {
#     "24-091": "Mhs A",
#     "angkatan": 2024,
#     "hobi": ["Membaca", "Menggambar"]
# } 
# #     {"24-01": { "Mhs B",
# #     "angkatan": 2024,
# #     "hobi": ["Bermain game"]}

# for nim, data_mhs in daftar_mahasiswa.items():
#     print(f"NIM: {nim}")

#     for key, value in data_mhs.items():
#         print(f"\t{key}: {value}")

# ##memberikan new line
# print()































# # ##Tugas Praktikum
# # ##Soal 1
# # print("Soal 1")
# # print("SOAL: ")
# # print("====================")

# Kontak = {}

# def NamaValid(n):
#     return n.replace(" ", "").isalpha()

# def NomerValid(no):
#     return no.isdigit() and len(no) >= 10

# def EmailValid(e):
#     return "@" in e and "." in e and e.count("@") == 1

# while True:
#     print("=== CONTACT BOOK ===")
#     print("1. Tampilkan Semua Kontak")
#     print("2. Cari Kontak")
#     print("3. Tambah Kontak")
#     print("4. Perbarui Email Kontak")
#     print("5. Hapus Kontak")
#     print("6. Keluar")

#     pilih = input("Pilih menu (1–6): ")
#     if pilih not in ["1","2","3","4","5","6"]:
#         print("Pilihan tidak valid!\n")
#         continue

# ##read
#     if pilih == "1":
#         print("\n--- Semua Kontak ---")
#         if not Kontak:
#             print("Belum ada kontak.\n")
#         else:
#             for nama in Kontak:
#                 print(f"Nama: {nama} | Nomor: {Kontak[nama][0]} | Email: {Kontak[nama][1]}")
#             print()

# ##search
#     elif pilih == "2":
#         nama = input("Masukkan nama yang dicari: ").lower()
#         ditemukan = False

#         for key in Kontak:
#             if key.lower() == nama:
#                 print(f"Nama: {key} | Nomor: {Kontak[key][0]} | Email: {Kontak[key][1]}\n")
#                 ditemukan = True
#                 break
#         if not ditemukan:
#             print("Kontak tidak ditemukan.\n")

# ##create
#     elif pilih == "3":
#         while True:
#             nama = input("Masukkan nama kontak: ").strip()
#             if NamaValid(nama):
#                 break
#             print("Nama tidak valid!")

#         while True:
#             nomor = input("Masukkan nomor telepon: ")
#             if NomerValid(nomor):
#                 break
#             print("Nomor telepon tidak valid!")

#         while True:
#             email = input("Masukkan email: ")
#             if EmailValid(email):
#                 break
#             print("Email tidak valid!")

#         Kontak[nama] = [nomor, email]
#         print("Kontak berhasil ditambahkan!\n")

# ##update
#     elif pilih == "4":
#         nama = input("Masukkan nama kontak: ").strip()

#         if nama not in Kontak:
#             print("Kontak tidak ditemukan.\n")
#         else:
#             while True:
#                 email = input("Masukkan email baru: ")
#                 if EmailValid(email):
#                     break
#                 print("Email tidak valid!")

#             Kontak[nama][1] = email
#             print("Email berhasil diperbarui!\n")

# ##delate
#     elif pilih == "5":
#         nama = input("Masukkan nama kontak: ")
#         if nama in Kontak:
#             del Kontak[nama]
#             print("Kontak berhasil dihapus!\n")
#         else:
#             print("Kontak tidak ditemukan.\n")

#     else:
#         print("Program selesai.")
#         break































# # ##Tugas Praktikum
# # ##Soal 2
# # print("Soal 2")
# # print("SOAL: ")
# # print("====================")

# Inventaris = {}

# while True:
#     print("=== INVENTARIS GUDANG ===")
#     print("1. Tampilkan Semua Barang")
#     print("2. Cari Barang Berdasarkan ID")
#     print("3. Tambah Barang")
#     print("4. Perbarui Stok Barang")
#     print("5. Hapus Barang")
#     print("6. Keluar")

#     pilih = input("Pilih menu (1–6): ")
#     if pilih not in ["1","2","3","4","5","6"]:
#         print("Pilihan tidak valid!\n")
#         continue

# ##read
#     if pilih == "1":
#         print("\n--- Daftar Semua Barang ---")
#         if not Inventaris:
#             print("Belum ada data barang.\n")
#         else:
#             print("ID         | Nama Barang       | Harga     | Stok")
#             print("---------------------------------------------------")
#             for ID, data in Inventaris.items():
#                 nama, harga, stok = data
#                 print(f"{ID:<10}| {nama:<18}| {harga:<10}| {stok}") #lebar kolom
#             print()

# ##search
#     elif pilih == "2":
#         print("\n--- Cari Barang Berdasarkan ID ---")
#         print("(ketik 0 untuk kembali)")
#         while True:
#             kode = input("Masukkan ID barang: ").strip()
#             if kode == "0":
#                 print()
#                 break
#             if kode in Inventaris:
#                 data = Inventaris[kode]
#                 print(f"ID: {kode} | Nama: {data[0]} | Harga: {data[1]} | Stok: {data[2]}\n")
#                 break
#             print("Barang tidak ditemukan!\n")

# ##create
#     elif pilih == "3":
#         print("\n--- Tambah Barang ---")

#         while True:
#             ID = input("Masukkan ID barang: ").strip()
#             if ID == "":
#                 print("ID tidak boleh kosong.")
#             elif ID in Inventaris:
#                 print("ID sudah digunakan!")
#             else:
#                 break

#         while True:
#             nama = input("Masukkan nama barang: ").strip()
#             if nama != "":
#                 break
#             print("Nama tidak boleh kosong!")

#         while True:
#             harga = input("Masukkan harga barang: ")
#             if harga.isdigit():
#                 harga = int(harga)
#                 break
#             print("Harga harus angka!")

#         while True:
#             stok = input("Masukkan stok barang: ")
#             if stok.isdigit():
#                 stok = int(stok)
#                 break
#             print("Stok harus angka!")

#         Inventaris[ID] = [nama, harga, stok]
#         print("Barang berhasil ditambahkan!\n")

# ##update
#     elif pilih == "4":
#         print("\n--- Perbarui Stok Barang ---")
#         print("(ketik 0 untuk kembali)")
#         while True:
#             kode = input("Masukkan ID barang: ")
#             if kode == "0":
#                 print()
#                 break
#             if kode in Inventaris:
#                 while True:
#                     stok = input("Masukkan stok baru: ")
#                     if stok.isdigit():
#                         Inventaris[kode][2] = int(stok)
#                         print("Stok berhasil diperbarui!\n")
#                         break
#                     print("Stok harus angka!")
#                 break
#             print("Barang tidak ditemukan!")

# ##delate
#     elif pilih == "5":
#         print("\n--- Hapus Barang ---")
#         print("(ketik 0 untuk kembali)")
#         while True:
#             kode = input("Masukkan ID barang: ")
#             if kode == "0":
#                 print()
#                 break
#             if kode in Inventaris:
#                 del Inventaris[kode]
#                 print("Barang berhasil dihapus!\n")
#                 break
#             print("Barang tidak ditemukan!")

#     else:
#         print("Program selesai. Terima kasih!")
#         break

































# ##Tugas Praktikum
# ##Soal 3
# print("Soal 3")
# print("SOAL: ")
# print("====================")

# Kupon = {
#     "HEMAT10": 10,
#     "DISKON20": 20,
#     "PROMO5": 5
# }

# while True:
#     print("=== SISTEM KASIR - KUPON DISKON ===")
#     print("1. Tampilkan Semua Kupon")
#     print("2. Proses Transaksi")
#     print("3. Keluar")

#     pilih = input("Pilih menu (1/2/3): ")
#     if pilih not in ["1","2","3"]:
#         print("Input tidak valid!\n")
#         continue

# ##read
#     if pilih == "1":
#         print("\n--- Daftar Kupon Tersedia ---")
#         if not Kupon:
#             print("Tidak ada kupon yang tersedia.\n")
#         else:
#             print("Kode Kupon   | Diskon (%)")
#             print("---------------------------")
#             for kode, disk in Kupon.items():
#                 print(f"{kode:<12}| {disk}")
#             print()

# ##proses
#     elif pilih == "2":
#         print("\n--- Proses Transaksi ---")

#         while True:
#             total = input("Masukkan total belanja: ")
#             if total.isdigit():
#                 total = int(total)
#                 break
#             print("Total harus angka!\n")

#         if not Kupon:
#             print("Semua kupon habis. Tidak ada diskon.")
#             diskon = 0
#         else:
#             print("Ketik 0 jika tidak ingin memakai kupon.")

#             while True:
#                 kode = input("Masukkan kode kupon: ")
#                 if kode == "0":
#                     diskon = 0
#                     break
#                 if kode in Kupon:
#                     diskon = Kupon[kode]
#                     print("Kupon valid! Diskon:", diskon, "%")
#                     del Kupon[kode]
#                     break
#                 print("Kupon tidak valid!\n")

#         potongan = total * diskon // 100
#         bayar   = total - potongan

#         print(f"Total belanja: {total}")
#         print(f"Potongan: {potongan}")
#         print(f"Total bayar: {bayar}\n")

#     else:
#         print("Program selesai. Terima kasih!")
#         break

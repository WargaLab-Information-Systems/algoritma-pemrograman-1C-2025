# # # # Dasar Teori Fungsi(Teks Untuk word lapres)
# # # def halo_dunia():
# # #     print'Halo Dunia!'

# # # halo_dunia() # Memanggil fungsi halo_dunia
# # # halo_dunia() # Memanggil fungsi halo_dunia lagi

# # # def<nama_fungsi>(arg1, arg2, arg3), ...., argN):
# # #         <statemen-statemen>
# # #         ...
# # #         return <value> 

# # # lambda argumen1, argumen2, ..., argumenN: expression using arguments

# # # Latihan Praktikum Fungsi

# # # Latihan 2.1
# # # Contoh penggunaan fungsi  
# def ucapan ():
#     print("selamat malam")

# ucapan()

# def masukkan_data():
#     nama = str(input("Masukkan nama: "))
#     NRP = int(input("Masukkan NIM: "))

# def cetak_string():
#     print("Ini adalah fungsi yang mencetak string")
#     print("silahkan masukkan data")

# cetak_string()
# masukkan_data()

# # # contoh program dengan melibatkan nilai balik (return)
# def perkalian(a, b):
#     c = a * b
#     return c

# print(perkalian(5, 10))

# # # contoh penggunaan fungsi lambda
# f = lambda x, y , z: x + y + z
# print (f(10, 20, 30))

# z = (lambda a = "tic", b = "tac", c = "toe": a + b + c)
# print (z("ZOO"))

# # # contoh penggunaan scope variable
# def contohScope():
#     X = 10 
#     print("Nilai X di dalam fungsi, x =", X)

# X = 30
# print ("nilai X di luar fungsi, X =", X)

# contohScope(X)



# # # Soal No 6 Dasar Teori Fungsi
# def hitung_tagihan(kwh):
#     tarif = 1500
#     total = kwh * tarif
#     return total

# def kategori_penggunaan(kwh):
#     if kwh >= 500:
#         return "Penggunaan Tinggi"
#     else:
#         return "Penggunaan Normal"

# # Program utama
# pemakaian = int(input("Masukkan jumlah pemakaian listrik (kWh): "))
# total_tagihan = hitung_tagihan(pemakaian)
# kategori = kategori_penggunaan(pemakaian)

# print("Total tagihan listrik: Rp", total_tagihan)
# print("Kategori:", kategori)









# # # Praktikum 
# def sapa():
#     print("Haloo Dunia!")

# # sapa()

# def sapa2():
#     sapa()
#     print ("haloo saya menyapa dua kali")

# sapa2()

# def tambah(a, b):
#     c = a + b 
#     print ("hasil penjumlahan :",c)
#     return c

# tambah(3,4)




# # # lambda 1
# tambah= lambda x, y , z: x + y + z
# print (tambah(10,2,5))
# print (tambah(3,5,7))

# # #lambda 2
# print((lambda k:k*3)(3))
# print((lambda k:k*3)(6))




# # # fungsi rekursif
# def faktorial (n):
#     if n == 1:
#         return 1
#     else:
#         return n * faktorial(n-1)
    
# print (faktorial(3))

# 3 * faktorial(2)
# 2 * faktorial(1)
# 1


# # #soal no 6 tp
# def hitung_tagihan(kwh):
#     tarif = 1500
#     total = kwh * tarif
#     return total

# def kategori_penggunaan(kwh):
#     if kwh >= 500:
#         return "tinggi"
#     else:
#         return "normal"

# print("===== Program menghitung tagihan listrik =====")
# kwh = int(input("Masukkan jumlah pemakaian listrik (kWh): "))
# total_tagihan = hitung_tagihan(kwh)
# kategori = kategori_penggunaan(kwh)

# print("===== TOTAL BIAYA YANG HARUS DI BAYARKAN =====")
# print("Total tagihan listrik: Rp", total_tagihan)
# print("Kategori:", kategori)
# print("Program selesai, Terima Kasih!")


# #edisi mengide lamba banyak
# tambah= lambda x, y , z, t, u , v , w: x + y + z + t + u + v + w
# print (tambah(10,2,5,1,2,3,4))
# print (tambah(3,5,7,8,9,10,11))



# # # fungsi rekursif
# def faktorial (n):
#     if n == 1:
#         return 1
#     else:
#         return n * faktorial(n)
    
# angka=input("masukkan angka:")
# print("faktorial dari",angka,"adalah",faktorial(angka))
# # print (faktorial(3))
# # 3 * faktorial(2)
# # 2 * faktorial(1)



























# # # Tugas Praktikum
# # # Soal 1
# print("========== Soal 1 ==========")
# print("SOAL: Seorang penjaga gudang bernama Pak Tungtung menghadapi masalah yaitu kesulitan membuka brankas tua yang menyimpan hardisk berisi private key dan publik key Bitcoin miliknya. Pak Tungtung ingin membuat fungsi rekursif python yang menerima input bilangan bulat non-negatif N dan mengembalikan hasil faktorial N! tersebut. Fungsi ini harus menggunakan prinsip rekursif (def) untuk menyelesaikan perhitungan. Bantulah Pak Tungtung membuat kode function untuk menghitung faktorial dari nilai N tersebut. Pastikan program bersifat dinamis!")
# print("============================")


# def fakto(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * fakto(n - 1) # #rekrusif

# while True:
#     N = input("Masukkan bilangan bulat positif (atau 'q' untuk keluar): ")
#     if N.lower() == "q":
#         print("Program selesai. Terima kasih!")
#         break
#     if not N.isdigit():
#         print("Input harus berupa bilangan bulat positif!")
#         continue
#     N = int(N)
#     if N < 0:
#         print("Input tidak boleh negatif!")
#         continue

#     hasil = fakto(N)
#     print("Faktorial dari", N, "adalah", hasil)




























# #Soal 2
# print("========== Soal 2 ==========")
# print("SOAL: Priman sedang belajar pemrograman Python dan ingin membuat sebuah fungsi yang dapat menentukan apakah dua kata merupakan anagram atau bukan. Program harus bersifat dinamis, yaitu pengguna dapat memasukkan dua kata secara langsung melalui input. Jika kedua kata tersebut merupakan anagram, fungsi harus mengembalikan nilai True, dan jika tidak maka mengembalikan False. Program juga harus menampilkan hasil akhir yang menunjukkan apakah kedua kata tersebut anagram atau bukan!")
# print("============================")


# def anagram(kata1, kata2):
#     kata1 = kata1.replace(" ", "").lower()
#     kata2 = kata2.replace(" ", "").lower()
#     if sorted(kata1) == sorted(kata2):
#         return True
#     else:
#         return False


# while True:
#     kata1 = input("Masukkan kata pertama : ")
#     kata2 = input("Masukkan kata kedua   : ")

#     if kata1.replace(" ", "").isalpha() and kata2.replace(" ", "").isalpha():
#         if anagram(kata1, kata2):
#             print(kata1, "dan", kata2, "adalah anagram.")
#         else:
#             print(kata1, "dan", kata2, "bukan anagram.")
#     else:
#         print("Input hanya boleh berisi huruf dan spasi!")

#     lanjut = input("Coba lagi? (y/n): ").lower()
#     if lanjut != "y":
#         print("Program selesai. Terima kasih!")
#         break











































# Soal 3
print("========== Soal 3 ==========")
print("SOAL: Sebuah perusahaan membutuhkan program yang dapat menghitung gaji bersih bulanan karyawan secara dinamis setelah memperhitungkan Pajak Penghasilan (PPh) tetap sebesar 5% dari gaji pokok. Program harus menggunakan sebuah function yang menerima input nama karyawan, jabatan, dan gaji pokok. Jika jabatan karyawan adalah “Manager”, maka karyawan mendapatkan tunjangan 10% dari gaji pokok, sedangkan jika “Staff”, tunjangannya 5%. Function harus menghitung gaji bersih setelah dikurangi pajak dan ditambah tunjangan, lalu menampilkan hasil perhitungan secara lengkap!")
print("============================")


def HitungGajiBersih(nama, jabatan, GajiPokok):
    pajak = int(0.05 * GajiPokok)
    if jabatan.lower() == "manager":
        tunjangan = int(0.10 * GajiPokok)
    elif jabatan.lower() == "staff":
        tunjangan = int(0.05 * GajiPokok)
    else:
        tunjangan = 0
    GajiBersih = GajiPokok - pajak + tunjangan
    print("=== HASIL PERHITUNGAN GAJI ===")
    print("Nama Karyawan :", nama)
    print("Jabatan       :", jabatan)
    print("Gaji Pokok    : Rp", GajiPokok)
    print("Pajak (5%)    : Rp", pajak)
    print("Tunjangan     : Rp", tunjangan)
    print("Gaji Bersih   : Rp", GajiBersih)
    print("==============================")

while True:
    print("=== PROGRAM HITUNG GAJI ===")
    while True:
        nama = input("Masukkan nama karyawan : ")
        if nama.replace(" ", "").isalpha():
            break
        else:
            print("Nama hanya boleh berisi huruf dan spasi!")

    while True:
        jabatan = input("Masukkan jabatan (Manager/Staff): ")
        if jabatan.replace(" ", "").isalpha():
            break
        else:
            print("Jabatan hanya boleh huruf (Manager/Staff)!")

    while True:
        gaji = input("Masukkan gaji pokok (angka): ")
        if gaji.isdigit():
            gaji = int(gaji)
            if gaji > 0:
                break
            else:
                print("Gaji pokok harus lebih dari 0!")
        else:
            print("Input gaji harus berupa angka bulat!")
    HitungGajiBersih(nama, jabatan, gaji)

    ulang = input("Hitung gaji karyawan lain? (y/n): ").lower()
    if ulang != "y":
        print("Program selesai. Terima kasih!")
        break

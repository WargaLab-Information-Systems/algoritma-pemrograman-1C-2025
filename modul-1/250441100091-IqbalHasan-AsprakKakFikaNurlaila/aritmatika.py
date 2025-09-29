# #Note: Tidak menjalankan kode keseluruhan secara langsung#
# print ("=" * 100)
# print ("Latihan 1")
# print ("=" * 100)
# print ("-" * 100)
# print ("a.Di bawah ini adalah contoh program implementasi operator aritmatika pada bahasa pemrograman Python:")
# print ("-" * 100)
# a = 10
# b = 5
# print ("a =", a)
# print ("b =", b)
# print ("=" * 100)

# print("Hasil Penjumlahan (a + b) =", a + b)
# print("Hasil Pengurangan (a - b) =", a - b)
# print("Hasil Perkalian (a * b) =", a * b)
# print("Hasil Pangkat (a ** b) =", a ** b)
# print("Hasil Pembagian (a / b) =", a / b)
# print("Hasil Pembagian Bulat (a // b) =", a // b)
# print("Hasil Sisa Bagi (a % b) =", a % b)

# print ("-" * 100)
# print ("b.Selesaikanlah soal dibawah ini dengan menggunakan Operasi Aritmatika")
# print ("-" * 100)

# print (10 + 5)
# kursi_204 = 30
# kursi_308 = 20
# jumlah = kursi_204 + kursi_308 
# print ("jumlah kursi_204 + kursi_308 =", jumlah)

# print ("=" * 100)
# print ("PERINTAH: Coba ganti operasi aritmatika di atas menjadi pengurangan , pembagian dan bentuk pangkat !")
# print ("=" * 100)
# print ("PENGURANGAN")

# print (10 - 5)
# kursi_204 = 30
# kursi_308 = 20
# jumlah = kursi_204 - kursi_308 
# print ("jumlah kursi_204 - kursi_308 =", jumlah)

# print ("-" * 100)
# print ("PEMBAGIAN")

# print (10 / 5)
# kursi_204 = 30
# kursi_308 = 20
# jumlah = kursi_204 / kursi_308 
# print ("jumlah kursi_204 : kursi_308 =", jumlah)

# print ("-" * 100)
# print ("BENTUK PANGKAT")

# print (10 ** 5)
# kursi_204 = 30
# kursi_308 = 20
# jumlah = kursi_204 ** kursi_308 
# print ("jumlah kursi_204 ** kursi_308 =", jumlah)

# print ("=" * 100)
# print ("Latihan 2")
# print ("=" * 100)
# print ("-" * 100)
# print ("a. Tampilkan contoh variabel , print nama = Agus Pergi ke pasar")
# print ("-" * 100)
# nama= "Agus pergi kepasar"
# print (nama)

# print ("-" * 100)
# print ("b. Contoh tipe data")
# print ("-" * 100)
# #Integer
# nilai_integer = 25
# print("Nilai Integer:", nilai_integer)
# #Float
# nilai_float = 3.14
# print ("Nilai float:", nilai_float)
# ##String
# nilai_string = "Hello Word"
# print ("Nilai string:", nilai_string)


# #Tugas pendahuluan
# #Soal a
# #Contoh penggunaan aritmatika
# a = 5
# b = 2
# print ("a =", a)
# print ("b =", b)
# print ( "penjumlahan a + b =",a + b )
# print ("pengurangan a - b =", a - b)
# print ( "perkalian a * b =",a * b )
# print ( "pembagian a / b =",a / b )
# print ( "bilangan bulat dari a // b =",a // b )
# print ( "sisa bagi dari a % b =",a % b )
# print ( "pangkat a ** b =",a ** b )

# # Soal 6 TP: 
# # Seorang mahasiswa membeli 3 buah buku dengan harga masing-masing Rp45.000 dan b buah pulpen dengan harga masing-masing Rp7.500. Tulisakan kode untuk soal dibawah ini:
# # a. Buatlah variabel untuk menyimpan harga buku dan harga pulpen.
# # b. Gunakan operator aritmatika Python untuk menghitung total biaya yang harus dibayarkan.
# # c. Jika mahasiswa tersebut membayar dengan uang Rp200.000, gunakan operator aritmatika untuk menghitung jumlah uang kembaliannya.


# print ("=" * 100)
# print ("PriceList:")
# harga_buku = 45000
# harga_pulpen = 7500
# jumlah_buku = 3
# jumlah_pulpen = b
# total_biaya = (jumlah_buku * harga_buku ) + (jumlah_pulpen * harga_pulpen)
# print ("Buku:", harga_buku)
# print ("Pulpen", harga_pulpen) 
# print ("-" * 10, "Pembelian", "-" * 10)
# print ("Buku:", jumlah_buku, "x")
# print ("Pulpen:", jumlah_pulpen, "x") 
# print ("-" * 12, "Total", "-" * 12)
# print("Total Harga: ", total_biaya)
# uang_bayar = 200000
# kembalian = uang_bayar - total_biaya
# print ("Tunai:", uang_bayar) 
# print("Kembalian:", kembalian) 
# print ("-" * 31)


# print ("=" * 10,"Pertemuan 2 Modul 1","=" * 10)
# print ("-" * 100)
# print ("1. Hallim pergi ke sebuah toko alat tulis untuk membeli beberapa perlengkapan sekolah. Ia membeli 3 buah buku tulis dengan harga satuan Rp 5.000 dan 2 buah pensil dengan harga satuan Rp 4.500 selain itu, toko tersebut memberlakukan pajak pembelian sebesar 10% dari total harga barang. Lalu Hallim harus menghitung berapa uang yang harus ia bayar ke kasir setelah di tambahkan pajak. Buatlah program untuk menghitung total belanja setelah pajak ditetapkan!")
# print ("-" * 100)
# #Soal Nomer 1 (Statis)
# harga_buku = 5000
# harga_pensil= 4500
# jumlah_buku= 3
# jumlah_pensil= 2
# total1 = (harga_buku * jumlah_buku) + (harga_pensil * jumlah_pensil)
# total2_pajak = total1 * 0.10
# total3 = total1 + total2_pajak

# print("Total sebelum pajak  : Rp", total1)
# print("Pajak 10%            : Rp", int(total2_pajak))
# print("Total                : Rp", int(total3))


# print ("-" * 100)
# print ("2. Seorang siswa sedang belajar tentang bangun ruang. Ia diminta menghitung volume dan luas permukaan sebuah balok dengan ukuran: Panjang = 10cm Lebar = 6 cm Tinggi = 4 cm Buatlah program untuk membantu siswa tersebut menyelesaikan masalah tersebut! program tersebut bisa menerima input dari panjang, lebar, dan tinggi!")
# print ("-" * 100)
# # Soal No 2 (Dinamis)
# panjang = int(input("Masukkan panjang balok (cm): "))
# lebar   = int(input("Masukkan lebar balok (cm): "))
# tinggi  = int(input("Masukkan tinggi balok (cm): "))
# volume = panjang * lebar * tinggi
# luas_permukaan = 2 * ((panjang * lebar) + (panjang * tinggi) + (lebar * tinggi))
# print("=" * 10, "Hasil Perhitungan Balok","=" * 10)
# print("Volume Balok         =", volume, "cm")
# print("Luas Permukaan Balok =", luas_permukaan, "cm")


# print ("-" * 100)
# print ("3. Dalam sebuah kotak terdapat 8 bola merah dan 6 bola biru. Seorang anak akan mengambil 3 bola sekaligus secara acak. Buatlah program Python untuk menghitung berapa banyak kemungkinan kombinasi bola yang dapat diambil!")
# print ("-" * 100)
# # Soal No 3 (Dinamis)
# def kombinasi(total_bola, bola_yang_diambil):
#     perkalian_atas = 1
#     perkalian_bawah = 1
#     for hitungan in range(bola_yang_diambil):   
#         perkalian_atas *= (total_bola - hitungan)
#         perkalian_bawah *= (hitungan + 1)
#     return perkalian_atas // perkalian_bawah

# bola_merah = int(input("Jumlah bola merah: "))
# bola_biru = int(input("Jumlah bola biru: "))
# bola_diambil = int(input("Jumlah yang diambil sekaligus: "))
# total_bola = bola_merah + bola_biru
# hasil = kombinasi(total_bola, bola_diambil)
# print("=" * 10, "Hasil Perhitungan","=" * 10)
# print("Jumlah bola merah :", bola_merah)
# print("Jumlah bola biru  :", bola_biru)
# print("Total bola        :", total_bola)
# print("Diambil sekaligus :", bola_diambil)
# print("Kombinasi         :", hasil)



harga_buku = 45000
harga_pulpen =7500
jumlah_buku=3
jumlah_pulpen=2
total_biaya=(jumlah_buku*harga_buku)+(jumlah_pulpen*harga_pulpen)
print ("Total biaya:", total_biaya)
uang_bayar=200000
kembalian = uang_bayar-total_biaya
print ("Tunai:", uang_bayar)
print ("Kembalian:", kembalian)

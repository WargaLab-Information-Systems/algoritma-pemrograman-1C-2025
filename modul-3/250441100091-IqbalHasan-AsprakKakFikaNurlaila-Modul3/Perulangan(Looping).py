# # #Modul 3 - Perulangan (Looping)
# # #latihan 1
# # #membuat program for, while dan break 
# # #contoh 1
# # a=1
# # while a<=5:
# #     print(a)
# #     a+=1
# # ##contoh 2
# # ##menampilkan bilangan ganjil
# # a=1
# # while a<=10:
# #     a+=1
# #     if a%2==0:
# #         print ('%d bilangan ganjil'%a)
# #     else:
# #         continue
# # ##Contoh 3 
# # ##menampilkan angka dari 1 sampai 6 dengan menggunakan while:
# # a=1
# # while a<=10:
# #     print(a)
# #     a+=1
# #     if a==6:
# #         break
# # ##contoh 4
# # ##perintah while menampilkan output tanpa henti:
# # while 1:
# #     print("perulangan tiada batas, tekan Ctrl+C untuk berhenti")
# # ##contoh 5
# # bulan={1:'januari',2:'februari',3:'maret',4:'april',5:'mei'}
# # for a in bulan.values():
# #     print(a)


# # #Tugas Pendahuluan Modul 3
# # #No.2 Contoh For Loop
# # jumlah_genap = 0
# # for n in range(1, 11):
# #     if n % 2 == 0:
# #         jumlah_genap += 1
# # print("Banyak bilangan genap:", jumlah_genap)
# # #No.3 Contoh While Loop
# # jawab = ""
# # while jawab.lower() != "ya":
# #     jawab = input("Ketik 'ya' untuk lanjut: ")
# # print("Lanjut!")


# # #No.5 Program Kasir Apotek Fuad Farma
# # print("===== KASIR APOTEK FUAD FARMA =====")
# # total = 0
# # jumlah = 0
# # harga = float(input("Harga obat (0 untuk selesai): "))
# # while harga != 0:
# #     total += harga
# #     jumlah += 1
# #     harga = float(input("Masukkan harga obat (0 untuk selesai): "))
# # print("===== STRUK PEMBELIAN =====")
# # if jumlah > 0:
# #     rata = total / jumlah
# #     print(f"Jumlah obat yang dibeli : {jumlah} item")
# #     print(f"Total harga seluruh     : Rp {total:,.2f}")
# #     print(f"Rata-rata harga obat    : Rp {rata:,.2f}")
# # else:
# #     print("Tidak ada obat yang dibeli.")
# # print("===== TERIMA KASIH =====")









# # # Praktikum Modul 3

# # #contoh for
# # angka = 10 
# # for num in range (angka):
# #     print (num)

# # #contoh while
# # i = 0
# # while i < 6 :
# #     print (i)
# #     i +=1
# #     if i==3:
# #         break

# # #contoh menggunakan for untuk mengiterasi string
# # nama = "fika"
# # for kalimat in nama:
# #     print (kalimat)

# # ##contoh for angka genap dari 1 - 10
# # for i in range (1,11):
# #     if i % 2 == 0:
# #         print (i)
# # ##contoh for angka ganjil dari 1 - 10 

# # #contoh for angka genap dari 1 - 10 tanpa angka 0
# # angka = int(input("masukkan angka(1/2): ")) 

# # for i in range (angka):
# #     if i  % 2 == 0 and i !=0:
# #         print (i)

# # #contoh while true
# # while True:
# #     n = int(input("masukkan pilihan: "))

# #     if n == 1:
# #         print("halo")
# #         break
# #     elif n == 2:
# #         print("hai")
# #         break
# #     else:
# #         print("pilihan tidak valid")
# #         continue

# # ##contoh pass
# # for i in range (10):
# #     pass #tidak ada output


# # ##Challange praktikum:
# # print ("========= PILIHAN =========")
# # print ("1. nomor")
# # print ("2. keluar")
# # print ("3. gwe")
# # print ("masukkkan pilihan(1/2/3): ")
# # print ("nomer: 78")
# # print ("============================")


# # while True:
# #     n = int(input("masukkan pilihan(1/2/3): "))

# #     if n == 1:
# #         print("anda memilih nomor 1")
# #         break
# #     elif n == 2:
# #         print("anda memilih keluar")
# #         break
# #     elif n == 3:
# #         print("anda memilih gwe")
# #         break
# #     else:
# #         print("pilihan tidak valid")
# #         continue




































# #Tugas Praktikum Modul 3
# #Soal No.1
# print("------------------------------------------")
# print("SOAL 1: Dalam matematika, bilangan prima merupakan bilangan asli lebih besar dari 1 yang hanya memiliki dua faktor yaitu 1 dan bilangan itu sendiri. Buatkan program untuk menampilkan bilangan prima dari 1 sampai n.")
# print("------------------------------------------")

# n = int(input("Masukkan batas angka minimal 2: "))
# if n < 2:
#     print("Tidak ada bilangan prima di bawah 2.")
# else:
#     print("Bilangan prima dari 1 sampai", n, "adalah:") 
#     for i in range(2, n + 1):
#         prima = True
#         for j in range(2, i):
#             if i % j == 0:
#                 prima = False
#                 break
#         if prima:
#             print(i, end=" ")










# #Soal No.2
# print("------------------------------------------")
# print("SOAL 2: Buatlah simulasi sederhana dari mesin ATM yang meminta user untuk memasukkan PIN(XXYYY(X = 2 NIM awal, Y = 3 NIM terakhir)). User memiliki kesempatan 3 kali untuk measukkan PIN yang benar. Jika PIN benar, Tampilkan pesan “PIN benar, akses diterima”, jika salah, maka tampilkan pesan “PIN salah, coba lagi”. Jika sudah 3 kali salah, tampilkan pesan “Akses ditolak, kartu diblokir”. PIN harus diinput dalam bentuk angka dan harus 5 digit.")
# print("------------------------------------------")

# pb = "25091"
# dd= "Iqbal Hasan - 250441100091"
# kesempatan = 3
# for i in range(kesempatan):
#     pin = input("Masukkan PIN (5 digit): ")
#     if not pin.isdigit():
#         print("PIN harus berupa angka 5 digit!")
#         continue
#     if len(pin) != 5:
#         print("PIN harus 5 digit angka!")
#         continue
#     if pin == pb:
#         print("PIN benar!")
#         print("Selamat datang,",dd)
#         break
#     else:
#         print("PIN salah, coba lagi")
# else:
#     print("Akses ditolak, kartu diblokir")











# #Soal No.3
# print("-------------------------------------------")
# print("SOAL 3: Buatlah program yang meminta user untuk memasukkan sebuah kalimat. Lalu program akan menganilsa kalimat tersebut dan menampilkan :")
# print ("a. Jumlah huruf vokal dan konsonan")
# print ("b. Jumlah kata dalam kalimat")
# print("-------------------------------------------")

# kalimat = input("Masukkan sebuah kalimat: ").lower()
# vokal = "aiueo"
# jumlah_vokal = 0
# jumlah_konsonan = 0
# for huruf in kalimat:
#     if huruf.isalpha():
#         if huruf in vokal:
#             jumlah_vokal += 1
#         else:
#             jumlah_konsonan += 1
# kata = kalimat.split()
# jumlah_kata = 0
# for k in kata:
#     if any(h.isalpha() for h in k):
#         jumlah_kata += 1
# if jumlah_vokal == 0 and jumlah_konsonan == 0:
#     jumlah_kata = 0
#     print("Kalimat tidak mengandung huruf alfabet!")

# print("=== hasil analisa kalimat ===")
# print("Jumlah huruf vokal     :", jumlah_vokal)
# print("Jumlah huruf konsonan  :", jumlah_konsonan)
# print("Jumlah kata            :", jumlah_kata)














# #Soal No.4
# print("------------------------------------------")
# print("SOAL 4: Ambaki adalah seorang developer di sebuah IndoMei. Ambaki diminta untuk membuat program yang menampilkan struk pembelian setiap pelanggan. Program tersebut akan meminta input berupa nama pembeli, daftar barang yang dibeli, dan harga dari setiap barang. Setelah itu, program akan menampilkan struk pembelian yang berisi nama pembeli, daftar barang beserta harganya, total harga keseluruhan, serta pesan “Terima kasih telah berbelanja di IndoMei.” Program akan terus meminta input dari kasir untuk pelanggan berikutnya hingga kasir memasukkan (y/n) pada pertanyaan “Apakah ada pembeli berikutnya?”.")
# print("------------------------------------------\n")

# while True:
#     print("====================================")
#     print("       PROGRAM STRUK INDO MEI       ")
#     print("====================================")
#     nama = input("Masukkan nama pembeli: ")
#     total_harga = 0
#     daftar_barang = []
#     while True:
#         barang = input("Masukkan nama barang (tekan 'selesai' jika sudah): ")
#         if barang == "selesai":
#             break
#         while True:
#             harga = input("Masukkan harga barang: ")
#             if  not harga.isdigit():
#                 print("Harga harus berupa angka dan tidak boleh negatif!")
#                 continue
#             harga = int(harga)
#             break
#         daftar_barang.append((barang, harga))
#         total_harga += harga
#     print("========== STRUK PEMBELIAN ==========")
#     print("Nama Pembeli :", nama)
#     print("-------------------------------------")
#     print("Daftar Barang:")
#     for barang, harga in daftar_barang:
#         print(f"- {barang:<20} Rp{harga:>8}")
#     print("------------------------------------")
#     print(f"Total Harga  : Rp{total_harga}")
#     print("Terima kasih telah berbelanja di IndoMei.")
#     print("====================================\n")
#     lanjut = input("Apakah ada pembeli berikutnya? (y/n): ")
#     if lanjut.lower() == "n":
#         print("Program selesai.")
#         break

# total = 0
# jumlah = 0

# while True:
#     harga = float(input("Masukkan harga obat (0 untuk selesai): "))
#     if harga == 0:
#         break
#     total += harga
#     jumlah += 1

# if jumlah > 0:
#     rata = total / jumlah
#     print("Total harga seluruh obat:", total)
#     print("Jumlah obat yang dibeli:", jumlah)
#     print("Rata-rata harga obat:", rata)
# else:
#     print("Tidak ada obat yang dimasukkan.")


#for
# angka = 10
# for angka in range(angka):
#     print(angka)

#while
# i = 0
# while i < 6:
#     print(i)
#     i += 1
#     if i == 3:
#         break

# nama = "sultan"

# for kalimat in nama:
#     print(kalimat)


# angka = int(input("masukkan angka: "))

# for i in range (angka):
#     if i % 2 == 0 and i = 0:
#         print (i)


# while True:
#     n = int(input("masukkan pilihan: "))
    
#     if n == 1:
#         print("halo")
#         break
#     elif n == 2:
#         print("hai")
#         break
#     else:
#         print("pilihan tidak valid")
#         continue

# for i in range(10):
#     pass

# print("1. nomor")
# print("2. keluar")
# print("huuu")

# while True:
#     pilihan= input("masukkan pilihan: ")
#     if pilihan == "1":
#         print("memilih nomor 1")
#         break
#     elif pilihan =="2":
#         print("anda memilih keluar")
#         break
#     elif pilihan =="3":
#         print("huuu")
#         break
#     else :
#         print ("masukkan ulang pilihan")

#Soal Modul 3

#NO 1

# n = int(input("Masukkan batas bilangan: "))
# print("Bilangan prima dari 1 sampai", n, "adalah:")

# for i in range(2, n + 1):
#     prima = True
#     for j in range(2, i):
#         if i % j == 0:
#             prima = False
#             break
#     if prima:
#         print(i)

#NO 2

# pin_benar = 25001
# kesempatan = 3

# while kesempatan > 0:
#     pin_input = input("Masukkan PIN : ")
#     if (".") in pin_input:
#         kesempatan -= 1
#         print ("masukkan bilangan bulat!")
#         continue

#     if not pin_input.isdigit():
#         kesempatan -= 1
#         print(" Masukkan pin berupa angka!")
#         continue
#     if len(pin_input) != 5:
#         kesempatan -= 1
#         print(" PIN harus berjumlah 5 digit!")
#         continue
    
#     pin = int(pin_input)
    
#     if pin == pin_benar:
#         print(" PIN benar, akses diterima")
#         break

#     else:
#         kesempatan -= 1
#         if kesempatan > 0:
#             print(" PIN salah!coba lagi:")
#         else:
#             print(" Akses ditolak, kartu diblokir.")
    
# if kesempatan > 0:
#     pass
# else:
#     print(" Akses ditolak, kartu diblokir.")


#NO 3

# kalimat = input("Masukkan kalimat: ").lower()
# vokal = "aiueo"
# jumlah_vokal = 0
# jumlah_konsonan = 0

# for huruf in kalimat:
#     if huruf.isalpha():
#         if huruf in vokal:
#             jumlah_vokal += 1
#         else:
#             jumlah_konsonan += 1

# jumlah_kata = len(kalimat.split())

# print("Jumlah huruf vokal:", jumlah_vokal)
# print("Jumlah huruf konsonan:", jumlah_konsonan)
# print("Jumlah kata:", jumlah_kata)


#NO 4

# while True:
#     nama = input("Nama pembeli: ")
#     total = 0
#     nb =""
#     while True:
#         barang = input("Nama barang: ")
#         harga = int(input("Harga barang: "))
#         jumlah = int(input("Jumlah barang: "))
#         total += harga * jumlah
#         nb += f"{barang:8} Rp. {harga}\n"
#         lagi = input("Tambah barang lain? (ya/tidak): ").lower()
#         if lagi != "ya":
#             break

#     print("\n===== STRUK PEMBELIAN =====")
#     print(nb)
#     print("Total belanja: Rp", total)
#     print("Terima kasih telah berbelanja di IndoMei!\n")

#     lanjut = input("Apakah ada pembeli berikutnya? (ya/tidak): ").lower()
#     if lanjut != "ya":
#         print("Program selesai.")
#         break

# # Dasar Teori

# #Perulangan bersarang (nested loop)
# # Loop luar (outer loop)
# for i in range(1, 4): #loop  ini akan berjalan 3 kali ( i = 1 2 3)
#     print(f"Loop luar i = {i}")

#     #Loop dalam (inner loop)
#     for j in range(1, 4): #loop ini juga akan berjalan 3 kali untuk setiap iterasi dari loop luar
#         print(f"loop dalam j = {j}")


# #Struktur Pengulangan dan Kombinasi
# a = 24
# b = 36

# while b != 0 :
#     a, b = b, a % b
#     print (f"FPB-nya adalah : {a}")


# # #Pola Matematika dalam Perulangan
# n=100 #batas angka
# a, b = 0, 1

# print("Bilangan Fibonacci hingga", n)
# while a <= n:
#     print(a, end=" ")
#     a, b= b, a + b


# # #Pola Grafis dalam Perulangan
# n = 5
# for i in range(1, n+1):

#     for j in range(n-i):
#         print(' ', end=' ')
#     for k in range(1, i+1):
#         print(k, end=' ')
#     print()


# #contoh tp no 2
# for i in range(1, 4):
#     for j in range(1, 4):
#         print(j, end=" ")
#     print()

# #contoh tp no 5
# a, b = 0, 1
# while a <= 100:
#     print(a, end=" ")
#     a, b = b, a + b


# ###contoh tp no 6
# n = int(input("Masukkan jumlah baris: "))
# for i in range(1, n+1):
#     for j in range(n-i):
#         print(" ", end="")
#     for k in range(1, i+1):
#         print(k, end=" ")
#     print()



































# # #Tugas praktikum no 1
# print("--------------------- TUGAS NO 1 ---------------------")
# print("SOAL : Mas rusdi kini mengawasi beberapa baris lampu di taman kota, dan setiap baris memiliki jumlah lampu yang berbeda. Untuk membantu temannya, mas narji ingin membuat program Python yang dapat menampilkan kondisi setiap lampu. Program harus meminta input jumlah baris lampu, lalu jumlah lampu di setiap baris. Setiap lampu diberi nomor urut, dan program menampilkan pesan “Lampu ke-[x] pada baris [y] menyala.” Jika nomor lampu merupakan kelipatan 3, tampilkan “Lampu ke-[x] pada baris [y] rusak.” Selain itu, jika baris lampu adalah baris terakhir, tambahkan pesan “Periksa sambungan daya utama.” Program ini membantu mas rusdi dan temannya mengetahui kondisi setiap lampu dengan cepat dan efisien tanpa harus memeriksa secara manual satu per satu.")
# print("------------------------------------------------------")

# while True:
#     baris_input = input("Masukkan jumlah baris lampu: ")
#     if baris_input.isdigit():
#         baris = int(baris_input)
#         if baris < 1:
#             print("Jumlah baris harus lebih dari 0!")
#         else:
#             break
#     else:
#         print("Input tidak valid! Masukkan angka positif.")

# blamp = 1
# i = 1

# while i <= baris:
#     while True:
#         lampu_input = input("Masukkan jumlah lampu pada baris ke-" + str(i) + ": ")
#         if lampu_input.isdigit():
#             jlampu = int(lampu_input)
#             if jlampu < 1:
#                 print("Jumlah lampu harus lebih dari 0!")
#             else:
#                 break
#         else:
#             print("Input tidak valid! Masukkan angka saja.")

#     for j in range(jlampu):
#         if blamp % 3 == 0:
#             print("Lampu ke-", blamp, "pada baris", i, "rusak.")
#         else:
#             print("Lampu ke-", blamp, "pada baris", i, "menyala.")
#         blamp += 1

#     if i == baris:
#         print("Periksa sambungan daya utama.")
#     i += 1


# # Tugas praktikum no 2
# print("--------------------- TUGAS NO 2 ---------------------")
# print("SOAL : Pak Wowo bekerja di perusahaan besar dengan dua shift, pagi dan malam. Program menghitung total gaji mingguan dengan memperhitungkan lembur dan bonus shift malam.")
# print("------------------------------------------------------") 

# total_gaji = 0
# total_jam_lembur = 0
# total_bonus_shift = 0
# hari = 1

# while hari <= 7:
#     print("Hari ke-", hari)
#     gaji_harian = 100000

#     while True:
#         jam_input = input("Masukkan jumlah jam lembur: ")
#         if jam_input.isdigit(): 
#             jam_lembur = int(jam_input)
#             if jam_lembur < 0:
#                 print("Jam lembur tidak boleh negatif!")
#             else:
#                 break
#         else:
#             print("Input tidak valid! Masukkan angka saja.")

#     while True:
#         shift = input("Apakah shift malam? (y/n): ").lower()
#         if shift in ["y", "n"]:
#             break
#         else:
#             print("Input tidak valid! Masukkan 'y' atau 'n'.")

#     if 1 <= jam_lembur <= 3:
#         gaji_harian += jam_lembur * 25000
#         total_jam_lembur += jam_lembur
#     elif jam_lembur == 4:
#         gaji_harian += 100000
#         total_jam_lembur += 4
#     elif jam_lembur == 6:
#         gaji_harian += 200000
#         total_jam_lembur += 6
#     elif jam_lembur == 8:
#         gaji_harian += 300000
#         total_jam_lembur += 8
#     elif jam_lembur > 8:
#         print("Lembur lebih dari 8 jam tidak dihitung.")

#     if shift == "y":
#         gaji_harian += 50000
#         total_bonus_shift += 50000

#     print("Gaji hari ini: Rp", gaji_harian)
#     total_gaji += gaji_harian

#     hari += 1

# print("---------------------------------")
# print("Total jam lembur minggu ini:", total_jam_lembur)
# print("Total bonus shift malam minggu ini: Rp", total_bonus_shift)
# print("Total gaji Pak Wowo selama seminggu: Rp", total_gaji)



# #Tugas praktikum no 3
# print("--------------------- TUGAS NO 3 ---------------------")
# print("SOAL : bjirka senang membuat pola angka untuk menenangkan pikirannya. Kali ini, ia ingin membuat dua piramida angka yang saling berhadapan seperti cermin. Jika pengguna memasukkan angka n = 5. Program harus menggunakan tiga perulangan bersarang (nested loop) — satu untuk sisi kiri piramida, satu untuk ruang kosong di tengah, dan satu untuk sisi kanan piramida. Gunakan logika agar jumlah angka dan spasi berubah sesuai barisnya sehingga pola tetap simetris untuk nilai n berapa pun.")
# print("------------------------------------------------------")


# n = int(input("Masukkan tinggi piramida: "))

# while n <= 0:
#     print("Tidak Valid!")
#     n = int(input("Masukkan tinggi piramida: "))

# for i in range(n, 0, -1):
#     # 1 - i (naik)
#     for kiri in range(1, i + 1):
#         print(format(kiri, '2d'), end='')

#     # spasi tengah
#     for tengah in range(2 * (n - i)):
#         print('  ', end='')

#     # i ke 1 (turun)
#     for kanan in range(i, 0, -1):
#         print(format(kanan, '2d'), end='')
#     print()
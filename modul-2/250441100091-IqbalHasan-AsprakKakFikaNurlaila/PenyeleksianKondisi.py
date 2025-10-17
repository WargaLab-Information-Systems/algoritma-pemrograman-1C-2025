##Note: Jalankan kode satu persatu
## Modul 2 Pendahuluan
## Penyeleksian Kondisi

# #Program perintah if
# nama = "python"
# if nama == "python":
#     print ("Hallo " + nama)
    
# #Perintah if-else
# Kunci = "python"
# password = input("Masukkan password: ")
# if password == Kunci :
#     print ("Paword Benar")
# else :
#     print ("Password Salah")

# #Program Perinta if-elif-else
# angka = int(input("Masukkan sebuah bilangan: "))
# if angka > 0:
#     print ("Angka merupakan Bilangan Positif")
# elif angka < 0:
#     print ("Angka merupakan Bilangan Negatif")
# else:
#     print ("Angka merupakan 0")

# #Program if Bersarang
# x = int(input("Masukkan nilai x="))
# y = int(input("Masukkan nilai y="))
# if x == y:
#     print("nilai", x, "dan ", y, "mempunyai nilai yang sama")
# else :
#     if x > y:
#         print(x, "lebih besar dari ", y)
#     if x < y:
#         print(x, "lebih kecil dari ", y)




# # Latihan 1
# print ("=" * 10, "Latihan 1", "=" * 10)   
# print ("-" * 30)
# print ("1. Di bawah ini adalah contoh program Penyeleksian kondisi pada Bahasa pemrograman Python")
# print ("-" * 30)

# nomor_acak = 7
# print('Tebak nomor acak antara 1-10')
# tebakan = int(input('Masukkan tebakan Anda (bil bulat): '))
# if tebakan == nomor_acak:
#     print('Selamat! tebakan Anda benar')
#     print('tapi tidak ada hadiah untuk anda :(')
# elif tebakan < nomor_acak:
#     print('Tebakan Anda terlalu kecil')
# else:
#     print('Tebakan Anda terlalu besar')
# print('selesai')

## 2. contoh program penyeleksian kondisi
# a = int(input("Masukkan umur: "))
# if a <= 15:
#     print("Muda")
# elif a <= 20:
#     print("Remaja")
# else:
#     print("Tua")

# # 3. Menentukan Ganjil Genap
# #genjil genap
# nilai = int(input("Masukkan angka: "))
# if nilai % 2:
#     print("Bilangan Ganjil")
# else:
#     print("Bilangan Genap")

# ##Latihan 2
# ##Buatlah program jika andi memasukan nilai 1 sampai 9 , maka outputnya “angka anda satu “ –“angka anda Sembilan “ menggunakan operasi if elif dan else

# #buatlah program j
# #angka ke kata
# a = int(input("Masukkan angka (0-9): "))
# if a == 0:
#     print("angka anda nol")
# elif a == 1:
#     print("angka anda satu")
# elif a == 2:
#     print("angka anda dua")
# elif a == 3:
#     print("angka anda tiga")
# elif a == 4:
#     print("angka anda empat")
# elif a == 5:
#     print("angka anda lima")
# elif a == 6:
#     print("angka anda enam")
# elif a == 7:
#     print("angka anda tujuh")
# elif a == 8:
#     print("angka anda delapan")
# elif a == 9:
#     print("angka anda sembilan")
# else:
#     print("angka anda not found")


##Tugas Pendahuluan Modul 2
##Nomor 2  
# #Apa perbedaan antara if, if-else, if-elif-else, dan if bersarang? Jelaskan dengan Bahasa kalian sendiri dan berikan contoh kodenya!
# # contoh if
# nilai = 80
# if nilai > 75:
#     print("Lulus")

# # contoh if-else
# nilai = 60
# if nilai >= 75:
#     print("Lulus")
# else:
#     print("Tidak Lulus")

# ## contoh if-elif-else
# nilai = 85
# if nilai >= 90:
#     print("A")
# elif nilai >= 75:
#     print("B")
# elif nilai >= 60:
#     print("C")
# else:
#     print("D")

# ## contoh if bersarang
# uang = 15000
# if uang > 5000:
#     if uang >= 10000:
#         print("nasi ayam")
#     else:
#         print("nasi bebek")
# else:
#     print("Uang tidak cukup")

#Nomor 5
#5. Buatlah Program dengan Studi Kasus Berikut :
#Sebuah jalan tol memberikan ketentuan pembayaran sebagai berikut: Tarif
#dasar tol berbeda sesuai jenis kendaraan:
#• Mobil pribadi → Rp15.000
#• Truk kecil → Rp25.000
#• Truk besar → Rp40.000
#Diskon tarif tol berlaku jika:
#• Jika pembayaran menggunakan e-money → diskon 10%
#• Jika pembayaran menggunakan e-money dan dilakukan pada jam sepi
#(23.00 – 05.00) → diskon 20%
#• Jika pembayaran tunai → tidak ada diskon

# # Program Hitung Tarif Tol
# kendaraan = input("Masukkan jenis kendaraan:").lower()
# pembayaran = input("Masukkan metode pembayaran:").lower()
# jam = int(input("Masukkan jam transaksi:"))

# # Tentukan tarif awal
# if kendaraan == "mobil pribadi":
#     tarif = 15000
# elif kendaraan == "truk kecil":
#     tarif = 25000
# elif kendaraan == "truk besar":
#     tarif = 40000
# else:
#     print("Jenis kendaraan tidak dikenali")
#     tarif = 0

# # Tentukan diskon
# if pembayaran == "tunai":
#     potongan = 0
# elif pembayaran == "e-money":
#     if jam >= 23 or jam < 5:
#         potongan = 0.20
#     else:
#         potongan = 0.10
# else:
#     print("metode pembayaran tidak dikenali")
#     potongan = 0

# # Hitung hasil akhir
# if tarif > 0:
#     bayar = tarif - (tarif * potongan)
#     print("Total tarif: Rp", int(bayar))





# # #percobaan praktikum
# #penyeleksian kondisi
# hewan1 = "kucing"
# hewan2 = "ayam"
# hewan3 = "kambing"
# pilih = int(input("Masukkan inputan: "))
# if pilih == 1:
#     print(hewan1)
#     makan = input("Makan apa kucingnya? ")
#     if makan == "rumput":
#         print("Salah")
#     elif makan == "ikan":
#         print("Benar")        
# elif pilih == 2:
#     print(hewan2)
# elif pilih == 3:
#     print(hewan3)
# else:
#     print("Hanya ada 3 pilihan") 


# angka1 = 10
# if angka1 >=11:
#     print("salah")
# elif angka1 < 11:
#     print("benar")
# elif angka1 <= 11:
#     print("salah")

# if angka1 < = 11:
#     print("pertengahan")   

# #sistem pendaftaran
# print("1. Daftar")
# print("2. Keluar")
# pilihan = int(input("Masukkan pilihan: "))
# if pilihan == 1:
#    nama = input("Masukkan nama: ")
# else:
#     print("Keluar")

# #operator logika
# angka1 = 10
# angka2 = 20
# if angka1 > 5 and angka2 >= 15:
#     print("benar")
# elif angka1 > 5 or angka2 < 15:
#     print("salah")












# # # Tugas Praktikum Modul 2
# # Soal No. 1
# Note: batasannya 0 - 100
print("masukkan nilai")
nilai = int(input())
if nilai > 100:
    print("Invalid!")
else:
    if nilai >= 85:
        print("A")
        print("masukkan kehadiran")
        kehadiran = int(input())
        if kehadiran >= 90:
            print("kelulusan:lulus dengan pujian")
    else:
        if nilai >= 70:
            print("B")
        else:
            if nilai >= 60:
                print("C")
            else:
                if nilai >= 50:
                    print("D")
                else:
                    if nilai < 0:
                        print("Invalid!")
                    else:
                        print("E")


# # Soal No. 2
usia = int(input("Masukkan usia: "))
pelajar = input("Apakah pelajar SMA dengan kartu pelajar? (ya/tidak): ")
hari = input("Hari: ")
harga = 50000
hari = hari.lower()
pelajar = pelajar.lower()
hari_selasa = (hari == "selasa")
pelajar_sma = (pelajar == "ya")
diskon = 0
if usia < 12:
    diskon = 0.5
elif pelajar_sma:
    diskon = 0.3
elif hari_selasa:
    diskon = 0.2
total = harga * (1 - diskon)
print("Diskon diterapkan:", int(diskon * 100), "%")
print("Total yang harus dibayar: Rp", int(total))

# ## Soal No. 3
lama = float(input("Masukkan lama parkir (jam): "))
vip = input("Apakah member VIP? (ya/tidak): ").lower()
biaya = 0
if vip == "ya":
    biaya = 0
else:
    if lama <= 24:
        jam = int(lama)
        if lama > jam:
            jam += 1
        if jam <= 2:
            biaya = 5000
        else:
            biaya = 5000 + (jam - 2) * 3000
        if biaya > 20000:
            biaya = 20000
    else:
        biaya = 20000 
        sisa_jam = lama - 24
        jam_tambahan = int(sisa_jam)
        if sisa_jam > jam_tambahan:
            jam_tambahan += 1
        biaya += jam_tambahan * 3000
print("Total biaya parkir: Rp", int(biaya))



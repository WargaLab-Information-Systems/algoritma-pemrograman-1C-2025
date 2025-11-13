# #program perintah if
# nama =  "python"
# if nama == "python":
#     print ("halo" + nama)

# #if else
# kunci = "python"
# password = input ("masukkan password : ")
# if password == kunci :
#     print("password benar")
# else :
#     print("password salah")

# #if elif else
# angka = int (input("masukkan sebuah bilangan : "))
# if angka > 0:
#     print ("angka merupakab bilangan positif")
# elif angka <0:
#     print("bilangan negatif")
# else:
#     print ("angka merupakan 0")

# #if bersarang
# x = int(input("masukkan nilai x="))
# y = int(input("masukkan nilai y"))
# if x == y:
#     print("nilai", x, "dan", y, "mempunyai nilai yang sama")
# else:
#     if x> y :
#         print (x, "lebih besar daripada", y)
#     if x< y:
#         print (x, "lebih kecil dari", y)


#Soal modul No 2

# harga = 50000
# usia = int(input("masukkan usia : "))
# pelajar = input("apakah pelajar sma (ya/tidak) : ").lower()
# hari = input("masukkan hari : ").lower()

# diskon = 0

# if usia <12:
#     diskon = 0.5
# elif pelajar == "ya":
#     diskon = 0.3
# elif hari == "selasa":
#     diskon = 0.2

# harga_bayar = harga - (harga * diskon)
# print(f"total yang harus dibayar : Rp.{harga_bayar :}")

#soal modul No 3

jam = int(input("masukkan lama parkir (berapa jam?) : "))
vip = input("apakah anda vip? (ya/tidak) : ").lower()

if vip == "ya":
    biaya = 0
else:
    if jam <= 2:
        biaya = 5000
    else:
        biaya = 5000 + (jam - 2) * 3000
        if biaya >20000:
            biaya = 20000

print(f"total biaya parkir : Rp{biaya:}")
usia = int(input("Masukkan usia: "))
pelajar = input("Apakah Anda pelajar SMA (y/t)? ")
hari = input("Masukkan hari : ")
harga_normal = 50000

if usia <= 1 :
    diskon = 100
elif usia <= 12 :
    diskon = 50
elif pelajar == "y" :
    diskon = 30
elif hari == "selasa":
    diskon = 20
else :
    diskon = 0
    print("Data yang dimasukkan Tidak Valid!")
    
harga_bayar = harga_normal - (harga_normal * diskon / 100)

print("\nDiskon yang didapat:", diskon, "%")
print("Harga tiket yang harus dibayar: Rp", int(harga_bayar))
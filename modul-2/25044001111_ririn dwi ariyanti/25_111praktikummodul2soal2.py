harga_normal = 50000

umur = int(input("masukkan umur: "))
pelajar = input("Apakah pelajar SMA dengan kartu pelajar? (ya/tidak): ")
hari = input("Hari apakah kamu kesana?: ")

if umur < 12:
    diskon = 50
elif pelajar == "ya" :
    diskon = 30
elif hari == "selasa":
    diskon = 20
else :
    diskon = 0
    
harga_bayar = harga_normal - (harga_normal * diskon/ 100)

print("diskon", diskon, "%")
print("harga tiket yang harus dibayar adalah : Rp", int(harga_bayar))
 
    


    
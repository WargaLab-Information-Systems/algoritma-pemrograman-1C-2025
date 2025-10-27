motormatic = 50000
motortrail = 100000
motorsport = 75000
asuransi = 15000
hari = 3
diskon = 0.10
diskonkupon = 0.5
kupon = "AconkGG"

kendaraan = input("Masukkan jenis kendaraan : ")
sewa = int(input("Masukkan lama sewa : "))

if sewa >= hari :
    kendaraan == "motor matic"  
    jml1 = motormatic - asuransi
    print(f"Mendapat asuransi : {jml1}")
    total = diskon * jml1
    print(f"Total : {total}")
elif sewa >= hari :
    kendaraan == "motor trail"
    jml2 = motortrail - asuransi
    subtotal = diskon * jml2
    print(f"Mendapat asuransi : {jml2}")
elif sewa >= hari :
    kendaraan == "motor sport"
    jml3 = motorsport - asuransi
    subtotal = diskon * jml3
    print(f"Mendapat asuransi : {jml3}")
else :
    print("Tidak ada asuransi!")
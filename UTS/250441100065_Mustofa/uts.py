print("=== RENTAL MOTOR ACONK===")

print("1.Motor Matic = Rp. 50.000.00")
print("2.Motor Trail = Rp. 100.000.00")
print("3.Motor Sport = Rp. 75.000.00")
jenismotor = int(input("pilih jenis motor yang ingin disewa(1/2/3): "))

if jenismotor == 1:
    print("Motor Matic = Rp. 50.000.00")
    sewa = int(input("masukkan jumlah hari sewa: "))
    totalsewa = sewa * 50000
    print(totalsewa)
elif jenismotor == 2:
    print("Motor Trail = Rp. 100.000.00")
    sewa = int(input("masukkan jumlah hari sewa: "))
    totalsewa = sewa * 100000
    print(totalsewa)
elif jenismotor == 3:
    print("Motor Sport = Rp. 75.000.00")
    sewa = int(input("masukkan jumlah hari sewa: "))
    totalsewa = sewa * 75000
    print(totalsewa)
else:
    print("motor tidak tersedia")

kupon =input("masukkan kode kupon :")
if totalsewa > 150000:
   diskon:0.10
elif kupon == "AconkGG":
  diskon: 0.5
else:
   print("kupon tidak valid")


# while True:
#   if sewa > 3:
#       asuransi = totalsewa - 15000
# else:



 





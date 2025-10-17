total=0
batasan=0
totaljam=0
vip=3

jam=int(input("Input jam = "))

if jam > 0 and jam  <= 2:
    total=5000
    totaljam=jam
elif jam>2:
    totaljam=jam
    jam=jam-2
    total=(jam*3000)+5000
else:
     total=-1
     totaljam=str("tidakvalid")
     vip=8
if total>20000:
    total=20000
elif total>=0:
    total=total
elif total<0:
    total=str("tidak valid")

if vip==3:
    vip=str(input("Apakah tamu VIP? Y/N = "))
if vip=="Y" or vip=="y":
    total=0
    print(" Tamu VIP")
    vip=bool(True)
elif vip=="N" or vip=="n":
    print("bukan tamu VIP")
    vip=bool(False)
else:
    vip=str("Tidak valid")


print("Total pembayaran = ",total)
print(f"Total waktu parkir ={totaljam}")
print("Anggota vip = ",vip)
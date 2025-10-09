tiket=50000
usia=int(input("Input usia = "))
totalharga=0

if (usia < 12):
    usia=bool(True)
else:
    usia=bool(False)

v_pelajar=str(input("Apakah pelajar SMA ? Y/N? = "))

if v_pelajar=="y" or v_pelajar=="Y":
    v_pelajar=bool(True)
else:
    v_pelajar=bool(False)


v_hari=str(input("penonton hari selasa ? Y/N = "))

if v_hari=="y" or v_hari=="Y":
    v_hari=bool(True)
else:
    v_hari=bool(False)

print("usia di bawah 12 tahun = ",usia)
print("Pelajar SMA = ",v_pelajar)
print("Penonton hari selasa = ",v_hari)

if usia==True:
    totalharga=tiket-25000
elif usia==False and v_pelajar==True and (v_hari==False or v_hari==True):
    totalharga=tiket-15000
elif usia==False and v_pelajar==False and v_hari==True:
    totalharga=tiket-10000
else:
    totalharga=tiket
    print(" dan tidak mendapat diskon ")


    
print("totalharga harga = ",totalharga)
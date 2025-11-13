total_lembur=0
total_jam_lembur=0
bonusmalam=0
gaji_pokok_total=0
lembur=100

for hari in range (1,8):
    gaji_pokok_total=gaji_pokok_total+100000
    lembur=100
    shift=str("m")
    print(f"hari ke [{hari}] ",end="")
    while  lembur!=0 or lembur !=1 or lembur !=2 or lembur !=3 or lembur !=4 or lembur !=6  or lembur!=5 or lembur!=7 or lembur!=8:
        lembur=int(input("input jam lembur = "))
        if lembur==0:
            print("tidak lembur hari ini")
            break
        elif lembur==1:
            total_lembur=total_lembur+25000
            total_jam_lembur+=lembur
            break
        elif lembur==2:
            total_lembur=total_lembur+50000
            total_jam_lembur+=lembur
            break
        elif lembur==3:
            total_lembur=total_lembur+75000
            print(total_lembur)
            total_jam_lembur+=lembur
            break
        elif lembur==4:
            total_lembur=total_lembur+100000
            total_jam_lembur+=lembur
            break
        elif lembur==5:
            total_lembur=total_lembur+125000
            total_jam_lembur+=lembur
            break
        elif lembur==6:
            total_lembur=total_lembur+200000
            total_jam_lembur+=lembur
            break
        elif lembur==7:
            total_lembur=total_lembur+225000
            total_jam_lembur+=lembur
            break
        elif lembur==8:
            total_lembur=total_lembur+300000
            total_jam_lembur+=lembur
            break
        elif lembur>8:
            print("lembur tidak di hitung")
            break
        else:
            print("tidak valid")

    while shift !="y" or shift !="Y" or shift!="N" or shift!="n":
        shift=str(input("apakah mengikuti shift malam ? Y = iya N = tidak = "))
        if shift =="y" or shift =="Y":
            print("mengikuti shift malam")
            bonusmalam=bonusmalam+50000
            break
        elif shift == "N" or shift == "n":
            print(" tidak mengikuti shift malam")
            break
        else:
            print("tidak valid")

print(f"total jam lembur [{total_jam_lembur} jam ] dan hasil nya Rp [{total_lembur}]")
print(f"total bonus shift malam [Rp. {bonusmalam}] ")
print(f"total jadi pokok 1 minggu [Rp. {gaji_pokok_total}]")
print(f"total pembayaran gaji = Rp. {total_lembur+bonusmalam+gaji_pokok_total}")


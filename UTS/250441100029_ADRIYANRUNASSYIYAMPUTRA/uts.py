matic = 50000 
trail = 100000
sport=75000
total=0
lanjut=True
while lanjut== True:
    hari_sewa= int(input("input berapa hari sewa/0= tidak ada"))
    hari_sewa_mutlak=hari_sewa
    type_motor=str(input("'matic / trail / sport"))
    if type_motor=="matic":
        "total=matic"
    elif type_motor=="trail":
        total=trail
    elif type_motor=="sport":
        total=sport
    else:
        pass

    if hari_sewa>3:
        asuransi=15000*(hari_sewa-3)
        total=total+asuransi+15000
    if total>150000:
        diskon=(total*10)//100
        total=total-diskon
    while True:
        kupon=str(input("input kupon / n = tidak ada kupon"))
        if kupon=="n" or kupon=="N":
            print("tidak dapat diskon")
            print("kendaraan yang di sewa = ",type_motor)
            print("total yang harus di bayar = ",total)
            print("total hari sewa = ",hari_sewa_mutlak)
            print("apakah ingin melakukan sewa lagi? y = ulang dan n= berhenti ")
            lanjut=str(input("lanjut menyewa lagi = y / berhenti =n"))
            if lanjut=="n" or lanjut=="N":
                lanjut=False
                break
            else:
                lanjut=True
                break
        if kupon=="AconkGG":
            diskonkupon=(total*5)//100
            total=total-diskonkupon
            print("kendaraan yang di sewa = ",type_motor)
            print("total yang harus di bayar = ",total)
            print("total hari sewa = ",hari_sewa_mutlak)
            print("apakah ingin melakukan sewa lagi? y = ulang dan n= berhenti ")
            lanjut=str(input("lanjut menyewa lagi = y / berhenti =n"))
            if lanjut=="n" or lanjut=="N":
                lanjut=False
                break
            else:
                lanjut=True
                break
        else:
            print("kupon salah, input lagi")
        
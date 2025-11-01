matic = 50000
trail =100000
sport = 75000
asuransi = 15000
disksubtot = 10/100
diskkupon = 5/100

while True:
    print("tersedia: 1.motor matic, 2.motor trail, 3.motor sport")
    sewa = int(input("anda ingin sewa motor apa (pilih sesuai nomor): "))
    if sewa == 1 :
        print("harga motor matic Rp.50000")
        hari = int(input("berapa hari anda sewa: "))
        if hari <= 3 :
            print("tidak ada asuransi, harga sewa Rp.50000")
            kupon = str(input("masukkan kode kupon"))
            if kupon == "AconkGG" :
                print("kupon benar, anda mendapat diskon 5%")
                totmatic = matic * diskkupon
                print ("harga sewa motor matic menjadi: ",totmatic)
            else:
                print("kupon salah tidak ada diskon tambahan")
            break
        elif hari > 3 :
            print("asuransi Rp.15000")
            totmatic = matic + asuransi
            print("harga sewa motor matic menjadi: ",totmatic)
            kupon = str(input("masukkan kode kupon"))
            if kupon == "AconkGG" :
                print("kupon benar, anda mendapat diskon 5%")
                totmatic = totmatic * diskkupon
                print ("harga sewa motor matic menjadi: ",totmatic)
                if totmatic > 150000 :
                    print("anda mendapat diskon 10%")
                    totmatic = totmatic * disksubtot
                    print("harga sewa motor matic menjadi: ",totmatic)

    if sewa == 2 :
        print("harga motor trail Rp.100000")
        hari = int(input("berapa hari anda sewa: "))
        if hari <= 3 :
            print("tidak ada asuransi, harga sewa Rp.100000")
            kupon = str(input("masukkan kode kupon"))
            if kupon == "AconkGG" :
                print("kupon benar, anda mendapat diskon 5%")
                tottrail = trail * diskkupon
                print ("harga sewa motor matic menjadi: ",totmatic)
                if totmatic > 150000 :
                    print("anda mendapat diskon 10%")
                    totmatic = totmatic * disksubtot
                    print("harga sewa motor matic menjadi: ",totmatic)
                    break
    
    if sewa == 3 :
        print("harga motor sport Rp.75000")
        hari = int(input("berapa hari anda sewa: "))
        if hari <= 3 :
            print("tidak ada asuransi, harga sewa Rp.75.000")
            kupon = str(input("masukkan kode kupon"))
            if kupon == "AconkGG" :
                print("kupon benar, anda mendapat diskon 5%")
                totmatic = trail * diskkupon
                print ("harga sewa motor matic menjadi: ",totmatic)
                if totmatic > 150000 :
                    print("anda mendapat diskon 10%")
                    totmatic = totmatic * disksubtot
                    print("harga sewa motor matic menjadi: ",totmatic)
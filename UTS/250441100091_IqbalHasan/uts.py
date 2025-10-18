##Program Rental Motor 

##pm=pilihan motor
##hp=harga perhari
##jk=jenis kendaraan


while True:
    print("--- Rental Motor Aconk ---")
    print ("-List kendaraan-")
    print ("1. Motor Matic = Rp. 50.000.00.") 
    print ("2. Motor Trail = 100.000.00")
    print ("3. Motor Sport = 75.000.00. ")
    print ("-------------------------------")
    
    pm = int(input("Masukkan pilihan angka 1,2,3:"))
    while True:
        if pm <1 or pm >3:
            print("Pilihan tidak valid!")
            pm = int(input("Masukkan pilihan angka 1,2,3:"))
            break
        while True:
            if pm == 1:
             hp= 50000
             jk = "Motor Matic"
            elif pm == 2:
                hp = 100000
                jk = "Motor Trail"
            elif pm == 3:
                hp = 75000
                jk = "Motor Sport"
                sewa = int(input("Waktu penyewaan(Hari):"))
                if sewa >3:
                    asuransi=15000
                else:
                    asuransi=0
                    break
                subtotal= hp+sewa
                if subtotal > 150000:
                    dk10= subtotal * 0.10
                else:
                    dk10=0

                total=dk10 
                dkk=input("Masukkan Kode Kupon (Jika ada): ")
                if dkk == "AconkGG":
                    potongan=subtotal + (dk10*dkk)
                else:
                    potongan=0
                ##Total

                print ("Total",subtotal)
                print ("")
                print ("")
                print ("")





    lanjut=input("Masukkan Y untuk lanjut dan N untuk Stop:")
    if lanjut.lower == "y":
        break
print("Program Selesai, Terima Kasih")
while True:
    print("1.jenis motor matic harga 500000")
    print("2.jenis motor trail harga 10000000")
    print("3.jenis motor sport harga 7500000")
    
    nama = input("masukkan nama penyewa: ")
    jenis = input("pilih jenis motor (1, 2, 3):")
    lama = input("lama sewa motor (jam):")
    kupon = input("apakah kamu punya kupon? (y/n)")
    
    
    
    if jenis == 1:
        print("motor matic")
    elif jenis == 2:
        print("motor trail")
    elif jenis == 3:
        print("motor sport")
    else:
        print("pilihan motor tidak valid")
        continue
    
    
    if lama >= 3:
        asuransi = 1500000
    else:
        asuransi = 0
    
    
    if diskon >= 15000000:
        subtotal = diskon * 0.10
    else:
        diskon = 0
        
        
    if kupon == ("AconkGG"):
        diskon = diskon * 0.05
    else:
        diskon = 0
        
        
    total = subtotal * diskon * asuransi
    
    
    print("nama penyewa", nama)
    print("jenis kendaraan", jenis)
    print("berapa lama yang disewa", lama)
    print("kupon", kupon)
    print("total yang perlu di bayar", total)
    print("diskon", diskon)
    
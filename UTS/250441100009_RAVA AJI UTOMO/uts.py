pilihan = "y"
while pilihan == "y" or pilihan == "Y":
    print("1. Motor Matic : Rp 50.000")
    print("2. Motor Trail : Rp 100.000")
    print("1. Motor Sport : Rp 75.000")
    #cek lama nya
    pilih = int(input("Masukkan angak untuk sewa: "))
    if pilih == 1:
        harga = 50000
        motor = "Matic"
    elif pilih == 2:
        harga = 100000
        motor = "Trail"
    elif pilih == 3:
        harga = 75000
        motor = "SPort"
    else:
        print("masukkan angka yang bener!")
        continue
    #input sewanya
    lama = int(input("berapa lama anda sewa:"))
    subtotal = lama * harga 
    #cek lama
    if lama > 3:
        asuransi = (lama // 3) * 15000
    else:
        asuransi = 0
    total = subtotal + asuransi
    #hitung subtotal
    if subtotal > 150000:
        total = total - (total * 0.1) #tak buat ke desimal
    #cek kupon
    kupon = input("Masukkan kupon: ")
    if kupon == "AconkGG":
        total = total - (total * 0.05)
    print("Sewa motor: ", motor)
    print("Sewa: ", lama, "hari")
    print("Asuransi: ", asuransi)
    print("Total: ", int(total))

    pilihan = input("apakah ingin sewa lagi? (y/t): ")
    if pilihan == "y":
        continue




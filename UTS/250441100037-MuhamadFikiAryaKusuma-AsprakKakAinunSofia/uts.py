matic = 50000
trail = 100000
sport = 75000
hari = 0
asuransi = 15000
total = 0
diskon = 0.10
while True :
    a = input (str("masukan motor yang mau di rental(matic/trail/sport): "))
    if a == "matic":
        print (matic)
    elif a == "trail":
        print(trail)
    elif a == ("sport"):
        print (sport)
    else:
        print ("tidak ada dalam daftar")

    while True:
        b = int(input("masukan rental berapa hari: "))
        if b > 3 :
            total = asuransi + matic or trail or sport 
            print (total)
        elif total > 150000:
            subtotal= total * diskon
            print(subtotal)
        c = input ("apakah anda mau rental lagi: ")
        if c != "iya" :
            print ("program selesai")
            break
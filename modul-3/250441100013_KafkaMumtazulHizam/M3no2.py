PIN = 25013
kesempatan = 3

while kesempatan > 0:
    pin = int(input("Masukkan PIN anda: "))


    if pin == PIN:
        print("PIN benar, Selamat datang di bank BNI")
        break
    
    else:
        
        if len(str(pin)) > 5:
            print("PIN tidak boleh lebih dari 5 digit")
        elif len(str(pin)) < 5:
            print("PIN tidak boleh kurang dari 5 digit")
        
        kesempatan = kesempatan - 1
        if kesempatan > 0:
            print("PIN salah, coba lagi")
            print("Kesempatan anda sisa ", kesempatan, "kali")
        else:
            print("Akses ditolak, anda sudah 3 kali memasukkan PIN yang salah")
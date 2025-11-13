PIN_GUA = "25017"
kesempatan = 3
    
print("=== ATM ===")
    
while kesempatan > 0:
    pin = input("masukkan PIN: ")
        
    if pin == PIN_GUA:
        print("PIN benar, akses diterima")
        break
    elif len(pin) != 5:
        print("PIN HARUS 5 DIGIT")
    elif pin != "str":
        print("PIN HARUS BERBENTUK ANGKA")
    else:
        kesempatan -= 1
        if kesempatan > 0:
            print(f"PIN salah, coba lagi. sisa percobaan: {kesempatan}")
        else:
            print("akses ditolak, kartu diblokir")
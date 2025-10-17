lama_parkir = int(input("Berapa jam anda akan parkir: "))
vip = input("Apakah kamu member VIP? (ya/tidak): ")

if vip == "ya":
    total = 0
else:
    if (lama_parkir) <= 2:
        total = 5000
    elif lama_parkir <= 7:
        total = 5000 + (lama_parkir - 2) * 3000
    elif lama_parkir <= 24:
        total = 20000    
    else:
        hari = lama_parkir // 24
        sisa_jam = lama_parkir % 24
        
        total = hari *20000
        
        
        if sisa_jam > 0:
         print("ada sisa jam")
         if   sisa_jam <= 2:
           total = total + 5000
         elif sisa_jam <= 7:
           total = total + 5000 + (sisa_jam - 2) * 3000
         elif sisa_jam > 7:
           total = total + 20000    
         


print(f"Total biaya parkir: Rp{total}")
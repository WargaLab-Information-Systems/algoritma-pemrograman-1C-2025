lama_parkir = int(input("masukkan lama parkir (jam): "))
vip = input("apakah anda membeer vip? (ya/tidak): ").lower()
 
tarif = 0

if vip == "ya":
    tarif = 0 
    
else:
    if lama_parkir <= 2:
        tarif = 5000
    else:
        tarif = 5000 + (lama_parkir - 2) * 800
    
print(f"lama parkir: {lama_parkir} jam")
print(f"status vip: {vip}")
print(f"total biaya parkir anda adalah: Rp{tarif}")
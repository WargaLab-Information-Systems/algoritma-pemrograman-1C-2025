#input dari user
lama_parkir = int(input("masukkan lama parkir (jam): "))
status_VIP = input("apakah termasuk member VIP? (ya/tidak): ")

if status_VIP == "ya":
    biaya = 0
else:
    if lama_parkir <= 0:
        biaya = 0
    else:
        hari_penuh = lama_parkir // 24
        sisa_jam = lama_parkir % 24
        
        biaya_harian = hari_penuh * 20000 
        
        if sisa_jam <= 0:
            biaya_sisa = 0
        elif sisa_jam <= 2:
            biaya_sisa = 5000
        else:
            biaya_sisa = 5000 + (sisa_jam - 2) * 3000
            biaya_sisa = min(biaya_sisa, 20000)
        
        # Total biaya
        biaya = biaya_harian + biaya_sisa

print(f"total biaya adalah: Rp {biaya:,}")

parkir = float(input("Masukkan lama parkir (jam): "))
vip = input("Apakah member VIP? (y/t): ")
tarif_awal = 5000
tarif_tambahan = 3000
tarif_perhari = 20000  

if vip == "y":
    biaya = 0
else:
    if parkir <= 0:
        biaya = 0
    else:
        hari = int(parkir // 24)
        sisa_jam = parkir % 24

        if sisa_jam <= 2:
            biaya_sisa = tarif_awal
        else:
            parkir_tambahan = sisa_jam - 2
            biaya_sisa = (parkir_tambahan * tarif_tambahan) + tarif_awal  
        if biaya_sisa > tarif_perhari:
            biaya_sisa = tarif_perhari

        biaya = (hari * tarif_perhari) + biaya_sisa

print("Biaya parkir: Rp", biaya)

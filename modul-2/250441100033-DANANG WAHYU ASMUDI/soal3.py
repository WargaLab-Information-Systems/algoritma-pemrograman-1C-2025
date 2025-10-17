jam_parkir = int(input("Masukkan lama parkir (jam): "))

if jam_parkir < 0:
    print("Jam parkir tidak valid! Harus 0 atau lebih.")
    biaya = "TIDAK VALID"
else:
    status_vip = input("Apakah member VIP? (ya/tidak): ")
    # Konstanta biaya parkir
    biaya_2_jam_pertama = 5000
    biaya_per_jam_berikutnya = 3000
    biaya_maksimal = 20000
if jam_parkir >= 0:
    # Jika pengunjung adalah VIP, biaya parkir gratis
    if status_vip == "ya":
        biaya = 0    
    # Hitung biaya parkir untuk non-VIP
    else:
        if jam_parkir <= 2:
            biaya = biaya_2_jam_pertama
        else:
            biaya = biaya_2_jam_pertama + (jam_parkir - 2) * biaya_per_jam_berikutnya    
        # Terapkan batas maksimal biaya parkir
        if biaya > biaya_maksimal:
            biaya = biaya_maksimal

# Tampilkan biaya parkir
print("Total biaya parkir: Rp",biaya)
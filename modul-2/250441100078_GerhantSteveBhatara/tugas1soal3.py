lama_parkir = int(input("Masukkan lama parkir (dalam jam): "))
status_vip = input("Apakah Anda member VIP? (ya/tidak): ").lower()

if status_vip == "ya":
    total_biaya = 0
else:
    hari = lama_parkir // 24
    sisa_jam = lama_parkir % 24

    # Hari pertama: tarif dasar + tambahan
    if lama_parkir <= 2:
        total_biaya = 5000
    elif lama_parkir <= 24:
        total_biaya = min(5000 + (lama_parkir - 2) * 3000, 20000)
    else:
        # Hari pertama maksimal 20.000
        total_biaya = 20000
        # Hari berikutnya (setiap 24 jam penuh) = 24 jam × 3000
        total_biaya += (hari - 1) * 24 * 3000
        # Tambah sisa jam (setelah hari penuh) = 3000/jam
        total_biaya += sisa_jam * 3000

print(f"Lama parkir: {lama_parkir} jam")
print(f"Status VIP: {status_vip}")
print(f"Total biaya parkir: Rp{total_biaya:,}")

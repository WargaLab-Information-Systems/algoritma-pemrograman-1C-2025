lama_parkir = int(input("masukkan lama parkirnya (jam): "))
vip = input("apakah anda member VIP? (ya/tidak): ").lower()

tarif = 0

if vip == "ya":
    tarif = 0
else:
    if lama_parkir <= 2:
        tarif = 5000
    else:
        tarif = 5000 + (lama_parkir - 2) * 900

print(f"lama parkir: {lama_parkir} jam")
print(f"status VIP: {vip}")
print(f"total biaya parkir: Rp{tarif}")
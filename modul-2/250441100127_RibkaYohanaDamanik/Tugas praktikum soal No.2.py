# Program Menghitung Biaya Parkir (Versi Hari)

lama_hari = int(input("Masukkan lama parkir (hari): "))
vip = input("Apakah Anda member VIP (ya/tidak)? ")

# Jika VIP, langsung gratis
if vip == "ya":
    total = 0
else:
    # Setiap hari dikenai biaya Rp20.000
    tarif_per_hari = 20000
    total = lama_hari * tarif_per_hari

print(f"Total biaya parkir: Rp{total:,}")
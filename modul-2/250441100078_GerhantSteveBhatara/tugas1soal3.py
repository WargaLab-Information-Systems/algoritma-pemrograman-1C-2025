# Program menghitung biaya parkir di mall

# Input data dari pengguna
lama_parkir = int(input("Masukkan lama parkir (dalam jam): "))
status_vip = input("Apakah Anda member VIP? (ya/tidak): ").lower()

# Jika member VIP, gratis parkir
if status_vip == "ya":
    total_biaya = 0
else:
    # Hitung biaya berdasarkan durasi parkir
    if lama_parkir <= 2:
        total_biaya = 5000
    else:
        total_biaya = 5000 + (lama_parkir - 2) * 3000

    # Batasi maksimal tarif per hari
    if total_biaya > 20000:
        total_biaya = 20000

# Tampilkan hasil
print("HASIL PERHITUNGAN PARKIR :")
print(f"Lama parkir: {lama_parkir} jam")
print(f"Status VIP: {status_vip}")
print(f"Total biaya parkir: Rp{total_biaya:,}")
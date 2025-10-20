# Program menghitung tarif parkir mall sederhana

# Input data dari pengguna
lama_parkir = int(input("Masukkan lama parkir (jam): "))
status_vip = input("Apakah Anda member VIP? (ya/tidak): ")

# Jika member VIP, gratis parkir
if status_vip == "ya":
    total_bayar = 0
else:
    # Hitung biaya parkir berdasarkan jam
    if lama_parkir <= 2:
        total_bayar = 5000
    else:
        # 2 jam pertama Rp5.000, jam berikutnya Rp3.000 per jam
        total_bayar = 5000 + (lama_parkir - 2) * 3000
    
    # Batas maksimal biaya parkir Rp20.000
    if total_bayar > 20000:
        total_bayar = 20000

# Menampilkan hasil
print("\n=== RINCIAN PARKIR ===")
print("Lama parkir:", lama_parkir, "jam")
print("Status VIP:", status_vip)
print("Total biaya parkir: Rp", total_bayar)

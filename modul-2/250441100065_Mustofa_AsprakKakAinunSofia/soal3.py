# Program Perhitungan Tarif Parkir Mall

# Input data dari pengguna
lama_parkir = int(input("Masukkan lama parkir (jam): "))
vip = input("Apakah Anda member VIP? (ya/tidak): ").lower()

# Cek status VIP
if vip == "ya":
    biaya = 0   # Jika VIP gratis
    keterangan = "Anda adalah member VIP, parkir gratis."
else:
    # Hitung biaya parkir biasa
    if lama_parkir <= 2:
        biaya = 5000 # 2 jam pertama Rp5000
    else:
        biaya = 5000 + (lama_parkir - 2) * 3000 # Tambahan Rp3000 per jam setelah 2 jam

    # Cek batas maksimal
    if biaya > 20000:
        biaya = 20000
        keterangan = "Biaya telah mencapai batas maksimal Rp20.000 per hari."
    else:
        keterangan = "Biaya dihitung berdasarkan lama parkir Anda."

# Tampilkan hasil
print("\n=== Hasil Perhitungan Parkir ===")
print(f"Lama parkir       : {lama_parkir} jam")
print(f"Status VIP        : {'Ya' if vip == 'ya' else 'Tidak'}")
print(f"Total biaya parkir: Rp{biaya}")
print(f"Keterangan        : {keterangan}")


# tarif parkir Mall
print ("=== Tarif Parkir Mall ===")
print ("\nKetentuan tarif parkir: ")
print ("1. 2 jam pertama: Rp.5000")
print ("2. Setiap jam berikutnya: Rp.3000")
print ("3. Maksimal tarif parkir/hari: Rp.20000")

# input
lama_parkir = int(input("\nMasukkan lama parkir (jam): "))
status_vip = input("Apakah member VIP? (ya/tidak): ").lower()
if status_vip == 'ya':
    biaya = 0
    print ("Status VIP: berhasil")
elif lama_parkir <= 2:
    biaya = 5000
    print("Status VIP: tidak berhasil")
else:
    biaya = 5000 + (lama_parkir - 2) * 3000
    print("Status VIP: tidak berhasil")
    if biaya > 20000:
        biaya = 20000

# hasil
print(f"Total biaya parkir: Rp{biaya: }")
print ("\n===TERIMA KASIH===")

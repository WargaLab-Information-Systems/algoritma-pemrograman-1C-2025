#Gaji Mingguan Pak Wowo
#sehari100k,shiftmlm50k,1–3 jam = Rp25.000 per jam, 4 jam = Rp100.000, 6 jam= Rp200.000, 8 jam = Rp300.000.
#jklmbrlbhdri3jmmkhangus/tdkdihitung

total_gaji = 0 #buatnyimpentotal uang
total_lembur = 0 #buatnyimpentotal jam
total_bonus_shift = 0 #buatnyimpentotal bonus

for hari in range(1, 8):
    print(f"\nHari ke-{hari}")
    while True:
            jam_lembur = int(input("Masukkan jumlah jam lembur: "))
            if jam_lembur < 0:
                print("Jam lembur tidak boleh negatif.")
                continue
            break
            print("Mskkn angka yang benar!")

    shift = input("Apkh shift malam? (y/n): ").lower()
    gaji_harian = 100000

    # Hitung lembur
    if 1 <= jam_lembur <= 3:
        gaji_harian += jam_lembur * 25000
    elif jam_lembur == 4:
        gaji_harian += 100000
    elif jam_lembur == 6:
        gaji_harian += 200000
    elif jam_lembur == 8:
        gaji_harian += 300000
    elif jam_lembur > 8:
        print("Lembur melebihi batas, tidak dihitung.")

    # Hitung bonus shift malam
    if shift == "y":
        gaji_harian += 50000
        total_bonus_shift += 50000

    total_gaji += gaji_harian
    total_lembur += jam_lembur

print("\n=== Rekap Gaji Mingguan ===")
print(f"Total jam lembur: {total_lembur} jam")
print(f"Total bonus shift malam: Rp{total_bonus_shift}")
print(f"Total gaji seminggu: Rp{total_gaji}")
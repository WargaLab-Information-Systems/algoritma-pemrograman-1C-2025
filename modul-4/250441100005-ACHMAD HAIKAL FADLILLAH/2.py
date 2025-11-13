total_gaji = 0
total_lembur = 0
total_bonus = 0

for hari in range(1, 7 + 1):
    print(f"=== Hari ke-{hari} ===")
    gaji_pokok = 100000

    while True:
        lembur = int(input("Masukkan jumlah jam lembur: "))
        if lembur < 0:
            print("Jam lembur tidak boleh negatif.")
            continue
        break

    tambahan = 0
    if 1 <= lembur <= 3:
        tambahan = lembur * 25000
    elif lembur == 4:
        tambahan = 100000
    elif lembur <= 6:
        tambahan = 200000
    elif lembur <= 8:
        tambahan = 300000
    elif lembur > 8:
        print("Lembur melebihi batas, tidak dihitung.")
        lembur = 0
    
    shift = input("Apakah hari ini shift malam? (y/n): ").lower()
    if shift == 'y':
        bonus = 50000
    elif shift == 'n':
        bonus = 0
    else:
        print("Input tidak valid! Bonus tidak diberikan.")
        bonus = 0

    gaji_harian = gaji_pokok + tambahan + bonus
    total_gaji += gaji_harian
    total_lembur += lembur
    total_bonus += bonus

print("\n=== Rekapitulasi Mingguan ===")
print(f"Total jam lembur: {total_lembur} jam")
print(f"Total bonus shift malam: Rp{total_bonus:,}")
print(f"Total gaji seminggu: Rp{total_gaji:,}")

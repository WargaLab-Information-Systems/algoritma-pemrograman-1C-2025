gaji = 0 
lembur = 0
bonus_shift = 0


for hari in range(1, 8):
    print(f"hari ke-{hari}")
    
    jam = int(input("masukkan jam lembur: "))

    if jam == 0:
        break

    if 1 <= jam <= 3:
        gaji_lembur = jam * 25000
    elif jam == 4:
        gaji_lembur = 100000
    elif jam == 6:
        gaji_lembur = 200000
    elif jam == 8:
        gaji_lembur = 300000
    elif jam > 8:
        print("lembur melebihi batas, tidak dihitung")
        gaji_lembur = 0
    else:
        gaji_lembur = 0

    lembur += jam

    shift = input("apakah shift malam (y/n): ")

    if shift == "y" or shift == "Y":
        bonus = 50000
        bonus_shift += bonus
    elif shift == "n" or shift == "N":
        bonus = 0
    else:
        print("input tidak valid, bukan shift malam")
        bonus = 0

    gaji_harian = 100000 + gaji_lembur + bonus
    gaji += gaji_harian

    print(f"gaji hari ke-{hari}: Rp{gaji_harian:,}")


print("REKAP GAJI MINGGUAN BAPAK WOWO")
print(f"total jam lembur: {lembur} jam")
print(f"total bonus shift malam: Rp{bonus_shift:,}")
print(f"total gajian seminggu: Rp{gaji:,}")
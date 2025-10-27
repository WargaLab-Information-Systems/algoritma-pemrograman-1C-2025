total_gaji = 0
total_jam_lembur = 0
total_bonus_malam = 0

for hari in range(1, 8):
    print(f"Hari {hari}:")

    jam_lembur = int(input("Jam lembur: "))
    shift_malam = input("Shift malam? (y/n): ")
    if jam_lembur > 8:
        print("Lembur melebihi batas, tidak dihitung.")
        lembur = 0
    elif jam_lembur in [1, 2, 3]:
        lembur = jam_lembur * 25000
    elif jam_lembur == 4:
        lembur = 100000
    elif jam_lembur == 6:
        lembur = 200000
    elif jam_lembur == 8:
        lembur = 300000
    else:
        lembur = 0
    
    bonus = 50000 if shift_malam == 'y' else 0
    gaji_hari = 100000 + lembur + bonus
    print(f"Gaji hari ini: Rp{gaji_hari}")
    total_gaji += gaji_hari
    total_jam_lembur += jam_lembur
    total_bonus_malam += bonus

print(f"\nTotal jam lembur: {total_jam_lembur}")
print(f"Total bonus malam: Rp{total_bonus_malam}")
print(f"Total gaji: Rp{total_gaji}")
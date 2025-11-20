
total_gaji = 0
total_lembur = 0
total_bonus = 0

for hari in range (1,8):
    print(f"hari ke-{hari:}")

    while True:
        try:
            jam_lembur = int(input("masukan jam lembur:"))
            shift_malam = input("apakah shitf malam? ('y'/'n'):")

            if jam_lembur < 0:
                print("jam lembur tidak boleh negatif.")
                continue 
            if shift_malam not in ['y', 'n']:
                print("input shift harus 'y' atau 'n'.")
                continue
            break
        except ValueError:
            print("input harus berupa angaka untuk jam lembur.")

    gaji_harian = 100000
    lembur_harian = 0
    bonus = 0

    if 1 <= jam_lembur <= 3:
        lembur_harian = jam_lembur * 25000
    elif jam_lembur == 4:
        lembur_harian = 100000
    elif jam_lembur == 6:
        lembur_harian = 200000
    elif jam_lembur == 8:
        lembur_harian = 300000
    elif jam_lembur > 8:
        print("jam lembur tidak valid!")
        lembur_harian = 0

    if shift_malam == "y":
        bonus_harian = 50000

    total_lembur += lembur_harian
    total_bonus += bonus_harian
    total_gaji += gaji_harian + lembur_harian + bonus_harian 

print(" gaji mingguan pak wowo ")
print(f"total lembur: Rp{total_lembur}")
print(f"total bonus shift malam: Rp{total_bonus}")
print(f"total gaji mingguan: Rp{total_gaji}")

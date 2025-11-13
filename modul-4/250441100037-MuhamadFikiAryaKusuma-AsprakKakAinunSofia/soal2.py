total_gaji = 0
total_lembur = 0
total_bonus_shift_malam = 0
for hari in range(1, 8):
    print(f"Hari ke-{hari}:")
    while True:
        try:
            jam_lembur = int(input("Masukkan jumlah jam lembur: "))
            if jam_lembur < 0:
                print("Jumlah jam lembur tidak boleh negatif. Silakan coba lagi.")
                continue
            break
        except ValueError:
            print("Input tidak valid. Silakan masukkan angka.")

    while True:
        shift_malam = input("Apakah hari ini shift malam? (y/n): ")
        if shift_malam not in ('y', 'n'):
            print("Input tidak valid. Silakan masukkan 'y' atau 'n'.")
            continue
        break

    gaji_harian = 100000

    if 1 <= jam_lembur <= 3:
        gaji_harian += jam_lembur * 25000
        total_lembur += jam_lembur
    elif jam_lembur == 4:
        gaji_harian += 100000
        total_lembur += jam_lembur
    elif jam_lembur == 5:
        gaji_harian += 150000
        total_lembur += jam_lembur
    elif jam_lembur == 6:
        gaji_harian += 200000
        total_lembur += jam_lembur
    elif jam_lembur == 7:
        gaji_harian += 250000
        total_lembur += jam_lembur
    elif jam_lembur == 8:
        gaji_harian += 300000
        total_lembur += jam_lembur
    elif jam_lembur > 8:
        print("Lembur melebihi batas, tidak dihitung.")

    if shift_malam == 'y':
        gaji_harian += 50000
        total_bonus_shift_malam += 50000

    total_gaji += gaji_harian

print(" Ringkasan Gaji Mingguan:")
print(f"Total Jam Lembur: {total_lembur} jam")
print(f"Total Bonus Shift Malam: {total_bonus_shift_malam}")
print(f"Total Gaji: {total_gaji}")

# Program Gaji Mingguan Pak Wowo

total_gaji = 0
total_lembur = 0
total_bonus = 0

print("=== Program Hitung Gaji Mingguan Pak Wowo ===")

for hari in range(1, 8):
    print(f"\nHari ke-{hari}")
    
    while True:
        try:
            jam_lembur = int(input("Masukkan jumlah jam lembur (0-8): "))
            if jam_lembur < 0:
                print("Jam lembur tidak boleh negatif.")
                continue
            break
        except ValueError:
            print("Input tidak valid, masukkan angka bulat.")
    
    while True:
        shift_malam = input("Apakah shift malam? (y/n): ").lower()
        if shift_malam in ('y', 'n'):
            break
        else:
            print("Input tidak valid. Ketik 'y' untuk ya atau 'n' untuk tidak.")

    gaji = 100000

    if 1 <= jam_lembur <= 3:
        gaji += jam_lembur * 25000
        total_lembur += jam_lembur
    elif jam_lembur == 4:
        gaji += 100000
        total_lembur += jam_lembur
    elif jam_lembur == 5:
        gaji += 125000
        total_lembur += jam_lembur
    elif jam_lembur == 6:
        gaji += 200000
        total_lembur += jam_lembur
    elif jam_lembur == 7:
        gaji += 225000
        total_lembur += jam_lembur
    elif jam_lembur == 8:
        gaji += 300000
        total_lembur += jam_lembur
    elif jam_lembur > 8:
        print("Lembur melebihi batas, tidak dihitung.")
        gaji += 300000
        total_lembur += jam_lembur

    if shift_malam == 'y':
        gaji += 50000
        total_bonus += 50000

    total_gaji += gaji

print("\n===== Laporan Mingguan Pak Wowo =====")
print(f"Total jam lembur       : {total_lembur} jam")
print(f"Total bonus shift malam: Rp{total_bonus:,}")
print(f"Total gaji seminggu    : Rp{total_gaji:,}")
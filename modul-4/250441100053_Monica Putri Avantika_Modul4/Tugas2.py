# Program menghitung total gaji mingguan Pak Wowo

total_gaji = 0
total_jam_lembur = 0
total_bonus_shift = 0

# Gaji pokok per hari
gaji_pokok = 100000

print("=== Perhitungan Gaji Mingguan Pak Wowo ===")

for hari in range(1, 8):  # 7 hari kerja
    print(f"\nHari ke-{hari}:")
    
    # --- Input jumlah jam lembur dengan validasi ---
    while True:
        try:
            jam_lembur = int(input("Masukkan jumlah jam lembur hari ini: "))
            if jam_lembur < 0:
                print("Jam lembur tidak boleh negatif. Coba lagi.")
                continue
            break
        except ValueError:
            print("Input tidak valid! Masukkan angka.")
    
    # --- Input shift malam dengan validasi ---
    while True:
        shift = input("Apakah shift malam? (y/n): ")
        if shift in ['y', 'n']:
            break
        else:
            print("Input tidak valid! Masukkan 'y' untuk ya atau 'n' untuk tidak.")
    
    # --- Hitung gaji harian ---
    gaji_harian = gaji_pokok
    bonus_shift = 0
    gaji_lembur = 0

    # Perhitungan lembur
    if jam_lembur == 0:
        gaji_lembur = 0
    elif 1 <= jam_lembur <= 3:
        gaji_lembur = jam_lembur * 25000
    elif jam_lembur == 4:
        gaji_lembur = 100000
    elif jam_lembur == 5:
        gaji_lembur = 125000
    elif jam_lembur == 6:
        gaji_lembur = 200000
    elif jam_lembur == 7:
        gaji_lembur = 225000
    elif jam_lembur == 8:
        gaji_lembur = 300000
    elif jam_lembur > 8:
        print("Lembur melebihi batas, tidak dihitung.")
        gaji_lembur = 300000
    
    # Bonus shift malam
    if shift == 'y':
        bonus_shift = 50000
        total_bonus_shift += bonus_shift
    
    # Hitung total harian
    gaji_harian += gaji_lembur + bonus_shift

    # Tambahkan ke total mingguan
    total_gaji += gaji_harian
    total_jam_lembur += jam_lembur

    # Tampilkan hasil hari itu
    print(f"Gaji hari ke-{hari}: Rp{gaji_harian:,}")

# --- Hasil akhir setelah 7 hari ---
print("====== Rekapitulasi Gaji Mingguan ========")
print(f"Total jam lembur selama seminggu : {total_jam_lembur} jam")
print(f"Total bonus shift malam           : Rp{total_bonus_shift:,}")
print(f"Total gaji mingguan               : Rp{total_gaji:,}")
print("==========================================")

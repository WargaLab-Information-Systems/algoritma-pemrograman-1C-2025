# Program untuk menghitung gaji mingguan Pak Wowo

# Inisialisasi variabel total
total_gaji = 0
total_jam_lembur = 0
total_bonus_malam = 0

# Loop untuk 7 hari
for hari in range(1, 8):
    # Validasi input jam lembur
    input_valid = False
    while not input_valid:
        jam_lembur_str = input(f"Hari {hari}: Masukkan jam lembur (bilangan bulat 0-24): ")
        # Cek apakah semua karakter adalah digit
        adalah_digit = True
        
        for karakter in jam_lembur_str:
            if karakter not in '0123456789':
                adalah_digit = False
                break
        if adalah_digit and jam_lembur_str != '':
            jam_lembur = int(jam_lembur_str)
            if 0 <= jam_lembur <= 24:
                input_valid = True
            else:
                print("Jam lembur harus antara 0 dan 24. Coba lagi.")
        else:
            print("Input jam lembur harus berupa bilangan bulat. Coba lagi.")
    
    # Validasi input shift malam
    shift_valid = False
    while not shift_valid:
        shift_malam = input("Apakah hari ini shift malam? (y/n): ")
        if shift_malam in ['y', 'n', 'Y', 'N']:
            shift_valid = True
        else:
            print("Input shift malam harus 'y' atau 'n'. Coba lagi.")
    
    # Menghitung tambahan lembur
    if jam_lembur == 0:
        tambahan_lembur = 0
    elif 1 <= jam_lembur <= 3:
        tambahan_lembur = 25000 * jam_lembur
    elif jam_lembur == 4:
        tambahan_lembur = 100000
    elif jam_lembur == 5:
        tambahan_lembur = 25000 + 100000  # 1 jam + 4 jam
    elif jam_lembur == 6:
        tambahan_lembur = 200000
    elif jam_lembur == 7:
        tambahan_lembur = 200000 + 25000  # 6 jam + 1 jam
    elif jam_lembur == 8:
        tambahan_lembur = 300000
    else:
        print("Lembur melebihi batas, tidak dihitung.")
        tambahan_lembur = 0
    
    # Tambahkan jam lembur ke total jika valid
    if tambahan_lembur > 0:
        total_jam_lembur += jam_lembur
    
    # Bonus shift malam
    bonus_malam = 50000 if shift_malam in ['y', 'Y'] else 0
    total_bonus_malam += bonus_malam
    
    # Gaji
    gaji_harian = 100000 + tambahan_lembur + bonus_malam
    total_gaji += gaji_harian

# Menampilkan hasil
print(f"\nTotal jam lembur selama seminggu: {total_jam_lembur} jam")
print(f"Total bonus shift malam: Rp{total_bonus_malam:,}")
print(f"Total gaji seminggu: Rp{total_gaji:,}")

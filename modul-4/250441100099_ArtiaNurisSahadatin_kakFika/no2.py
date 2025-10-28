#==PROGRAM GAJI MINGGUAN PAK WOWO==
total_gaji = 0
total_lembur = 0
total_bonus_shift = 0

# Perulangan selama 7 hari (seminggu)
for hari in range(1, 8):
    print(f"\nHari ke-{hari}:")
    
    # Input jam lembur (harus angka)
    lembur_input = input("Masukkan jam lembur: ")
    while not lembur_input.isdigit(): #untuk memestikan input itu angka
        print(" Input harus berupa angka! Coba lagi.")
        lembur_input = input("Masukkan jam lembur: ")
    lembur = int(lembur_input)

    # Input shift malam (harus y/n)
    shift = input("Apakah shift malam? (y/n): ")
    while shift not in ['y', 'n']:
        print(" Input harus 'y' untuk ya atau 'n' untuk tidak!")
        shift = input("Apakah shift malam? (y/n): ")
  # Hitung gaji harian
    gaji_pokok = 100000
    bonus_lembur = 0

    if lembur > 8:
        print("Lembur melebihi batas, tidak dihitung.")
    elif lembur == 4:
        bonus_lembur = 100000
    elif lembur == 6:
        bonus_lembur = 200000
    elif lembur == 8:
        bonus_lembur = 300000
    elif 1 <= lembur <= 3:
        bonus_lembur = lembur * 25000

    bonus_shift = 50000 if shift == 'y' else 0

    # Tambahkan ke total mingguan
    total_lembur += lembur if lembur <= 8 else 0
    total_bonus_shift += bonus_shift
    total_gaji += gaji_pokok + bonus_lembur + bonus_shift

# Tampilkan hasil akhir
print("\n=== HASIL AKHIR ===")
print(f"Total jam lembur: {total_lembur} jam")
print(f"Total bonus shift malam: Rp{total_bonus_shift}")
print(f"Total gaji seminggu: Rp{total_gaji}")
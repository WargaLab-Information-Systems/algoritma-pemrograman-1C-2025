t_jam_lembur = 0
t_bonus_shift = 0
t_gaji = 0

gaji_harian = 100_000

for hari in range(1, 8):

    while True:
        jam_lembur = input(f"Hari ke-{hari}, masukkan jumlah jam lembur: ")
        if jam_lembur.isdigit():
            jam_lembur = int(jam_lembur)
            if jam_lembur >= 0:
                break
            else:
                print("Tidak boleh negatif Coba lagi.")
        else:
            print("Harus berupa angka Coba lagi.")

  
    shift = input("Apakah hari ini shift malam? (y/n): ").lower()
    while shift not in ('y', 'n'):
        shift = input("Input tidak valid! Harus 'y' atau 'n': ").lower()


    if 1 <= jam_lembur <= 3:
        uang_lembur = jam_lembur * 25_000
    elif jam_lembur == 4:
        uang_lembur = 100_000
    elif jam_lembur == 5:
        uang_lembur = 150_000
    elif jam_lembur == 6:
        uang_lembur = 200_000
    elif jam_lembur == 8:
        uang_lembur = 300_000
    elif jam_lembur > 8:
        uang_lembur = 0
        print("Lembur melebihi batas, tidak dihitung.")
    else:
        uang_lembur = 0


    bonus_shift = 50_000 if shift == 'y' else 0


    gaji_total_harian = gaji_harian + uang_lembur + bonus_shift


    t_jam_lembur += jam_lembur
    t_bonus_shift += bonus_shift
    t_gaji += gaji_total_harian

    print(f"Gaji hari ke-{hari}: Rp{gaji_total_harian:,}\n")

print(f"Total jam lembur: {t_jam_lembur} jam")
print(f"Total bonus shift malam: Rp{t_bonus_shift:,}")
print(f"Total gaji seminggu: Rp{t_gaji:,}")
gaji = 0
lembur = 0
total_bonus_shift = 0

for hari in range(1, 8):
    print(f"\nHari ke-{hari}")
    while True:
        try:
            jam_lembur = int(input("Masukkan jam lembur : "))
            if jam_lembur < 0:
                print("Jam harus bernilai positif!")
                continue
            break
        except ValueError:
            print("Input tidak valid. Harus berupa angka!")
    if jam_lembur == 0 :
        print("Anda memasukkan 0 jam lembur. Program dihentikan. ULANGG!!")
        break

    while True:
        shift_malam = input("Apakah shift malam? (Y/N) : ")
        if shift_malam in ["Y", "N", "y", "n"]:
            break
        else:
            print("Input tidak valid. Harus 'Y' atau 'N'.")
    
    gaji_pokok = 100000
    tambahan_lembur = 0
    
    if jam_lembur == 0:
        tambahan_lembur = 0
    elif 1 <= jam_lembur <= 3:
        tambahan_lembur = jam_lembur * 25000
    elif jam_lembur == 4:
        tambahan_lembur = 100000
    elif jam_lembur == 6:
        tambahan_lembur = 200000
    elif jam_lembur == 8:
        tambahan_lembur = 300000
    elif jam_lembur > 8:
        print("Lembur melebihi batas, tidak dihitung.")
        jam_lembur = 0

    if shift_malam == "Y" or shift_malam == "y":
        bonus_shift = 50000
    else:
        bonus_shift = 0
    
    gaji_harian = gaji_pokok + tambahan_lembur + bonus_shift
    gaji += gaji_harian
    lembur += jam_lembur
    total_bonus_shift += bonus_shift

print("\n===== Rekap Mingguan Gaji Pak Wowo =====")
print(f"Total lembur : {lembur} jam")
print(f"Total bonus shift malam : Rp{total_bonus_shift:,}")
print(f"Total gaji dalam seminggu : Rp{gaji:,}")
print("\n")


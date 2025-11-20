total_gaji = 0
total_jam_lembur = 0
total_bonus_shift_malam = 0
gaji_pokok = 100000

for hari in range(1, 8):
    print(f"\nhari {hari}:")
    
    while True:
        jam_lembur_str = input("masukkan jumlah jam lembur: " )
        if jam_lembur_str.isdigit():
            jam_lembur = int(jam_lembur_str)
            if jam_lembur >= 0:
                break
            
            else:
                print("jumlah jam lembur tidak boleh negatif, coba lagi")
        else:
            print("input harus berupa angka bulat positif, coba lagi")

    gaji_lembur = 0
    if 1 <= jam_lembur <= 3 :
        gaji_lembur = jam_lembur * 25000
        total_jam_lembur += jam_lembur
    elif jam_lembur == 4 :
        gaji_lembur = 100000
        total_jam_lembur += jam_lembur
    elif jam_lembur == 6 :
        gaji_lembur = 200000
        total_jam_lembur += jam_lembur
    elif jam_lembur == 8 :
        gaji_lembur = 300000
        total_jam_lembur += jam_lembur
    elif jam_lembur > 8 :
        print("lembur melebihi batas, tidak dihitung")

    while True:
        shift_malam = input("apakah hari ini shift malam (y/n): ")
        if shift_malam in ['y', 'n']:
            break
        else:
            print("input harus 'y' atau 'n' . coba lagi")

    bonus_shift_malam = 0
    if shift_malam == 'y':
       bonus_shift_malam = 50000
       total_bonus_shift_malam += bonus_shift_malam
      
       gaji_pokok = 100000 + jam_lembur + shift_malam
    
    gaji_pokok = 100000 + gaji_lembur + bonus_shift_malam
    total_gaji += gaji_pokok
    print(f"gaji hari ini: Rp{gaji_pokok:,}")

print("\n=== Ringkasan Mingguan ===")
print(f"total jam lembur: {total_jam_lembur} jam")
print(f"total bonus shift malam: Rp{total_bonus_shift_malam:,}")
print(f"total gaji seminggu: Rp{total_gaji:,}")
 
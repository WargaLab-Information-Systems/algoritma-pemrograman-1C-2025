total_gaji_mingguan = 0
total_jam_lembur = 0
total_bonus_malam = 0
gaji_pokok_harian = 100000

for hari in range(1, 8):
    print(f"\nhari ke-{hari}:")

    while True:
        try:
            jam_lembur = int(input(f"masukkan jumlah jam lembur: "))
            if jam_lembur < 0:
               print("jam lembur tidak boleh kurang dari 0.")
            else:
               break 
        except ValueError:
            print("input tidak valid. masukkan angka.")
    
    while True:
        shift_malam = input("apakah hari ini shift malam? (y/n): ")
        if shift_malam in ['y', 'n']:
           break
        else:
           print("input tidak valid masukkan 'y' atau 'n'.")          

    gaji_lembur_hari_ini = 0
    if jam_lembur == 0:
       print("tidak ada lembur hari ini.")
    elif jam_lembur > 8:
       print("lembur melebihi batas, tiak dihitung.")
    elif 1 <= jam_lembur <= 3:
       gaji_lembur_hari_ini = jam_lembur * 25000
    elif jam_lembur == 4:
       gaji_lembur_hari_ini = 100000
    elif jam_lembur == 6:
       gaji_lembur_hari_ini = 200000
    elif jam_lembur == 8:
       gaji_lembur_hari_ini = 300000


    bonus_malam_hari_ini = 0
    if shift_malam == 'y':
       bonus_malam_hari_ini = 50000

    gaji_harian = gaji_pokok_harian + gaji_lembur_hari_ini + bonus_malam_hari_ini

    total_gaji_mingguan += gaji_harian
    total_jam_lembur += jam_lembur
    total_bonus_malam += bonus_malam_hari_ini

print("\n--- Ringkasan gaji mingguan ---")
print(f"total jam lembur: {total_jam_lembur} jam")
print(f"total bonus shift malam: Rp{total_bonus_malam:,.0f}")
print(f"total gaji seminggu: Rp{total_gaji_mingguan:,.0f}")
     
# soal 2
total_gaji = 0      
total_lembur = 0    
total_bonus = 0     
for hari in range(1, 8):  # ulang dari hari ke 1-7
    print("Hari ke-", hari)  # tampil nomor hari
    jam_lembur = -1
    while jam_lembur < 0 or jam_lembur > 24:  # loop sampai input jam lembur bener
        jam_input = input("Masukkan jumlah jam lembur (0-8): ")
        if jam_input == "`":
            print("Input tidak boleh kosong.")
            continue

        angka_valid = True
        for c in jam_input:
            if c < "0" or c > "9":
                angka_valid = False
                break
        if not angka_valid:
            print("harus berupa angka.")
            continue
        jam_lembur = int(jam_input)
        if jam_lembur < 0 or jam_lembur > 24:
            print("Jumlah jam tidak boleh negatif atau lebih dari 24.")
    shift = ""
    while shift != "y" and shift != "n":  # loop sampai input shift malam bener
        shift = input("Apakah shift malam? (y/n): ")
        if shift != "y" and shift != "n":
            print("Masukkan 'y' atau 'n'.")
    gaji_harian = 100000 
    tambahan_lembur = 0
    bonus = 0
    if jam_lembur == 0:
        tambahan_lembur = 0
    elif jam_lembur >= 1 and jam_lembur <= 3:
        tambahan_lembur = jam_lembur * 25000
    elif jam_lembur == 4:
        tambahan_lembur = 100000
    elif jam_lembur == 6:
        tambahan_lembur = 200000
    elif jam_lembur == 8:
        tambahan_lembur = 300000
    elif jam_lembur > 8:
        print("Lembur melebihi batas, tidak dihitung.")
        tambahan_lembur = 0
    if shift == "y":
        bonus = 50000
        total_bonus = total_bonus + bonus
    if jam_lembur <= 8:
        total_lembur = total_lembur + jam_lembur
    gaji_harian = gaji_harian + tambahan_lembur + bonus
    total_gaji = total_gaji + gaji_harian
    
print("Total jam lembur       :", total_lembur, "jam")
print("Total bonus shift malam: Rp", total_bonus)
print("Total gaji seminggu    : Rp", total_gaji)
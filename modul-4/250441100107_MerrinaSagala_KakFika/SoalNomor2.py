#==PROGRAM GAJI MINGGUAN PAK WOWO==
# total_lembur = 0
# total_bonus = 0
# total_gaji = 0

# for hari in range (1,8): #selama 7 hari #jadi pengulanggannya dimulai dari 1,2,3,4,5,6,7
#     print (f"\nHari ke - {hari}") #\n dipakai agar hasil rapi kebawahhh
#     jam_lembur = int (input("masukkan jumlah jam lembur:"))
#     shift_malam = input ("masukkan shift malam (y/n):")

#     gaji_pokok = 100000
#     tambahan = 0
#     if 1 <= jam_lembur <= 3:
#         tamabahan = jam_lembur*25000
#     elif jam_lembur == 4:
#         tambahan = 100000
#     elif jam_lembur == 6:
#         tambahan = 200000
#     elif jam_lembur == 8:
#         tambahan = 300000
#     elif jam_lembur>8:
#         print ("Lembur melebihi batas, tak dikira")
#         tambahan = 0

# gaji_hari_ini = gaji_pokok + tambahan
# total_lembur += jam_lembur

# if shift_malam == "y": 
#     gaji_hari_ini += 50000
#     total_bonus += 50000
    
# total_gaji += gaji_hari_ini
# print ("\n===REKAP GAJI MINGGUAN===")
# print (f"total jam lembur : {total_lembur}jam")
# print (f"total bonus malam : Rp {total_bonus_malam}")
# print (f"total gaji seminggu : Rp{total_gaji}")


#==PROGRAM GAJI MINGGUAN PAK WOWO==
total_gaji = 0
total_lembur = 0
total_bonus_shift = 0

# Perulangan selama 7 hari (seminggu)
for hari in range(1, 8): 
    print(f"\nHari ke-{hari}:")# diguankan f" karena format string dan \n spasi kebawah
    
    # Input jam lembur (harus angka)
    lembur_input = input("Masukkan jam lembur: ")
    while not lembur_input.isdigit(): #memastikan input adalah angka
        print(" Input harus berupa angka! Coba lagi.")
        lembur_input = input("Masukkan jam lembur: ")
    lembur = int(lembur_input)

    # Input shift malam (harus y/n)
    shift = input("Apakah shift malam? (y/n): ")
    while shift not in ['y', 'n']: #
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
print(f"Total gaji seminggu: Rp{total_gaji}")


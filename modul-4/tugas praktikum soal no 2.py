total_gaji = 0
total_lembur = 0
total_bonus_malam = 0

print("=== PROGRAM HITUNG GAJI MINGGUAN PAK WOWO ===")

for hari in range(1, 8):#untuk hitung per hari dalam seminggu
    print(f"Hari {hari}:")
    
    while True:#looping sampai input valid
        try:
            jam_lembur = int(input("Masukkan jumlah jam lembur: "))
            if jam_lembur < 0:
                print("Jam lembur tidak boleh negatif. Silakan coba lagi.")
                continue
            break
        except ValueError:
            print("input tidak valid. hanya angka yang dierbolehkan.")
    
    while True:#looping sampai input valid lagi
        shift_malam = input("apakah hari ini shift malam? (y/n): ")
        if shift_malam in ['y', 'n', 'yes', 'no', 'Y', 'N']:
            break
        else:
            print("input tidak valid. masukkan 'y' untuk ya atau 'n' untuk tidak.")
    
    # Hitung gaji pokok
    gaji_harian = 100000 #ada di soal
    
    # Hitung gaji lembur
    if jam_lembur == 0:# tidak lembur
        gaji_lembur = 0
    elif 1 <= jam_lembur <= 3:# lembur 1-3 jam
        gaji_lembur = jam_lembur * 25000#per jam
    elif jam_lembur == 4:
        gaji_lembur = 100000
    elif jam_lembur == 6:
        gaji_lembur = 200000
    elif jam_lembur == 8:
        gaji_lembur = 300000
    elif jam_lembur > 8:
        print("Lembur melebihi batas, tidak dihitung.")
        gaji_lembur = 0#tidak dihitung
    else:# untuk jam lembur 5 dan 7 karena ga ada ketentuan di soal gatau bener ngganya, tanyain ke kak faza
        gaji_lembur = 0
    
    # Hitung bonus shift malam
    bonus_malam = 50000 if shift_malam == 'y' else 0#ternary kalo ga salah
    
    # Total gaji harian
    gaji_total_harian = gaji_harian + gaji_lembur + bonus_malam#jumlahin semua
    
    # Akumulasi total
    total_gaji += gaji_total_harian
    total_lembur += jam_lembur
    total_bonus_malam += bonus_malam#jumlah bonus malam
    
    print(f"Gaji hari {hari}: Rp{gaji_total_harian:,}")

# Tampilkan hasil akhir
print("\n=== REKAP MINGGUAN ===")
print(f"Total jam lembur: {total_lembur} jam")
print(f"Total bonus shift malam: Rp{total_bonus_malam:,}")
print(f"Total gaji seminggu: Rp{total_gaji:,}")
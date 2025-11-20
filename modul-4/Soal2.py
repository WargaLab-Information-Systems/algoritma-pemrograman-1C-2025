# Program menghitung total gaji seminggu
total_overtime_hours = 0
total_night_bonus = 0
total_salary = 0

for day in range(1, 8):
    print(f"\nHari ke-{day}")
    
    # Input jam lembur
    overtime_hours = int(input("Masukkan jumlah jam lembur: "))
    overtime_pay = int(overtime_hours * 25000)
    
    # Validasi input shift malam
    while True:
        night_shift = input("Apakah shift malam? (y/n): ").lower()
        if night_shift in ['y', 'n']:
            break
        else:
            print("Input harus 'y' atau 'n'. Coba lagi.")
    
    # Hitung bonus shift malam
    night_bonus = 50000 if night_shift == 'y' else 0
    
    # Hitung gaji harian
    daily_salary = 100000 + overtime_pay + night_bonus
    
    # Akumulasi total
    total_overtime_hours += overtime_hours
    total_night_bonus += night_bonus
    total_salary += daily_salary
    
    # Tampilkan gaji hari ini (opsional)
    print(f"Gaji hari ini: Rp{daily_salary:,}")

# Tampilkan hasil akhir
print("\nHasil Akhir:")
print(f"Total jam lembur: {total_overtime_hours} jam")
print(f"Total bonus shift malam: Rp{total_night_bonus:,}")
print(f"Total gaji seminggu: Rp{total_salary:,}")
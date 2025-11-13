total_gaji = 0
total_lembur = 0
total_bonus = 0

for hari in range(1, 8):
    print(f"\n--- Hari ke-{hari} ---")
    
    while True:
        jam = int(input("Masukkan jam lembur (0–8): "))
        if 1 <= jam <= 24:
            print(f"Jam lembur yang dimasukkan: {jam}")
            break
        else:
            print("\nInput tidak valid! silahkan masukkan jam lembur (0-8)")

    if jam < 0:
        print("Jam lembur tidak boleh negatif!")
        jam = 0
    elif jam > 8:
        print("Lembur melebihi batas, tidak dihitung.")
        jam = 0

    if 1 <= jam <= 3:
        upah_lembur = 25000 * jam
    elif jam == 4:
        upah_lembur = 100000
    elif jam == 5:
        upah_lembur = 150000
    elif jam == 6:
        upah_lembur = 200000
    elif jam == 7:
        upah_lembur = 250000
    elif jam == 8:
        upah_lembur = 300000
    else:
        jam >= 9
        upah_lembur = 300000

    total_lembur += jam

    while True:
        shift = input("Shift malam? (y/n): ").lower()
        if shift in ('y', 'n'):
            break
        print("Input salah, silakan coba lagi (y/n).")

    bonus = 50000 if shift == "y" else 0
    total_bonus += bonus

    gaji_harian = 100000 + upah_lembur + bonus
    total_gaji += gaji_harian

    print(f"Gaji hari ke-{hari}: Rp {gaji_harian:,.0f}")

print("\n=== HASIL AKHIR ===")
print(f"Total jam lembur    : {total_lembur} jam")
print(f"Total bonus shift   : Rp {total_bonus:,.0f}")
print(f"Total gaji seminggu : Rp {total_gaji:,.0f}")

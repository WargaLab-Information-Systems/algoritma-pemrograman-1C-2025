total_lembur = 0
total_bonus_shift_malam = 0
total_gaji = 0

def hitung_gaji_lembur(jam):
    if jam == 0:
        return 0
    elif 1 <= jam <= 3:
        return 25000 * jam
    elif jam == 4:
        return 100000
    elif jam == 5:
        # Jika 5 jam, hitung sebagai 4 jam + 1 jam lembur biasa
        return 100000 + 25000
    elif jam == 6:
        return 200000
    elif jam == 7:
        # Jika 7 jam, hitung sebagai 6 jam + 1 jam lembur biasa
        return 200000 + 25000
    elif jam == 8:
        return 300000

def is_valid_jam_lembur(jam_input):
    return jam_input.isdigit() and 1 <= int(jam_input) <= 8

for hari in range(1, 8):
    print(f"Hari ke-{hari}:")
    jam_lembur_input = input("Masukkan jumlah jam lembur (0-8): ")
    while not (jam_lembur_input.isdigit() and 0 <= int(jam_lembur_input) <= 8):
        print("Jam lembur harus angka antara 0 sampai 8. Coba lagi.")
        jam_lembur_input = input("Masukkan jumlah jam lembur (0-8): ")
    jam_lembur = int(jam_lembur_input)

    shift_malam = input("Apakah shift malam? (y/n): ").strip().lower()
    while shift_malam not in ['y', 'n']:
        print("Input tidak valid, masukkan 'y' atau 'n'.")
        shift_malam = input("Apakah shift malam? (y/n): ").strip().lower()

    gaji_pokok = 100000
    gaji_lembur = hitung_gaji_lembur(jam_lembur)

    bonus_shift = 50000 if shift_malam == 'y' else 0

    total_lembur += jam_lembur
    total_bonus_shift_malam += bonus_shift
    total_gaji += gaji_pokok + gaji_lembur + bonus_shift

print("\n--- Rekap Gaji Mingguan Pak Wowo ---")
print(f"Total jam lembur: {total_lembur} jam")
print(f"Total bonus shift malam: Rp{total_bonus_shift_malam:,}")
print(f"Total gaji minggu ini: Rp{total_gaji:,}")

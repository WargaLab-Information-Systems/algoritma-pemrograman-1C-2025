total_gaji = 0
total_lembur = 0
total_bonus = 0

for i in range(1, 8):
    print("Hari ke-", i)

    while True:
        jam_input = input("Masukkan jam lembur: ")

        if jam_input.isalpha():
            print("Input tidak valid! Masukkan angka, bukan huruf.")
            continue

        if "-" in jam_input:
            print("Input tidak valid! Tidak boleh negatif.")
            continue

        if jam_input.isdigit():
            jam = int(jam_input)
            break

    if jam > 8:
        print("Lembur melebihi batas, tidak dihitung.")

    if jam >=1 and jam <=3:
        gaji_lembur = jam * 25000
    elif jam == 4:
        gaji_lembur = 100000
    elif jam == 5:
        gaji_lembur = 150000         
    elif jam == 6:
        gaji_lembur = 200000
    elif jam == 7:
        gaji_lembur = 250000          
    elif jam == 8:
        gaji_lembur = 300000
    else:
        gaji_lembur = 300000

    while True:
        shift = input("Apakah shift malam? (y/n): ")
        if shift == "y" or shift == "Y" or shift == "n" or shift == "N":
            break
        else:
            print("Input tidak valid! Harus 'y' atau 'n'.")

    if shift == "y" or shift == "Y":
        bonus = 50000
    else:
        bonus = 0

    total_lembur = total_lembur + jam
    total_bonus = total_bonus + bonus
    total_gaji = total_gaji + 100000 + gaji_lembur + bonus

print("\n")
print("Total jam lembur:", total_lembur)
print("Total bonus shift malam: Rp", total_bonus)
print("Total gaji seminggu: Rp", total_gaji)

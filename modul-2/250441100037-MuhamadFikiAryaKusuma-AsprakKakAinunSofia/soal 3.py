# Program menghitung biaya parkir di mall
lama_parkir = int(input("Masukkan berapa lama parkir (jam): "))
status_vip = input("Apakah kamu member VIP? (iya/tidak): ").lower()

if status_vip == "iya":
    biaya = 0
else:
    if lama_parkir <= 2:
        biaya = 5000
    else:
        biaya = 5000 + (lama_parkir - 2) * 3000

    if biaya > 20000:
        biaya = 20000

# hasil perhitunganya
print(f"Lama kamu berparkir : {lama_parkir} jam")
print(f"Status VIP   : {status_vip}")
print(f"Total biaya parkir : Rp {biaya:,}")
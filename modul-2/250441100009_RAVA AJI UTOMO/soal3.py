# Input lama parkir
lama_parkir = int(input("Masukkan lama parkir (jam): "))
if lama_parkir < 0:
    lama_parkir = 0
# Input status VIP
status_vip = input("Status VIP (ya/tidak): ")
# Hitung total biaya
if status_vip == "ya":
    total = 0
else:
    if lama_parkir <= 2:
        total = 5000
    else:
        total = 5000 + (lama_parkir - 2) * 3000 
        if total > 20000:
            total = 20000
# Output total biaya
print("Total biaya parkir: Rp", total)
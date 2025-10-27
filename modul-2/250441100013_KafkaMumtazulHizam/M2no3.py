lama = int(input("Berapa jam anda akan parkir: "))
vip = input("Apakah kamu member VIP? (ya/tidak): ")

if vip == "ya":
    total = 0
else:
    if lama <= 2:
        total = 5000
    elif lama <= 7:
        total = 5000 + (lama - 2) * 3000
    else:
        total = 20000

print(f"Total biaya parkir: Rp{total}")
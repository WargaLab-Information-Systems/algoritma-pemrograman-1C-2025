jam = int(input("Masukkan lama parkir (jam): "))
vip = input("Apakah Anda member VIP? (ya/tidak): ").lower()

if vip == "ya":
    total = 0
else:
    if jam <= 2:
        total = 5000
    elif jam <= 24:
        total = 5000 + ((jam - 2) * 3000)
        if total > 20000:
            total = 20000
    else:
       
        hari = jam // 24
        sjam = jam % 24

        
        total = (hari * 20000) + (sjam * 3000)

print(f"Total biaya parkir: Rp {total}")
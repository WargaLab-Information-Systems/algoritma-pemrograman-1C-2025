waktu = int(input("Masukkan lama parkir (waktu): "))
langganan = input("Apakah Anda member langganan? (ya/tidak): ").lower()

if langganan == "ya":
    total = 0
else:
    if waktu <= 2:
        total = 5000
    else:
        total = 5000 + (waktu - 2) * 3000

    if total > 20000:
        total = 20000
        total = 40000


print(f"Total akhir parkir: Rp{total}")
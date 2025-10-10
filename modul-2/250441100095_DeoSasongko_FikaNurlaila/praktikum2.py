harga = 50000

umur = int(input("Masukkan usia: "))
siswa = input("Apa sma ada kartu pelajar? (ya/tidak): ").lower()
hari = input("Hari apa sekarang? ").lower()

diskon = 0

if umur < 12:
    diskon = 50
elif siswa == "ya":
    diskon = 30
elif hari == "selasa":
    diskon = 20

total = harga - (harga * diskon / 100)

print(f"Diskon yang diperoleh: {diskon}%")
print(f"Total yang harus dibayar: Rp{int(total)}")



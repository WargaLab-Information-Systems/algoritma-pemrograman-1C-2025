harga_tiket = 50000

usia = int(input("Masukkan usia Anda: "))
status_pelajar = input("Apakah Anda pelajar SMA? (ya/tidak): ").lower()
hari = input("Masukkan hari : ").lower()

diskon = 0

if usia < 12:
    diskon += 50
if status_pelajar == "ya":
    diskon += 30
if hari == "selasa":
    diskon += 20

if diskon > 100:
    diskon = 100

harga_diskon = harga_tiket - (harga_tiket * diskon / 100)

print(f"Diskon yang didapat: {diskon}%")
print(f"Harga yang harus dibayar: Rp{int(harga_diskon)}")
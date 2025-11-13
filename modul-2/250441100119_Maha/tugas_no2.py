umur = int(input("masukkan umur: "))
pelajar = input("apakah anda pelajar SMA (ya/tidak)? ").lower()
hari = input("hari apa sekarang? ").lower()

harga_tiket = 50000
diskon = 0

if umur < 3:
    harga_terakhir = 0
    print("Anak di bawah 3 tahun gratis masuk!")
else:
    if umur < 12:
        diskon = max(diskon, 50)
    if pelajar == "ya":
        diskon = max(diskon, 30)
    if hari == "selasa":
        diskon = max(diskon, 20)

    harga_terakhir = harga_tiket - (harga_tiket * diskon / 100)

print(f"Harga tiket normal : Rp{harga_tiket}")
print(f"Diskon yang didapat: {diskon}%")
print(f"Harga yang harus dibayar: Rp{int(harga_terakhir)}")
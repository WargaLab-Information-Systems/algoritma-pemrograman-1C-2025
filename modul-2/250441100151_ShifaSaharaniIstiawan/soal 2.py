harga_normal = 50000
usia = int(input("Masukkan usia Anda: "))
status_pelajar = input("Apakah Anda pelajar SMA dengan kartu pelajar? (ya/tidak): ")
hari = input("Masukkan hari: ")
diskon = 0
if usia < 12:
    diskon = 0.5
if usia <= 2:
    diskon = 1
elif status_pelajar == "ya":
    diskon = 0.3
elif hari == "Selasa":
    diskon = 0.2

harga_akhir = harga_normal * (1 - diskon)
print(f"Harga tiket yang harus dibayar: Rp{int(harga_akhir):,}")
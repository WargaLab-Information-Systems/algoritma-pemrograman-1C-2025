# Program menghitung harga tiket bioskop dengan diskon terbesar
usia = int(input("Masukkan usia anda: "))
status_pelajar = input("Apakah Anda pelajar SMA? (ya/tidak): ").lower()
hari = input("Masukkan hari pas nonton bioskop(misalnya: senin, selasa, rabu, ...): ").lower()


harga_normal = 50000
diskon = 0  # variabel untuk menyimpan diskon terbesar

if usia < 12 and 50 > diskon:
    diskon = 50

if status_pelajar == "ya" and 30 > diskon:
    diskon = 30

if hari == "selasa" and 20 > diskon:
    diskon = 20
if usia and status_pelajar == "ya" and hari == "selasa" :
    diskon = 50
# Menghitung harga yang akan dibayar setelah diskon
harga_akhir = harga_normal - (harga_normal * diskon / 100)

print("Harga tiket normal : Rp", str(harga_normal))
if diskon > 0:
    print("Diskon yang berlaku :", str (diskon),"%")
else:
    print("Tidak ada diskon yang berlaku.")
print("Total yang harus dibayar : Rp", int(harga_akhir))
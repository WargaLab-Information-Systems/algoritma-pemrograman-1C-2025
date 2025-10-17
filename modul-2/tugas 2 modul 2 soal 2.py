#input dari pengguna
usia = int (input("masukkan usia: "))

hari = input("Masukkan hari: ")

#tiket normal
harga_normal = 50000

#diskon
diskon = 0

#cek diskon terbesar
#1. anak-anak < 12 thn diskon 50%
if usia <= 12:
    diskon = 50
else:
    status_pelajar = input("Pelajar SMA? (ya/tidak): ")
#2. pelajar dgn kartu pelajar diskon 30%
    if status_pelajar == "ya":
        diskon = 30
#3. hari selsa diskon 20%
    else:
        if hari == "selasa":
            diskon = 20
#total harga
harga_diskon = harga_normal * (100 - diskon) / 100

print("HARGA TIKET")
print(f"harga normal: Rp {harga_normal:,}")
print(f"diskon berlaku: {diskon}%")
print(f"total akhir: Rp {harga_diskon:,}")
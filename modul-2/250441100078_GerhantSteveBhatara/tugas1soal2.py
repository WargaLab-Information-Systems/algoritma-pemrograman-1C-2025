#Soal 2
# Program menghitung harga tiket bioskop

# Harga normal
harga_tiket = 50000

# Input data dari pengguna
usia = int(input("Masukkan usia Anda: "))
status_pelajar = input("Apakah Anda pelajar SMA? (ya/tidak): ").lower()
hari = input("Masukkan hari (contoh: Senin, Selasa, Rabu, ...): ").capitalize()

# Diskon berdasarkan kondisi
diskon = 0  # persentase diskon

# Cek kondisi diskon
if usia < 12:
    diskon = 50
if status_pelajar == "ya":
    diskon = max(diskon, 30)
if hari == "Selasa":
    diskon = max(diskon, 20)

# Harga setelah diskon
harga_diskon = harga_tiket * (1 - diskon / 100)

# Tampilkan hasil
print("HASIL PERHITUNGAN :")
print(f"Hari: {hari}")
print(f"Usia: {usia}")
print(f"Pelajar SMA: {status_pelajar}")
print(f"Diskon yang didapat: {diskon}%")
print(f"Harga yang harus dibayar: Rp{harga_diskon:,.0f}")
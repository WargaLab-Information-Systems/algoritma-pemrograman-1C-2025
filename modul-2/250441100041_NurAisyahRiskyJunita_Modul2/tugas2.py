# Harga tiket normal
harga_tiket = 50000

# Input dari pengguna
usia = int(input("Masukkan usia: "))
pelajar = input("Apakah Anda pelajar SMA? (ya/tidak): ")
hari = input("Masukkan hari (contoh: Senin, Selasa, ...): ")

# Menentukan diskon
diskon = 0

if usia < 12:
    diskon = 0.5
elif pelajar == "ya":
    diskon = 0.3
elif hari == "Selasa":
    diskon = 0.2
else:
    diskon = 0

# Hitung total bayar
potongan = harga_tiket * diskon
total_bayar = harga_tiket - potongan

# Tampilkan hasil
print("\n=== RINCIAN PEMBAYARAN ===")
print("Harga tiket normal     : Rp", harga_tiket)
print("Diskon yang didapat    :", int(diskon * 100), "%")
print("Total yang harus dibayar: Rp", int(total_bayar))
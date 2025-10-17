# Program Menghitung Harga Tiket Bioskop

# Harga tiket normal
harga_tiket = 50000

# Input dari pengguna
usia = int(input("Masukkan usia: "))
pelajar = input("Apakah Anda pelajar SMA? (ya/tidak): ").lower()
kartu = input("Apakah Anda memiliki kartu pelajar? (ya/tidak): ").lower()
hari = input("Masukkan hari: ").lower()

# Tentukan diskon berdasarkan prioritas terbesar
if usia < 12:
    diskon = 0.5   # 50% untuk anak-anak
elif pelajar == "ya" and kartu == "ya":
    diskon = 0.3   # 30% untuk pelajar SMA yang memiliki kartu pelajar
elif hari == "selasa":
    diskon = 0.2   # 20% promo hari Selasa
else:
    diskon = 0     # Tidak ada diskon

# Hitung harga akhir
harga_akhir = harga_tiket - (harga_tiket * diskon)

# Tampilkan hasil
print("\n=== Hasil Perhitungan Harga Tiket ===")
print(f"Harga tiket normal      : Rp{harga_tiket}")
print(f"Diskon yang diterapkan  : {int(diskon * 100)}%")
print(f"Total yang harus dibayar: Rp{int(harga_akhir)}")

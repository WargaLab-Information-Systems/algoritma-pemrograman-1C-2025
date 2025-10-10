# Program Penentuan Harga Tiket Bioskop (Versi Sederhana)

# Input data
usia = int(input("Masukkan usia: "))
pelajar = input("Apakah Anda pelajar SMA (ya/tidak)? ")
hari = input("Masukkan hari (contoh: Senin, Selasa, Rabu): ")

# Harga dasar
harga_normal = 50000
diskon = 0

# Cek usia 0–3 tahun gratis
if usia <= 3:
    harga_bayar = 0
    diskon = 100
else:
    # Cek diskon berdasarkan kondisi lain
    if usia <= 12:
        diskon = 50

    if pelajar == "ya" or pelajar == "Ya" or pelajar == "YA":
        if diskon < 30:
            diskon = 30

    if hari == "Selasa" or hari == "selasa" or hari == "SELASA":
        if diskon < 20:
            diskon = 20

    # Hitung harga akhir
    harga_bayar = harga_normal - (harga_normal * diskon / 100)

# Output
print("\nDiskon yang didapat:", diskon, "%")
print("Harga tiket yang harus dibayar: Rp", int(harga_bayar))
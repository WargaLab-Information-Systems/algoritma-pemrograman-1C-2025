tiket_normal = 50000
diskon_usia = 0
diskon_sma = 0
diskon_hari = 0

# Input data pengguna
usia = int(input("Masukkan usia Anda: "))
hari = input("masukkan hari (senin, selasa, rabu, kamis, jumat, sabtu, minggu): ")

# Cek diskon berdasarkan usia
if usia < 12:
    diskon_usia = 0.50 * tiket_normal
elif usia > 12:
    status_pelajar_sma = input("Apakah Anda pelajar SMA ? (ya/tidak): ")
    # Cek diskon untuk pelajar SMA dengan kartu pelajar
    if status_pelajar_sma == "ya":
        kartu_pelajar = input("Apakah Anda memiliki kartu pelajar ? (ya/tidak): ")
        if kartu_pelajar == "ya":
            diskon_sma = 0.30 * tiket_normal

# Cek diskon hari Selasa
if hari == "selasa":
    diskon_hari = 0.20 * tiket_normal

# Ambil diskon terbesar
if diskon_usia >= diskon_sma and diskon_usia >= diskon_hari:
    diskon = diskon_usia
elif diskon_sma >= diskon_usia and diskon_sma >= diskon_hari:
    diskon = diskon_sma
else:
    diskon = diskon_hari
# Hitung harga tiket akhir setelah diskon
tiket_akhir = tiket_normal - diskon
print("Harga tiket akhir yang harus dibayar: Rp", tiket_akhir)
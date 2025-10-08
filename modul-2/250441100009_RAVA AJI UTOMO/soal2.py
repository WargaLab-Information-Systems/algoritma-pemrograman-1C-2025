usia = int(input("Masukkan usia: ")) # Minta input dari pengguna
if usia >= 12:
    status_pelajar = input("Apakah Anda pelajar? (ya/tidak): ")
else:
    status_pelajar = "tidak" 
hari = input("Masukkan hari: ")
# Harga tiket normal
harga = 50000
# buat Cek diskon anak (50%)
if usia < 12:
    diskon_anak = 50
else:
    diskon_anak = 0
# buat Cek diskon pelajar (30%)
if status_pelajar == "ya" and usia >= 12:
    diskon_pelajar = 30
else:
    diskon_pelajar = 0
# buat Cek diskon hari Selasa (20%)
if hari == "Selasa":
    diskon_selasa = 20
else:
    diskon_selasa = 0
# Ambil diskon yang PALING BESAR
if diskon_anak >= diskon_pelajar and diskon_anak >= diskon_selasa:
    diskon_terbesar = diskon_anak
elif diskon_pelajar >= diskon_anak and diskon_pelajar >= diskon_selasa:
    diskon_terbesar = diskon_pelajar
else:
    diskon_terbesar = diskon_selasa
# Hitung harga akhir
potongan = harga * diskon_terbesar / 100 
harga_akhir = harga - potongan
# Tampilkan hasil
print("Harga tiket: Rp", int(harga_akhir))
usia = int(input("masukkan usia anda: :"))
status_pelajar = input("Apakah anda pelajar SMA dengan kartu pelajar? (ya/tidak): ")
hari = input("masukkan hari kunjungan (misal: senin, selasa, dll): ")

diskon_anak = 0
diskon_pelajar = 0
diskon_selasa = 0

if usia < 12:
    diskon_anak = 0.50
if status_pelajar == "ya":
    diskon_pelajar = 0.30
if hari == "selasa":
    diskon_selasa = 0.20
diskon_terbesar = max(diskon_anak, diskon_pelajar, diskon_selasa)
 
harga_tiket_normal = 50000
harga_setelah_diskon = harga_tiket_normal * (1 - diskon_terbesar)

print(f"harga tiket yang harus dibayar: Rp.{int(harga_setelah_diskon)}")

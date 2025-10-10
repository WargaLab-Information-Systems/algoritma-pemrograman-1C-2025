# Harga Tiket Bioskop
harga_tiket_normal = 50000

print ("=== Harga Tiket Bioskop ===")
print ("\nHarga Tiket Normal: Rp.50000")
print ("\nList Tiket Bioskop Diskon: ")
print ("1.Diskon 50% untuk anak di bawah 12 tahun")
print ("2.Diskon 30% untuk pelajar SMA")
print ("3.Diskon 20% untuk hari selasa")

# input
usia = int(input("\nMasukkan umur anda: "))
status_pelajar = input("apakah anda pelajar SMA ? (ya/tidak): ").lower()
hari = input("Masukkan Hari anda membeli tiket bioskop: ").lower()

# diskon
diskon = 0
if usia < 12:
    diskon = 50
elif status_pelajar == "ya":
    diskon = 30
elif hari == "selasa":
    diskon = 20
else:
    diskon = 0
harga_akhir = round(harga_tiket_normal * (1 - diskon / 100))

#hasil
print ("\nHasil:")
print (f"Diskon: {diskon}%")
print (f"Harga Tiket Bioskop: Rp. {harga_akhir: }")
print ("\n===TERIMA KASIH===")
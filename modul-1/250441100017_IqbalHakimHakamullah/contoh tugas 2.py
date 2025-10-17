# Tarif dasar
tarif = {
    "mobil pribadi": 15000,
    "truk kecil": 25000,
    "truk besar": 40000
}

# Input dari user
kendaraan = input("Masukkan jenis kendaraan (mobil pribadi/truk kecil/truk besar): ")
pembayaran = input("Masukkan metode pembayaran (tunai/e-money): ")
jam = int(input("Masukkan jam keberangkatan (0-23): "))


# Tarif dasar
tarif_dasar = tarif[kendaraan]
print(f"Tarif dasar untuk {kendaraan}: Rp {tarif_dasar:,}")

# Hitung diskon
diskon = 0
if pembayaran == "e-money":
    diskon = 10
    if 23 <= jam or jam <= 5:  # Jam sepi: 23:00 - 05:00
        diskon = 20
    print(f"Diskon {diskon}% (e-money + jam sepi)")
else:
    print("Tidak ada diskon (pembayaran tunai)")

# Hitung total
total = tarif_dasar * (1 - diskon / 100)
print(f"Total yang harus dibayar: Rp {int(total):,}")
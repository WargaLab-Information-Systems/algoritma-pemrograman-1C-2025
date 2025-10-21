matic = "50000"
trail = "100000"
sport = "75000"
asuransi = "15000"
diskon = "0.10"
diskon_tambahan = "0.05"
semua_diskon = "0.15"
total_harga = 0
kupon = "AconkGG"
print("==== List Harga Sewa ====")
print(f"1. Motor Matic: Rp.{matic}")
print(f"2. Motor Trail: Rp.{trail}")
print(f"3. Motor Sport: Rp.{sport}")

ulang = "y"
while True:
    motor =input("Pilih motor yang mau disewa: ")
    hari = int(input("Berapa hari anda akan menyewa: "))
    if matic:
        total_harga = motor * hari
        print(f"Harga Sewa: Rp.{total_harga}")
    elif trail:
        total_harga = int(motor) * int(hari)
        print(f"Harga Sewa: Rp.{total_harga}")
    elif sport:
        total_harga = motor * hari
        print(f"Harga Sewa: Rp.{total_harga}")
    

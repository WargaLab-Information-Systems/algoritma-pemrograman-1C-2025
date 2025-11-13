# motormatic = 50000
# motortrail = 100000
# motorsport = 75000
# asuransi = 15000
# hari = 3
# diskon = 0.10
# diskonkupon = 0.5
# kupon = "AconkGG"

# kendaraan = input("Masukkan jenis kendaraan : ")
# sewa = int(input("Masukkan lama sewa : "))

# if sewa >= hari :
#     kendaraan == "motor matic"  
#     jml1 = motormatic - asuransi
#     print(f"Mendapat asuransi : {jml1}")
#     total = diskon * jml1
#     print(f"Total : {total}")
# elif sewa >= hari :
#     kendaraan == "motor trail"
#     jml2 = motortrail - asuransi
#     subtotal = diskon * jml2
#     print(f"Mendapat asuransi : {jml2}")
# elif sewa >= hari :
#     kendaraan == "motor sport"
#     jml3 = motorsport - asuransi
#     subtotal = diskon * jml3
#     print(f"Mendapat asuransi : {jml3}")
# else :
#     print("Tidak ada asuransi!")


while True:
    print("\n=== RENTAL MOTOR ACONK ===")
    print("1. Motor Matic  = Rp 50.000/hari")
    print("2. Motor Trail  = Rp 100.000/hari")
    print("3. Motor Sport  = Rp 75.000/hari")

    pilih = input("Pilih motor (1/2/3): ")

    if pilih == "1":
        harga = 50000
        jenis = "Matic"
    elif pilih == "2":
        harga = 100000
        jenis = "Trail"
    elif pilih == "3":
        harga = 75000
        jenis = "Sport"
    else:
        print("Pilihan tidak valid!")
        continue

    lama = int(input("Lama sewa (hari): "))
    subtotal = harga * lama

    # Asuransi 15.000 per 3 hari (kelipatan)
    asuransi = 0
    if lama > 3:
        asuransi = (lama // 3) * 15000

    total = subtotal + asuransi

    # Diskon 10% jika subtotal > 150.000
    if subtotal > 150000:
        total -= total * 0.10

    # Diskon tambahan 5% jika kupon AconkGG
    kupon = input("Masukkan kupon (jika ada): ")
    if kupon == "AconkGG":
        total -= total * 0.05

    print("\n=== STRUK PEMBAYARAN ===")
    print(f"Jenis Motor     : {jenis}")
    print(f"Lama Sewa       : {lama} hari")
    print(f"Subtotal        : Rp{subtotal:,}")
    print(f"Asuransi        : Rp{asuransi:,}")
    print(f"Total Bayar     : Rp{int(total):,}")

    ulang = input("\nSewa lagi? (y/n): ")
    if ulang != 'y' and ulang != 'Y':
        print("Terima kasih telah menyewa di Rental Motor Aconk!")
        break

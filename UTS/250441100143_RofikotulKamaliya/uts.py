# Program Rental Motor
motor_matic = 50000
motor_trail = 100000
motor_sport = 75000
asuransi = 15000
diskon_subtotal = 0.10
diskon_kupon = 0.05

while True:
    penyewaan_motor = input("anda ingin menyewa motor apa?: ")
    lama_penyewaan = input("Berapa hari anda ingin menyewa motor tersebut?: ")
    total = penyewaan_motor
    if lama_penyewaan > 3:
        asuransi = lama_penyewaan*5000
        total_pembayaran = total + asuransi
    if total_pembayaran > 150000 :
        diskon = float(total_pembayaran * 0.10)
        kupon = input("Apakah anda memilik kupon? ")
    if kupon == "iya":
        nama_kupon = input("Masukkan nama kupon anda: ")
    if nama_kupon == "AconkGG":
        total_pembarayaran = asuransi
        subtotal = float(total_penyewaan * 0.05)
        print("Selamat Anda mendapatkan diskon tambahan sebesar 5%")
    else:
        print("mohon maaf nama kupon anda tidak termasuk dalam diskon tambahan kami.")
        print("Subtotal penyewaan anda sebesar: Rp{subtotal}") 
    jawaban = input("Apakah masih ada yang ingin menyewa motor(y/n)?: ")
    if jawaban == 'n' :
        break

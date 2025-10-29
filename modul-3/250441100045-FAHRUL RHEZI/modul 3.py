#1
n = int(input("Masukkan nilai n: "))

for i in range(2, n + 1):
    prima = True
    for h in range(2, i):
        if i % h == 0:
            prima = False
            break
    if prima:
        print(i, end=" ")
print("\n")

#2
pin_benar = 25045
kesempatan = 3
while kesempatan > 0:
    pin = input("Masukkan PIN Anda (5 digit): ")
    if not pin.isdigit() or len(pin) != 5:
        kesempatan -= 1
        print("PIN harus berupa 5 digit angka.")
        if kesempatan == 0:
            print("Akses ditolak, kartu diblokir.")
        continue
    pin_int = int(pin)
    if pin_int == pin_benar:
        print("PIN benar, akses diterima.\n")
        break
    else:
        kesempatan -= 1
        print("PIN salah, coba lagi.")
        if kesempatan == 0:
            print("Akses ditolak, kartu diblokir.")
            break

#3
kalimat = input("Masukkan sebuah kalimat: ")
vokal = 0
konsonan = 0

for huruf in kalimat:
    if huruf.lower() in "aiueo":
        vokal += 1
    elif huruf.isalpha():
        konsonan += 1

jumlah_kata = len(kalimat.split())

print(f"Jumlah huruf vokal: {vokal}")
print(f"Jumlah huruf konsonan: {konsonan}")
print(f"Jumlah kata: {jumlah_kata}")

#4
ulang = "y"
while ulang.lower() == "y":
    print("\n=== Program Struk Pembelian IndoMei ===")
    nama = input("Masukkan nama pembeli: ")
    print("\nMasukkan daftar barang yang dibeli:")
    print("(Ketik '0' pada nama barang jika sudah selesai)\n")
    
    total = 0
    nomor = 1
    daftar_barang = []
    daftar_harga = []
    while True:
        barang = input(f"Nama barang ke-{nomor}: ")
        if barang == "0":
            break
        harga = int(input("Harga barang: "))
        daftar_barang.append(barang)
        daftar_harga.append(harga)
        total += harga
        nomor += 1

    print("\n========== STRUK PEMBELIAN ==========")
    print(f"Nama Pembeli : {nama}")
    print("------------------------------------")
    for i in range(len(daftar_barang)):
        print(f"{i+1}. {daftar_barang[i]} - Rp{daftar_harga[i]:,.2f}")
    print("------------------------------------")
    print(f"Total Harga  : Rp{total:,.2f}")
    print("====================================")
    print("Terima kasih telah berbelanja di IndoMei.")
    print("====================================\n")
    ulang = input("Apakah ada pembeli berikutnya? (y/n): ")
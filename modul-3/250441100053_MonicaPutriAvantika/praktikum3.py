#TUGAS1

# Program menampilkan bilangan prima dari 1 sampai n

n = int(input("Masukkan nilai n: "))

print(f"Bilangan prima dari 1 sampai {n} adalah:")

for i in range(2, n + 1):  # dimulai dari 2 karena 1 bukan bilangan prima
    prima = True
    for j in range(2, int(i ** 0.5) + 1):  # cukup cek sampai akar i
        if i % j == 0:
            prima = False
            break
    if prima:
        print(i, end=" ")

TUGAS2

Program simulasi sederhana mesin ATM

Misal NIM kamu: 25053
Maka PIN = 25 053 -> ambil 2 NIM awal (25) + 3 NIM terakhir (053) = 25053
Kamu bisa ubah sesuai kebutuhan
PIN_BENAR = 25053

kesempatan = 3 

for i in range(kesempatan):
    try:
        pin = int(input("Masukkan PIN (5 digit): "))

        if len(str(pin)) != 5:
            print("PIN harus 5 digit!")
            continue

        if pin == PIN_BENAR:
            print("PIN benar, akses diterima ")
            break
        else:
            print("PIN salah, coba lagi ")

    except ValueError:
        print("Input harus berupa angka!")

else:
    print("Akses ditolak, kartu diblokir ")

TUGAS3

 # Program analisa kalimat

# Input kalimat dari pengguna
kalimat = input("Masukkan sebuah kalimat: ")

# Daftar huruf vokal
vokal = "aiueoAIUEO"

# Variabel penghitung
jumlah_vokal = 0
jumlah_konsonan = 0
jumlah_kata = 1  # mulai dari 1 karena kata dipisahkan oleh spasi

# Hitung jumlah huruf vokal dan konsonan
for huruf in kalimat:
    if huruf in vokal:
        jumlah_vokal = jumlah_vokal + 1
    elif huruf == " ":
        jumlah_kata = jumlah_kata + 1
    elif huruf.isalpha():  # hanya huruf (abaikan angka/tanda baca)
        jumlah_konsonan = jumlah_konsonan + 1

# Tampilkan hasil analisa
print("\n=== HASIL ANALISA KALIMAT ===")
print("Kalimat:", kalimat)
print("Jumlah huruf vokal   :", jumlah_vokal)
print("Jumlah huruf konsonan:", jumlah_konsonan)
print("Jumlah kata          :", jumlah_kata)


#TUGAS4

print("=== Program Struk Pembelian IndoMei ===")

while True:
    # Input nama pembeli
    nama = input("Masukkan nama pembeli: ")

    # Inisialisasi daftar barang dan total harga
    daftar_barang = []
    total = 0

    # Input daftar barang
    while True:
        barang = input("Masukkan nama barang (ketik 'selesai' untuk berhenti): ")
        if barang == "selesai":
            break
        harga = float(input(f"Masukkan harga {barang}: Rp "))
        daftar_barang.append((barang, harga))
        total += harga

    # Tampilkan struk pembelian
    print("==============================")
    print("        STRUK PEMBELIAN       ")
    print("==============================")
    print(f"Nama Pembeli : {nama}")
    print("------------------------------")
    print("Daftar Barang:")
    for item, harga in daftar_barang:
        print(f"- {item:15} Rp{harga:,.0f}")
    print("------------------------------")
    print(f"Total Harga   : Rp{total:,.0f}")
    print("==============================")
    print("Terima kasih telah berbelanja di IndoMei!")
    print("==============================\n")

    # Pertanyaan untuk pembeli berikutnya
    lagi = input("Apakah ada pembeli berikutnya? (y/n): ")
    if lagi != 'y':
        print("Program selesai. Semua transaksi telah dicetak.")
        break

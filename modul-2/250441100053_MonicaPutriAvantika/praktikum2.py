#TUGAS1
print("masukkan jumlah nilai mahasiswa(0-100)")
nilai = int(input())
print("nilai = " + str(nilai))
if nilai >= 85:
    print("A")
    print("masukkan jumlah persen kehadiran")
    kehadiran = int(input())
    print("kehadiran = " + str(kehadiran) + "%")
    if kehadiran >= 90:
        print("Lulus dengan Pujian")
else:
    if nilai >= 70:
        print("B")
    else:
        if nilai >= 60:
            print("C")
        else:
            if nilai >= 50:
                print("D")
            else:
                print("E")

#TUGAS2

# Program menghitung harga tiket bioskop 

# Input data
usia = int(input("Masukkan usia :"))
pelajar = input("apakah kamu pelajar sma dengan kartu pelajar? (ya/tidak):")
hari = input("sekarang hari apa :")

# Harga tiket normal
harga_normal = 50000
diskon = 0

# Cek kondisi diskon
if usia < 12:
    diskon = 50
elif pelajar == "ya":
    diskon = 30
elif hari == "selasa":
    diskon = 20
else:
    diskon = 0

# Hitung harga akhir
harga_akhir = harga_normal - (harga_normal * diskon/100) 

# Tampilkan hasil
print("Hasil Perhitungan")
print("Usia:", usia)
print("Pelajar:", pelajar)
print("Hari:", hari)
print("Diskon:", diskon, "%")
print("Harga yang harus dibayarkan:Rp", int(harga_akhir))

#TUGAS3
# Program Perhitungan Tarif Parkir Mall

# Input data dari pengguna
lama_parkir = int(input("Masukkan lama parkir (jam): "))
vip = input("apakah anda member vip? (ya/tidak): ")

# Cek status VIP
if vip == "ya":
    biaya = 0   # Jika VIP gratis
else:
    # Hitung biaya parkir biasa
    if lama_parkir <= 2:
        biaya = 5000  # 2 jam pertama Rp5000
    else:
        biaya = 5000 + (lama_parkir - 2) * 3000  # Tambahan Rp3000 per jam setelah 2 jam 

    # Cek batas maksimal
    if biaya > 20000:
        biaya = 20000  # Maksimal Rp20.000 per hari

# Tampilkan hasil
print("Hasil Perhitungan Parkir")
print(f"Lama parkir       : {lama_parkir} jam")
print(f"Status VIP        : {'Ya' if vip == 'ya' else 'Tidak'}")
print(f"Total biaya parkir: Rp{biaya}")


#Soal 1
print("masukkan nilai ujian : ")
nu = int(input())
print("masukkan persentase kehadiran : ")
kehadiran = int(input())
print("kehadiran : " + str(kehadiran) + "%")
if nu >= 85:
    print("nilai : " + str(nu) + ". nilai : A")
    if kehadiran >= 90:
        print("lulus dengan pujian")
    else:
        print("lulus")
else:
    if nu >= 70:
        print("nilai : " + str(nu) + ". nilai : B")
        print("lulus")
    else:
        if nu >= 60:
            print("nilai : " + str(nu) + ". nilai : C")
            print("lulus")
        else:
            if nu >= 50:
                print("nilai : " + str(nu) + ". nilai : D")
            else:
                print("nilai : " + str(nu) + ". nilai : E")
            print("tidak lulus")
            
#soal 2
print("\nHarga tiket normal: Rp 50.000")
print("List diskon:")
print("1. Diskon 50% untuk anak di bawah 12 tahun")
print("2. Diskon 30% untuk pelajar SMA")
print("3. Diskon 20% untuk hari Selasa")

usia = int(input("Berapa usia anda: "))
pljr = input("Apakah Anda pelajar SMA? (ya/tidak): ")
h = input("Masukkan hari anda membeli tiket: ")
hn = 50000
diskon = 0

if usia < 12:
    diskon = max(diskon, 50)
if pljr == "ya":
    diskon = max(diskon, 30)
if h == "selasa":
    diskon = max(diskon, 20)

jb = hn - (hn * diskon / 100)

print(f"\nDiskon yang diperoleh: {diskon}%")
print(f"Harga yang harus dibayar: Rp{int(jb)}")

#soal 3
print("\nTarif parkir mall:")
print("1. 2 jam pertama: Rp 5.000")
print("2. Setiap jam berikutnya: Rp 3.000") 
print("3. Maksimal biaya parkir: Rp 20.000")
print("4. Member VIP: Gratis parkir")

dp = int(input("Masukkan lama parkir (jam): "))
vip = input("Apakah Anda member VIP? (ya/tidak): ")

if vip == "ya":
    total = 0
else:
    if dp <= 2:
        total = 5000
    elif dp <= 7:
        total = 5000 + (dp - 2) * 3000
    else:
        total = 20000

print(f"\nTotal biaya parkir: Rp{total}")
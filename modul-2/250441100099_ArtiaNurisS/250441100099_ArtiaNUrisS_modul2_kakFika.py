# #===no1===
print("masukkan nilai")
n = int(input())
print("masukkan kehadiran 1-100")
pk = int(input())
if n >= 85 and pk >= 90:
    print("sealamat anda lulus dengan pujian, dengan nilai A")
else:
    if n >= 85:
        print("selamat anda lulus dengan nilai A")
    else:
        if n >= 70 and n < 85:
            print("anda lulus dengan nilai B")
        else:
            if n >= 60 and n < 70:
                print("anda lulus dengan nilai C")
            else:
                if n >= 50 and n < 60:
                    print("coba lagi, karena nilai anda D")
                else:
                    if n < 59:
                        print("coba lagi, karena nilai anda E")
                    else:
                        print("apaya")

# ===no2===
harga_normal = 50000

umur = int(input("masukkan umur: "))
pelajar = input("Apakah pelajar SMA dengan kartu pelajar? (ya/tidak): ")
hari = input("Hari apakah kamu kesana?: ")

if umur < 12:
    diskon = 50
elif pelajar == "ya" :
    diskon = 30
elif hari == "selasa":
    diskon = 20
else :
    diskon = 0
    
harga_bayar = harga_normal - (harga_normal * diskon/ 100)

print("diskon", diskon, "%")
print("harga tiket yang harus dibayar adalah : Rp", int(harga_bayar))
 
    
# #===no3===
lama = int(input("Berapa jam anda akan parkir: "))
vip = input("Apakah kamu member VIP? (ya/tidak): ")

if vip == "ya":
    total = 0
else:
    if lama <= 2:
        total = 5000
    elif lama <= 7:
        total = 5000 + (lama - 2) * 3000
    else:
        total = 20000

print(f"Total biaya parkir: Rp{total}")                       


# =====challange=====

# #===no1===
print("masukkan nilai")
n = int(input())
print("masukkan kehadiran 1-100")
pk = int(input())
if n == -1 or pk == -1:
    print("Tidak valid")
if n >= 85 and pk >= 90:
    print("sealamat anda lulus dengan pujian, dengan nilai A")
else:
    if n >= 85:
        print("selamat anda lulus dengan nilai A")
    else:
        if n >= 70 and n < 85:
            print("anda lulus dengan nilai B")
        else:
            if n >= 60 and n < 70:
                print("anda lulus dengan nilai C")
            else:
                if n >= 50 and n < 60:
                    print("coba lagi, karena nilai anda D")
                else:
                    if n < 59:
                        print("coba lagi, karena nilai anda E")
                    else:
                        print("apaya")

# #===no2===
harga_tiket = 50000

usia = int(input("Masukkan usia Anda: "))
status_pelajar = input("Apakah Anda pelajar SMA? (ya/tidak): ").lower()
hari = input("Masukkan hari : ").lower()

diskon = 0

if usia < 12:
    diskon += 50
if status_pelajar == "ya":
    diskon += 30
if hari == "selasa":
    diskon += 20

if diskon > 100:
    diskon = 100

harga_diskon = harga_tiket - (harga_tiket * diskon / 100)

print(f"Diskon yang didapat: {diskon}%")
print(f"Harga yang harus dibayar: Rp{int(harga_diskon)}")
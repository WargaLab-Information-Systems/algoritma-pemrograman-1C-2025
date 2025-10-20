tiket_normal = 50000
#kategori usia
print("kategori usia penonton:")
print("1.dewasa")
print("2.anak-anak")
dewasa = (">12 tahun")
anak_anak = ("<12 tahun")
hari = ("rabu")
pilih = int (input("kategori usia penonton: "))
if pilih ==  2:
     print("anak_anak")
     print("diskon 50%")
     print(f"{tiket_normal} * 0.5")
     print("total bayar:", tiket_normal - 25000 )
else :
     print("Tidak mendapatkan diskon")
dengan = ("iya")
tanpa = ("tidak") 
print("1.pelajar sma dengan kartu pelajar")
print("2.pelajar sma tanpa kartu pelajar")   
pilih = int (input("status pelajar: "))     
if pilih == 1:
    print("dengan")
    print("diskon 30%")
    print(f"{tiket_normal} * 0.3")
    print("total bayar:", tiket_normal - 15000 )
else :
    print("tidak mendapatkan diskon")       
pilih = str (input("hari kunjungan: ")) 
promo = ("selasa_spesial")
if pilih == "selasa" : 
    print("promo")
    print("diskon 20%")
    print(f"{tiket_normal} * 0.2")
    print("total bayar:", tiket_normal - 10000 )
else :
    print("Maaf anda tidak mendapatkan diskon")    
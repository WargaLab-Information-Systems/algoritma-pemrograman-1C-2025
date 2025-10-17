harga_tiket = 50000
diskon = 0

umur = int(input("Masukkan umur anda: "))
status_pelajar = input("Apakah anda pelajar/mahasiswa? (ya/tidak): ")
hari = input("Hari apa anda membeli tiket?: ")
if umur == 1:
    diskon = 0 
    harga_tiket = 0
    print ("karena umur anda 1 tahun, tiket gratis.")
    print (f"Diskon anda sebesar: {diskon}%")
    print (f"harga tiket yang harus dibayar : Rp {harga_tiket}")
    

elif  umur < 12:
    diskon = 0.5
    total = harga_tiket - (harga_tiket * diskon / 100)
    print (f"Diskon anda sebesar: {diskon*100}%")
    print (f"Harga tiket yang harus dibayar: Rp {int(harga_tiket - (harga_tiket*diskon))}")
elif status_pelajar == "ya":
    diskon = 0.3
    print (f"Diskon anda sebesar: {diskon*100}%")
    print (f"Harga tiket yang harus dibayar: Rp {int(harga_tiket - (harga_tiket*diskon))}")
elif hari == "selasa":
    diskon = 0.2
    print (f"Diskon anda sebesar: {diskon*100}%")
    print (f"Harga tiket yang harus dibayar: Rp {int(harga_tiket - (harga_tiket*diskon))}")
else:
    print ("Anda tidak mendapatkan diskon")
    print (f"Harga tiket yang harus dibayar: Rp {harga_tiket}")
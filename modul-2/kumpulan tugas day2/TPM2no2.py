
h_tiket = 50000

u = int(input("Masukkan umur anda: "))
sp = input("Apakah anda pelajar/mahasiswa? (ya/tidak): ")
h = input("Hari apa anda membeli tiket?: ")

if  u < 12:
    diskon = 0.5
    print (f"Diskon anda sebesar: {diskon*100}%")
    print (f"Harga tiket yang harus dibayar: Rp {h_tiket - (h_tiket*diskon):.0f}")
elif sp == "ya":
    diskon = 0.3
    print (f"Diskon anda sebesar: {diskon*100}%")
    print (f"Harga tiket yang harus dibayar: Rp {h_tiket - (h_tiket*diskon):.0f}")
elif h == "selasa":
    diskon = 0.2
    print (f"Diskon anda sebesar: {diskon*100}%")
    print (f"Harga tiket yang harus dibayar: Rp {h_tiket - (h_tiket*diskon):.0f}")
else:
    print ("Anda tidak mendapatkan diskon")
    print (f"Harga tiket yang harus dibayar: Rp {h_tiket:.0f}")
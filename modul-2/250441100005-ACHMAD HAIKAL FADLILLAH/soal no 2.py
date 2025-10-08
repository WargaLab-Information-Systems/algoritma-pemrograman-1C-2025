tiket = 50000
usia = int (input ("masukkan usia: "))
if usia < 12 :
   hari = str (input ("masukkan hari: "))
   diskonusia = tiket * 50/100
   print("diambil diskon terbesar")
   print("diskon 50%, harga tiket menjadi ", tiket - diskonusia)
elif usia >= 12 :
   pelajar = str (input ("status pelajar SMA dengan kartu pelajar (ya/bukan): "))
   hari = str (input ("masukkan hari: "))
   print("usia anda sudah mencapai 12 tahun atau lebih")
   if pelajar == "ya" :
      diskonsma = tiket * 30/100
      print("diambil diskon terbesar")
      print("diskon 30%, harga tikrt menjadi ", tiket - diskonsma)
   elif pelajar == "bukan" :
      print("anda tidak membawa kartu pelajar atau bukan pelajar SMA")
      if hari == "selasa" :
         diskonhari = tiket * 20/100
         print("diskon 20%, harga tiket menjadi ", tiket - diskonhari)
      elif hari == "senin" or "rabu" or "kamis" or "jumat" or "sabtu" or "minggu" :
         print("tidak ada diskon, harga tetap ", tiket)
      else:
         print("tidak valid, mohon masukkan nama hari")

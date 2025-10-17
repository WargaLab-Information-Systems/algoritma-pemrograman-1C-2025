tarif = 5000
berikutnya = 3000
jam = float (input ("berapa jam anda parkir: "))
vip = str (input ("anda termasuk member VIP (ya/bukan): "))
if vip == "ya" :
   print("parkir anda gratis")
elif vip == "bukan" :
   if jam < 0 :
      print("tidak valid, masukkan angka lebih dari 0")
   elif jam <= 2 :
      print("harga parkir anda Rp", tarif)
   elif jam == 3 :
      print("harga parkir anda Rp", tarif + berikutnya)
   elif jam == 4 :
      print("harga parkir anda Rp", tarif + berikutnya * 2)
   elif jam == 5 :
      print("harga parkir anda Rp", tarif + berikutnya * 3)
   elif jam == 6 :
      print("harga parkir anda Rp", tarif + berikutnya * 4)
   elif jam >= 7 and jam <= 24 :
      print("harga parkir anda Rp", tarif + berikutnya * 5)
   else:
      print("kembali ke satu jam pertama")
else:
   print("data tidak valid")
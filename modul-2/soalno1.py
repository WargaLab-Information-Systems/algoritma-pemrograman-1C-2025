nama = input ("Masukkan nama: ")
print("nama")
nilai= int (input ("Masukkan nilai: "))
if nilai  >= 85 :
    print ("A")
    kehadiran = int (input("Masukkan presensi kehadiran: "))
    if kehadiran >= 90 :
        print ("Selamat anda lulus dengan pujian!")
    else :
        print ("Tetap Semangat! coba lagi")    
elif nilai >= 70 :
    print ("B")
elif nilai >= 60 :
    print ("C")
elif nilai >= 50 :
    print ("D")        
elif nilai <= 50 :
    print ("E")

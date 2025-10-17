print("masukkan nilai :")
nilai = int(input())
if nilai >= 85:
    print("mendapatkan nilai A")
    print("masukkan presentase kehadiran)")
    kehadiran = int (input ())
    if kehadiran >= 90:
        print("lulus dengan tujuan")
    else:
        print("lulus")
else:
    if nilai <= 70 and nilai <= 84:
        print("mendapatkan nilai B")
        print("masukkan presentase kehadiran")
        kehadiran = int(input())
        if kehadiran >= 90:
            print("lulus dengan pajak")
        else:
            print("lulus")
    else:
        if nilai >= 60 and niallai <= 69:
            print("mendapatkan nilai C")
            print("tidak lulus")
        else: 
            if nilai >= 50 and nilai <= 59:
                print("mendapatkan nilai D")
                print("tidak lulus")
            else:
                if nilai <= 50:
                    print("mendapatkan nilai E")
                    print("tidak lulus")


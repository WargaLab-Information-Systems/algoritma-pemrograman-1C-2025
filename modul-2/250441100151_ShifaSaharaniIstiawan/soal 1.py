print("Masukkan nilai")
nilai = int(input())
if nilai >= 85 and nilai <= 100:
    print("nilai A")
    print("Masukan persentase Kehadiran")
    kehadiran = int(input())
    if kehadiran >= 90:
        if kehadiran <= 100:
            print("Lulus dengaan pujian")
    else:
        print("Lulus")
else:
    print("tidak sesuai")
    if nilai >= 70 and nilai <= 84:
        print("nilai B")
        print("Masukkan presentase kehadiran: ")
        kehadiran = int(input())
        if kehadiran >= 90:
            print("Lulus dengan pajak")
        else:
            print("Lulus")
    else:
        if nilai >= 60 and nilai >= 69:
            print("nilai C")
            print("Tidak Lulus")
        else:
            if nilai >= 50 and nilai >= 59:
                print("nilai D")
                print("Tidak Lulus")
            else:
                if nilai <= 50:
                    print("nilai e")
                    print("tidak lulus")

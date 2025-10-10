print("Masukan nilai siswa")
nilai = int(input())
if nilai > 85:
    print("Nilai A")
    print("Masukan persentase Kehadiran")
    status = input()
    if status > str(90) + "%":
        print("Lulus dengan pujian")
else:
    if nilai > 70:
        print("Nilai B")
    else:
        if nilai > 60:
            print("nilai B")
        else:
            if nilai > 50:
                print("Nilai D")
            else:
                print("Nilai E")
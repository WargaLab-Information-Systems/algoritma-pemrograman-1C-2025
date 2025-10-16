print("masukkan jumlah nilai mahasiswa(0-100)")
nilai = int(input())
print("nilai = " + str(nilai))
if nilai >= 85:
    print("A")
    print("masukkan jumlah persen kehadiran")
    kehadiran = int(input())
    print("kehadiran = " + str(kehadiran) + "%")
    if kehadiran >= 90:
        print("Lulus dengan Pujian")
else:
    if nilai >= 70:
        print("B")
    else:
        if nilai >= 60:
            print("C")
        else:
            if nilai >= 50:
                print("D")
            else:
                print("E")

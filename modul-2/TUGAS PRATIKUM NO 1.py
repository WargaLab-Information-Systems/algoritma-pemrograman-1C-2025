print("Masukkan Nilai: ")
nilai = int(input())
print("Masukkan Kehadiran Mahasiswa (0-100): ")
presentaseKehadiran = int(input())
if nilai >= 85 and presentaseKehadiran >= 90:
    print("Selamat anda LULUS dengan pujian nilai A")
else:
    if nilai > 85:
        print("Selamat anda LULUS dengan nilai A")
    else:
        if nilai >= 70 and nilai <= 84:
            print("Selamat anda LULUS dengan nilai B")
        else:
            if nilai >= 60 and nilai <= 69:
                print("Selamat anda LULUS dengan nilai C")
            else:
                if nilai >= 50 and nilai <= 59:
                    print("Maaf anda TIDAK LULUS dengan nilai D")
                else:
                    if nilai < 50:
                        print("Maaf anda TIDAK LULUS dengan nilai E")

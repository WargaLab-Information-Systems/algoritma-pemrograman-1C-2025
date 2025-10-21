print("Masukkan nilai  (1-100) : ")
nilai = int(input())
print("Masukkan kehadiran (1-100) : ")
kehadiran = int(input())
if nilai < 0 or nilai > 100:
    print("Nilai tidak valid, harus 1 - 100!")
else:
    if nilai >= 85:
        huruf = "A"
        if nilai >= 85 and kehadiran >= 90:
            status = "Baik Sekalii"
    else:
        if nilai >= 70 and nilai <= 84:
            huruf = "B"
        else:
            if nilai >= 60 and nilai <= 69:
                huruf = "C"
            else:
                if nilai >= 50 and nilai <= 59:
                    huruf = "D"
                else:
                    huruf = "E"
                    if huruf == "E":
                        status = "Tidak Lulus"
                    else:
                        status = "Lulus"

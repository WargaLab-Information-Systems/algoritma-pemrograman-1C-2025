print("masukkan nilai")
n = int(input())
print("masukkan kehadiran 1-100")
pk = int(input())
if n >= 85 and pk >= 90:
    print("selamat anda lulus dengan pujian, dengan nilai A")
else:
    if n >= 85:
        print("selamat anda lulus dengan nilai A")
    else:
        if n >= 70 and n < 85:
            print("anda lulus dengan nilai B")
        else:
            if n >= 60 and n < 70:
                print("anda lulus dengan nilai C")
            else:
                if n >= 50 and n < 60:
                    print("coba lagi, karena nilai anda D")
                else:
                    if n < 49:
                        print("coba lagi, karena nilai anda E")
                    else:
                        print("semangat")

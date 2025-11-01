n = int(input("Masukkan tinggi piramida: "))

for i in range(1, n + 1): #misal n=5 maka i akan 1,2,3,4,5
    for j in range(1, i + 1): #kr
        print(j, end="") #endagrtdkpndhbrs

    for spasi in range((n - i) * 2): #ruangtengah,smkinkbwhsmkindkit
        print(" ", end="")

    for k in range(i, 0, -1): #mulai dari angka i, turun sampai 1/sebaliknya yg kanan
        print(k, end="")

    print()  # ganti baris


#kr, 1
    #12
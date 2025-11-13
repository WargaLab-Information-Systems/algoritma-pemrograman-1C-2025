n = int(input("masukkan tinggi piramida: "))
for i in range(1, n+1):
    #sisi kieri piramia: mencetak angka dari 1 sampai i
    for j in range(1, i+1):
        print(j, end=" ")
    #ruang kosong di tengah untuk menjaga simetri
    for j in range(2*(n - i)):
        print(" ", end=" ")
    #sisi kanan piramida: mencetak angka dari i turun sampai 1
    for j in range(i, 0, -1):
        print(j, end= " ")
    print()



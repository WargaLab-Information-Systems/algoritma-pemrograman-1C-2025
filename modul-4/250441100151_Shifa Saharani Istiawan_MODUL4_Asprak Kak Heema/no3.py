n = int(input("Masukkan tinggi piramida : "))

for i in range(1, n + 1):
    for j in range(1, i + 1):  #sisi kiri piramida
        print(j, end="")

    spasi = 2 * (n - i)
    print(" " * spasi, end="") 
     
    for j in range(i, 0, -1):  #sisi kanan piramida
        print(j, end="")
    
    print()
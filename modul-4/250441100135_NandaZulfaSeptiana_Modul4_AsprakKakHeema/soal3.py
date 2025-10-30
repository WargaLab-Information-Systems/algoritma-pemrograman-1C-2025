tinggi = int(input("Masukkan tinggi piramida : "))

for i in range(1, tinggi + 1):
    for j in range(1, i + 1):
        print(j, end="")

    spasi = 2 * (tinggi - i)
    print(" " * spasi, end="") 
     
    for j in range(i, 0, -1):
        print(j, end="")
    
    print()



# Program Pola Dua Piramida Cermin
n = int(input("Masukkan tinggi piramida: "))

for c in range(1, n + 1):
    for o in range(1, c + 1):
        print(o, end=" ")
    
    for d in range(2 * (n - c)):
        print("  ", end="")
    
    for e in range(c, 0, -1):
        print(e, end=" ")
    print()
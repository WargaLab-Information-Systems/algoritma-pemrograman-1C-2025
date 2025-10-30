
n = int(input("Masukkan jumlah baris (n): "))

for i in range(n, 0, -1):
    for j in range(1, n - i + 2):
        print(j, end=' ')
    
    for s in range((i - 1) * 2):
        print(" ", end=' ')
    
    for j in range(n - i + 1, 0, -1):
        print(j, end=' ')
    
    print()


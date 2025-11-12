n = int(input("masukkan angka n: "))

for i in range(1, n + 1):
    for j in range(1, n - i + 2):
        print(j, end=' ')
    for k in range((i - 1) * 2):
        print(" ", end=' ')
    for j in range(n -i+1, 0,-1):
        print(j, end=' ') 
    print()


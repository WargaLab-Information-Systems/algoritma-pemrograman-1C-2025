n = int(input("Masukkan nilai n: "))
for i in range(1, n + 1):
    # kiri
    for j in range(1, i + 1):
        print(j, end="")
    # tengah
    print(" " * (2 * (n - i)), end="")
    # kanan
    for k in range(i, 0, -1):
        print(k, end="")
    print()





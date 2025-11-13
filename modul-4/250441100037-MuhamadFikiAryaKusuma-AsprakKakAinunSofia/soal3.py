n = int(input("Masukkan angka n: "))
for i in range(1, n + 1):
    # Sisi kiri piramida
    for j in range(1, i + 1):
        print(j, end=" ")
    # Ruang kosong di tengah
    for j in range(2 * (n - i)):
        print(" ", end=" ")
    # Sisi kanan piramida
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()

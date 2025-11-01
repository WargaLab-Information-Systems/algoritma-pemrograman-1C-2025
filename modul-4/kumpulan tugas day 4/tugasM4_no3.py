# Program Piramida Cermin Angka

n = int(input("Masukkan tinggi piramida (n): "))

for i in range(1, n + 1):
    # Sisi kiri piramida
    for j in range(1, n - i + 2):
        print(j, end=' ')
    # Spasi di tengah
    for k in range((i - 1) * 2):
        print(" ", end=' ')
    # Sisi kanan piramida
    for j in range(n - i + 1, 0, -1):
        print(j, end=' ')
    print()

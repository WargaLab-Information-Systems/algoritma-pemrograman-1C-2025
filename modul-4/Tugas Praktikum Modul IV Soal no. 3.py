
n = int(input("Masukkan tinggi piramida: "))

while n <= 0:
    print("Tidak Valid!")
    n = int(input("Masukkan tinggi piramida: "))

for i in range(n, 0, -1):

    for kiri in range(1, i + 1):
        print(format(kiri, '2d'), end='')

    for tengah in range(2 * (n - i)):
        print('  ', end='')

    for kanan in range(i, 0, -1):
        print(format(kanan, '2d'), end='')
    print()
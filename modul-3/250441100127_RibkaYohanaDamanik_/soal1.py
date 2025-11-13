n = int(input("Masukkan batas bilangan (n): "))

print("Bilangan prima dari 1 sampai", n, ":")

i = 2
while i <= n:
    j = 2
    hitung = 0
    while j <= i:
        if i % j == 0:
            hitung += 1
        j += 1
    if hitung == 1:  # hanya bisa dibagi oleh dirinya sendiri
        print(i, end=" ")
    i += 1
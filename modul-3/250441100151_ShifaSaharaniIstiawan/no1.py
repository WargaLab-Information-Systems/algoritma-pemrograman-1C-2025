n = int(input("Masukkan batas akhir: "))

print(f"Bilangan prima dari 1 sampai {n}:")
for i in range(2, n + 1):
    prima = 1
    for jumlah in range(2, int(i ** 0.5) + 1):
        if i % jumlah == 0:
            prima = 0
            break
    if prima:
        print(i, end=" ")

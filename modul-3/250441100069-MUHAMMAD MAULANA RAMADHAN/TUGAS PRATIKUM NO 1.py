n = int(input("Masukkan nilai n: "))

print(f"Bilangan prima dari 1 hingga {n}:")
for i in range(2, n + 1):
    prima = True
    for j in range(2, i):
        if i % j == 0:
            prima = False
            break
    if prima:
        print(i, end=" ")



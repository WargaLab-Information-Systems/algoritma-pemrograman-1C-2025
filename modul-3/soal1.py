n = int(input("Masukkan batas angka (n): "))

print(f"Bilangan prima dari 1 sampai {n} adalah:")

# Perulangan dari 2 hingga n
for i in range(2, n + 1):
    #  i adalah bilangan prima
    prima = True
    # Cek faktor dari 2 sampai i-1
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            prima = False
            break
    # Jika masih prima, tampilkan
    if prima:
        print(i, end=" ") 
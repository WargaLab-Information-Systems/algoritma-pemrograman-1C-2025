# Program menampilkan bilangan prima dari 1 sampai n

# Meminta input dari pengguna
n = int(input("Masukkan nilai n: "))

print(f"Bilangan prima dari 1 sampai {n} adalah:")

# Perulangan dari 2 sampai n
for i in range(2, n + 1):
    # Asumsikan i adalah bilangan prima
    is_prima = True
    # Cek apakah i memiliki faktor selain 1 dan dirinya sendiri
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            is_prima = False
            break
    # Jika tidak ada faktor, maka i adalah bilangan prima
    if is_prima:
        print(i, end=" ")

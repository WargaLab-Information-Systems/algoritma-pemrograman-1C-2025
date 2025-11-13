def faktorial(N):
    if N == 0:
        return 1
    else:
        return N * faktorial(N - 1)
# Contoh penggunaan dinamis
N = int(input("Masukkan bilangan bulat non-negatif N: "))
hasil = faktorial(N)
print(f"Faktorial dari {N} adalah {hasil}")
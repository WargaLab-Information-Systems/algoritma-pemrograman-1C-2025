while True:
    n = int(input("Masukkan bilangan bulat (n): "))
    if n < 0:
        print("Bilangan tidak valid! Masukkan bilangan positif (n)")
    else:
        break

def faktorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktorial(n - 1)

hasil = faktorial(n)
print(f"Faktorial dari {n} adalah {hasil}")



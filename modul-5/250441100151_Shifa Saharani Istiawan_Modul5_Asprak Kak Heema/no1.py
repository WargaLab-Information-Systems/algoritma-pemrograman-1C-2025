def faktorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktorial(n - 1)

# Program utama
try:
    n = int(input("Masukkan bilangan bulat non-negatif: "))
    if n < 0:
        print("Input tidak boleh negatif!")
    else:
        print(f"Faktorial dari {n} adalah {faktorial(n)}")
except ValueError:
    print("Input harus berupa bilangan bulat!")

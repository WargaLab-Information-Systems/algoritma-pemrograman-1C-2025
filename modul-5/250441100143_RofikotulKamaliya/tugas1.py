def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

n = input("Masukkan bilangan non-negatif: ")
if n.isdigit():
    n = int(n)
    print("Faktorial dari", n, "adalah:", factorial(n))
else:
    print("Input harus berupa angka dan termasuk bilangan bulat non-negatif!")
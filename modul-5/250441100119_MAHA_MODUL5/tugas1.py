def faktorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktorial(n - 1)

n = input("Masukkan bilangan bulat non-negatif: ")

if not n.isdigit():
    print("Input tidak sesuai, valid")
else:
    n = int(n)
    if n < 0:
        print("Bilangan tidak boleh negatif!")
    else:
        hasil = faktorial(n)
        print(f"Faktorial dari {n} adalah: {hasil}")

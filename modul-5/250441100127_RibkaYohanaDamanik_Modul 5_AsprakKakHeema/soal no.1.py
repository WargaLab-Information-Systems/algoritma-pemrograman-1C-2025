def faktorial_iteratif(n):
    hasil = 1
    for i in range(1, n + 1):
        hasil *= i
    return hasil


# Program dinamis
try:
    N = int(input("Masukkan bilangan bulat non-negatif: "))

    if N < 0:
        print("Angka harus non-negatif!")
    else:
        print(f"Faktorial dari {N} adalah = {faktorial_iteratif(N)}")

except ValueError:
    print("Input harus bilangan bulat!")

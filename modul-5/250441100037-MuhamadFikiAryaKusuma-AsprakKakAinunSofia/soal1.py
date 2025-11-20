def hitung_faktorial (n):
    if n == 1:
        return 1
    else:
        return n * hitung_faktorial(n-1)
n= int(input("Masukkan angka untuk menghitung faktorial: "))

for i in range(n,0,-1):
    print(i, end=" ")
    if i != 1:
        print("x", end=" ")
print("= ", hitung_faktorial(n))
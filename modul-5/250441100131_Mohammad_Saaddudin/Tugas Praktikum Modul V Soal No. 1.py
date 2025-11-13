def faktorial (n):
    if n == 0 or n ==1:
        return 1
    else:
        return n * faktorial(n-1)
    
while True:
    try:
        n = int(input("masukkan bilangan bulat non-negatif: "))
        if n < 0:
            print("bilangan tidak boleh negatif! coba lagi")
            continue

        hasil = faktorial(n)
        print(f"faktorial dari {n} adalah: {hasil}")
        break
    except ValueError:
        print("input tidak valid! masukkan bilangan bulat")


    
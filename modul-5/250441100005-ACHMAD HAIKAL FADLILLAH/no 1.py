def faktorial(n):
    
    if n == 0 or n == 1:
        return 1    
    elif n >= 1:
        return n * faktorial(n - 1)    
    else:
        return "Error!! harus bilangan bulat dan bukan bilangan negatif!"

n = int(input("masukkan bilangan : "))
print ("faktorial dari", n, "adalah", faktorial(n))
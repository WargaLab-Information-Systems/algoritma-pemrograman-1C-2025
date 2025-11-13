n=int(input("input faktorial = "))

def faktorial(n):
    #print(n)
    if n == 0 or n == 1: 
        return 1
    else:
        #print(n)
        return n * faktorial(n - 1)  
print(faktorial(n))

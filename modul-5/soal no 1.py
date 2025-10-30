def faktorial(n):
    if n == 0:
        return 1
    else:
        return n * faktorial(n-1)
    
try:
    bilangan = int(input("masukkan bilangan bulat non negatif untuk dihitung faktorialnya: "))
    if bilangan <0:
        print("maaf, faktorial tidak untuk bilangan negatif.")
    else:
        hasil_faktorial = faktorial(bilangan)
        print(f"faktorial dari {bilangan} adalah : {hasil_faktorial}")
except ValueError:
    print("input yang dimasukkan tidak valid. harap masukkan bilangan bulat.")
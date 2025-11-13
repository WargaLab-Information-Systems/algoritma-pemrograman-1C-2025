def faktorial(n):
    
    if n < 0:
        return "Input harus bilangan bulat non-negatif."
    
    if n == 0 or n == 1:
        return 1
    hasil = 1
    
    for i in range(1, n + 1):
        hasil = hasil * i
        
    return hasil

input_n = int(input("Masukkan bilangan bulat (n) untuk dihitung faktorialnya: "))

hasil_faktorial = faktorial(input_n)

print(f"\nFaktorial dari {input_n}! adalah: {hasil_faktorial}")
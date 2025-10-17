n = int(input("Masukkan nilai n: "))

print(f"Bilangan prima dari 1 sampai {n} adalah:")

for i in range(2, n + 1): 
    
    prima = True
    for a in range(2, i): #pakek for lagi takut ada bilagan yg msih bs di bgi
        if i % a == 0:  
            prima = False  #kalo sudah flse di break
            break
    if prima:
        print(i)

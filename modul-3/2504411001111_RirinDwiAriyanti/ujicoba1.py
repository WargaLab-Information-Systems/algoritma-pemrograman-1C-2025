# Mencari bilangan prima
n = int(input("Masukkan batas bilangan: "))
print("Bilangan prima dari 1 sampai", n ,"adalah:")

for i in range(2, n + 1):  
    prima = True
    for jumlah in range(2, i): 
        if i % jumlah == 0:
            prima = False
            break
    else:
        print(i,end=" , ")
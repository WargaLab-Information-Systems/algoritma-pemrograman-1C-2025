#Mencari bilangan prima
n = int(input("Masukkan batas bilangan: "))
print("Bilangan prima dari 1 sampai", n ,"adalah:")

for i in range(2, n + 1):  # mulai dari 2 karena 1 bukan bilangan prima
    prima = True
    for j in range(2, i): #j sebagai bilangan pembagi apakah i adalah bilangan prima
        if i % j == 0:
            prima = False
            break
    else:
        print(i, end=" ")
   
   
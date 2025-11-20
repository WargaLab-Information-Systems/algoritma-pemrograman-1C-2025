n = int(input("masukkan nilai n:"))

print(f"bilangan prima dari 1 sampai n yaitu:")

for i in range (2, n + 1):
    for j in range (2, i):
        if i % j == 0:             
            break
    else:
        print(i, end=" ")
        
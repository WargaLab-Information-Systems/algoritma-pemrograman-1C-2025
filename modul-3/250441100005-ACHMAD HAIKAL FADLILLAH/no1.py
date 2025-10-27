n = int (input("masukkan angka: "))
print(f"bilangan prima dari 1 sampai {n} adalah:")

for i in range (2, n + 1) :
    prima = True
    for a in range (2, int (i ** 0.5) + 1) :
        if i % a == 0 :
            prima = False
            break
    if prima :
        print(i, end=", ")

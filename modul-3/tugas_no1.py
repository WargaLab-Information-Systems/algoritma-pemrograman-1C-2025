n = int(input("masukkan nilai n:"))

print(f"bilangan prima dari 1 sampai n yaitu:")

for i in range (2, n + 1):
    for j in range (2, i):
        if i % j == 0:             
            break
    else:
        print(i, end=" ")

# j cek i itu blgn prima or not
# klo i hsil dibgi j berarti i bs dibgi angka lain selain 1 n herself
# krn udh bkn prima, jd stop j 
# JANGAN PAKE TRUE FALSE
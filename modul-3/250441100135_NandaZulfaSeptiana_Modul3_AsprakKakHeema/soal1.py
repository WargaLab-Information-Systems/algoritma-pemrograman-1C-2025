bil = int(input("Masukkan nilai: "))

print("Bilangan prima dari 1 sampai", bil, "adalah:")
for i in range(2, bil + 1):
    for jml in range(2, i):
        if i % jml == 0:
            break
    else:
        print(i, end=" ")

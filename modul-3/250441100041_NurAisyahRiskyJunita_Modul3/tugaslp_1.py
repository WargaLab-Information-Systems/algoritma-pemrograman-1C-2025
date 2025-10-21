# Program menampilkan bilangan prima dari 1 sampai n

n = int(input("Masukkan batas angka (n): "))

print(f"\nBilangan prima dari 1 sampai {n} adalah:")

for i in range(2, n + 1):
    prima = True  # anggap dulu semua bilangan adalah prima
    for j in range(2, i):
        if i % j == 0:  # jika ada pembagi lain
            prima = False
            break
    if prima:
        print(i, end=" ")
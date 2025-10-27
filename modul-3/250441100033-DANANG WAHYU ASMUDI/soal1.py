# Program menampilkan bilangan prima dari 1 sampai n
# Input batas bilangan
n = int(input("Masukkan batas bilangan: "))
if n < 2:
    print("Input tidak valid! Bilangan prima dimulai dari 2.")
else:
    print(f"Bilangan prima dari 1 sampai {n} adalah:")

    # Periksa setiap bilangan dari 2 sampai n
    for i in range(2, n+1):
        prima = True
        for j in range(2, i):
            if i % j == 0:
                prima = False
                break
        if prima:
            print(i)
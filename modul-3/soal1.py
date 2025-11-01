main
# Tugas no 1

batas = int(input("masukkan batas angka akhir :"))

print("Bilangan prima dari 1 sampai", batas, ":")

for angka in range(2, batas + 1):
    prima = True
    for pembagi in range(2, angka):
        if angka % pembagi == 0:
            prima = False
            break
    if prima:
        print(angka)

n = int(input("Masukkan batas angka (n): "))

print(f"Bilangan prima dari 1 sampai {n} adalah:")

# Perulangan dari 2 hingga n
for i in range(2, n + 1):
    #  i adalah bilangan prima
    prima = True
    # Cek faktor dari 2 sampai i-1
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            prima = False
            break
    # Jika masih prima, tampilkan
    if prima:
        print(i, end=" ") 
main

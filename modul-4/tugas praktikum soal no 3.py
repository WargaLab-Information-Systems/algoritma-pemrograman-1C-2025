n = int(input("Masukkan nilai n: "))

print("pola piramida angka mirorr:")

for i in range(1, n + 1):
    # piramida kiri - angka menurun
    for j in range(i, 0, -1):
        print(j, end="")
    
    # spasi di tengah
    for k in range(2 * (n - i) + 2):
        print(" ", end="")
    
    # piramida kanan - angka menaik
    for l in range(1, i + 1):
        print(l, end="")
    
    print()  # pindah baris
# Piramida angka saling berhadapan (bisa lebih dari 9)
n = int(input("Masukkan tinggi piramida (n): "))

for i in range(1, n + 1): #untuk setiap baris dari 1 sampai n
    for j in range(n, i - 1, -1): #mencetak angka dari n turun ke i, -1 untuk urutan menurun
        print(f"{j:3}", end="") # mencetak anngka dengan lebar 3, f" digunakan untuk string
    for spasi in range(1, (i - 1) * 6 + 1): # mencetak spasi ditengah piramida, i-1*6 untuk mengatur jarak antara dua sisi piramida contohnya i = 2 maka spasi = 6
        print(" ", end="") # cetak spasi tanpa pindah baris
    for j in range(i, n + 1): # mencetak angka dari i smapai n
        print(f"{j:3}", end="")# angka dengan lebar 3
    print()
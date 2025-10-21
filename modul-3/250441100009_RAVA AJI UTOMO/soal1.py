batas_atas = int(input("Masukkan nilai n: "))  # Input dari pengguna
print("Bilangan prima dari 1 sampai", batas_atas, "adalah:")
for angka in range(2, batas_atas + 1): 
    adalah_prima = True  # Asumsi awal prima
    pembagi = 2
    while pembagi * pembagi <= angka:
        if angka % pembagi == 0:
            adalah_prima = False  # Bukan prima jika ada pembagi
            break  
        pembagi += 1
    if adalah_prima:
        print(angka)  
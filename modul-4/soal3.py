# Meminta input n
n = int(input("Masukkan tinggi piramida (n): "))
# Loop untuk setiap baris (dari 1 hingga n)
for i in range(1, n + 1):
    # Loop untuk sisi kiri piramida: cetak angka dari 1 hingga i
    for j in range(1, n - i + 2):
        print(j, end=' ')
    
    # Loop untuk ruang kosong di tengah: cetak 2 spasi
    for k in range((i  - 1) * 2):
        print(" ", end=' ')
    
    # Loop untuk sisi kanan piramida: cetak angka dari i hingga 1
    for j in range(n - i + 1, 0, -1):
        print(j, end=' ')
    
    # Pindah ke baris baru
    print()